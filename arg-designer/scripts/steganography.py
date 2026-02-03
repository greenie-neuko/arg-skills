#!/usr/bin/env python3
"""
ARG Steganography Tools - Hide and extract messages in images and audio.

Usage:
    python steganography.py hide-image <image> <message> <output>
    python steganography.py extract-image <image>
    python steganography.py hide-metadata <file> <message> <output>
    python steganography.py extract-metadata <file>
    python steganography.py unicode-hide <text> <message>
    python steganography.py unicode-extract <text>

Requirements:
    pip install pillow numpy
"""

import argparse
import os
import sys

def hide_in_image_lsb(image_path: str, message: str, output_path: str):
    """Hide message in image using LSB steganography."""
    try:
        from PIL import Image
        import numpy as np
    except ImportError:
        print("Error: Requires 'pillow' and 'numpy'. Install with: pip install pillow numpy")
        sys.exit(1)

    # Load image
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = np.array(img)

    # Prepare message with length header and terminator
    message_bytes = message.encode('utf-8')
    length = len(message_bytes)
    data = length.to_bytes(4, 'big') + message_bytes

    # Check capacity
    max_bytes = (pixels.size // 8)
    if len(data) > max_bytes:
        print(f"Error: Message too large. Max {max_bytes} bytes, got {len(data)}")
        sys.exit(1)

    # Convert to bits
    bits = ''.join(format(byte, '08b') for byte in data)

    # Hide bits in LSB
    flat_pixels = pixels.flatten()
    for i, bit in enumerate(bits):
        flat_pixels[i] = (flat_pixels[i] & 0xFE) | int(bit)

    # Save
    result = flat_pixels.reshape(pixels.shape)
    Image.fromarray(result.astype(np.uint8)).save(output_path)
    print(f"Message hidden in {output_path}")
    print(f"Capacity used: {len(data)}/{max_bytes} bytes ({100*len(data)/max_bytes:.1f}%)")


def extract_from_image_lsb(image_path: str) -> str:
    """Extract message from image using LSB steganography."""
    try:
        from PIL import Image
        import numpy as np
    except ImportError:
        print("Error: Requires 'pillow' and 'numpy'. Install with: pip install pillow numpy")
        sys.exit(1)

    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = np.array(img).flatten()

    # Extract length (first 32 bits)
    length_bits = ''.join(str(pixels[i] & 1) for i in range(32))
    length = int(length_bits, 2)

    # Sanity check
    if length > len(pixels) // 8 or length < 0:
        print("No valid message found or image not encoded")
        return ""

    # Extract message
    message_bits = ''.join(str(pixels[i] & 1) for i in range(32, 32 + length * 8))
    message_bytes = bytes(int(message_bits[i:i+8], 2) for i in range(0, len(message_bits), 8))

    try:
        return message_bytes.decode('utf-8')
    except UnicodeDecodeError:
        print("Warning: Could not decode as UTF-8, returning raw bytes")
        return str(message_bytes)


def hide_in_metadata(file_path: str, message: str, output_path: str):
    """Hide message in file EXIF/metadata (for images)."""
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
    except ImportError:
        print("Error: Requires 'pillow'. Install with: pip install pillow")
        sys.exit(1)

    img = Image.open(file_path)

    # For JPEG/PNG, we can add to info dict
    if img.format in ['JPEG', 'PNG']:
        # Copy the image with metadata
        img_copy = img.copy()

        # Add comment
        if img.format == 'PNG':
            from PIL import PngImagePlugin
            meta = PngImagePlugin.PngInfo()
            meta.add_text("Comment", message)
            img_copy.save(output_path, pnginfo=meta)
        else:
            # For JPEG, use EXIF comment (limited support)
            img_copy.save(output_path)
            print("Note: JPEG metadata hiding has limited support. Consider PNG.")

        print(f"Message hidden in metadata of {output_path}")
    else:
        print(f"Unsupported format: {img.format}")


def extract_from_metadata(file_path: str) -> str:
    """Extract message from file metadata."""
    try:
        from PIL import Image
    except ImportError:
        print("Error: Requires 'pillow'. Install with: pip install pillow")
        sys.exit(1)

    img = Image.open(file_path)

    # Check PNG text chunks
    if 'Comment' in img.info:
        return img.info['Comment']

    # Check all info
    for key, value in img.info.items():
        if isinstance(value, str) and len(value) > 0:
            print(f"{key}: {value}")

    # Check EXIF
    if hasattr(img, '_getexif') and img._getexif():
        exif = img._getexif()
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"EXIF {tag}: {value}")

    return ""


def unicode_hide(text: str, message: str) -> str:
    """Hide message using zero-width Unicode characters."""
    # Zero-width space (U+200B) = 0
    # Zero-width non-joiner (U+200C) = 1
    ZERO = '\u200b'
    ONE = '\u200c'

    # Convert message to binary
    binary = ''.join(format(ord(c), '08b') for c in message)
    hidden = ''.join(ZERO if b == '0' else ONE for b in binary)

    # Insert at beginning or middle of text
    mid = len(text) // 2
    return text[:mid] + hidden + text[mid:]


def unicode_extract(text: str) -> str:
    """Extract message from zero-width Unicode characters."""
    ZERO = '\u200b'
    ONE = '\u200c'

    # Extract binary
    binary = ''
    for char in text:
        if char == ZERO:
            binary += '0'
        elif char == ONE:
            binary += '1'

    if not binary:
        return ""

    # Convert to text
    chars = []
    for i in range(0, len(binary) - 7, 8):
        byte = binary[i:i+8]
        chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def main():
    parser = argparse.ArgumentParser(description='ARG Steganography Tools')
    subparsers = parser.add_subparsers(dest='command', help='Command')

    # Hide in image
    hide_img = subparsers.add_parser('hide-image', help='Hide message in image (LSB)')
    hide_img.add_argument('image', help='Input image file')
    hide_img.add_argument('message', help='Message to hide')
    hide_img.add_argument('output', help='Output image file')

    # Extract from image
    extract_img = subparsers.add_parser('extract-image', help='Extract message from image')
    extract_img.add_argument('image', help='Image file with hidden message')

    # Hide in metadata
    hide_meta = subparsers.add_parser('hide-metadata', help='Hide message in metadata')
    hide_meta.add_argument('file', help='Input file')
    hide_meta.add_argument('message', help='Message to hide')
    hide_meta.add_argument('output', help='Output file')

    # Extract from metadata
    extract_meta = subparsers.add_parser('extract-metadata', help='Extract from metadata')
    extract_meta.add_argument('file', help='File with metadata')

    # Unicode hide
    uni_hide = subparsers.add_parser('unicode-hide', help='Hide in zero-width Unicode')
    uni_hide.add_argument('text', help='Cover text')
    uni_hide.add_argument('message', help='Message to hide')

    # Unicode extract
    uni_extract = subparsers.add_parser('unicode-extract', help='Extract from zero-width Unicode')
    uni_extract.add_argument('text', help='Text with hidden message')

    args = parser.parse_args()

    if args.command == 'hide-image':
        hide_in_image_lsb(args.image, args.message, args.output)
    elif args.command == 'extract-image':
        message = extract_from_image_lsb(args.image)
        if message:
            print(f"Extracted message: {message}")
    elif args.command == 'hide-metadata':
        hide_in_metadata(args.file, args.message, args.output)
    elif args.command == 'extract-metadata':
        message = extract_from_metadata(args.file)
        if message:
            print(f"Extracted: {message}")
    elif args.command == 'unicode-hide':
        result = unicode_hide(args.text, args.message)
        print(f"Result (copy this): {result}")
        print(f"Visible length: {len(args.text)}, Actual length: {len(result)}")
    elif args.command == 'unicode-extract':
        message = unicode_extract(args.text)
        if message:
            print(f"Hidden message: {message}")
        else:
            print("No hidden message found")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
