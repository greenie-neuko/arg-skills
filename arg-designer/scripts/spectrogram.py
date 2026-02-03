#!/usr/bin/env python3
"""
ARG Spectrogram Tools - Create and analyze audio spectrograms.

Usage:
    python spectrogram.py image-to-audio <image> <output.wav> [--duration SECONDS]
    python spectrogram.py text-to-audio <text> <output.wav> [--duration SECONDS]
    python spectrogram.py view <audio_file> [--output IMAGE]

Requirements:
    pip install pillow numpy scipy matplotlib
"""

import argparse
import sys


def image_to_spectrogram_audio(image_path: str, output_path: str, duration: float = 5.0):
    """Convert image to audio that displays the image as a spectrogram."""
    try:
        from PIL import Image
        import numpy as np
        from scipy.io import wavfile
    except ImportError:
        print("Error: Requires 'pillow', 'numpy', 'scipy'. Install with:")
        print("  pip install pillow numpy scipy")
        sys.exit(1)

    # Load and prepare image
    img = Image.open(image_path).convert('L')  # Grayscale

    # Resize to reasonable spectrogram dimensions
    width = 800
    height = 256  # Frequency bins
    img = img.resize((width, height))

    # Convert to numpy array (flip vertically so low frequencies are at bottom)
    pixels = np.array(img)
    pixels = np.flipud(pixels)

    # Normalize to 0-1
    pixels = pixels / 255.0

    # Audio parameters
    sample_rate = 44100
    num_samples = int(duration * sample_rate)
    samples_per_column = num_samples // width

    # Frequency range (Hz)
    min_freq = 200
    max_freq = 8000

    # Generate frequencies for each row
    frequencies = np.linspace(min_freq, max_freq, height)

    # Generate audio
    audio = np.zeros(num_samples)

    for col in range(width):
        start_sample = col * samples_per_column
        end_sample = start_sample + samples_per_column
        t = np.arange(samples_per_column) / sample_rate

        for row in range(height):
            amplitude = pixels[row, col]
            if amplitude > 0.1:  # Threshold to reduce noise
                freq = frequencies[row]
                audio[start_sample:end_sample] += amplitude * np.sin(2 * np.pi * freq * t)

    # Normalize
    audio = audio / np.max(np.abs(audio)) * 0.8

    # Convert to 16-bit
    audio_int = (audio * 32767).astype(np.int16)

    # Save
    wavfile.write(output_path, sample_rate, audio_int)
    print(f"Created audio file: {output_path}")
    print(f"Duration: {duration}s, Sample rate: {sample_rate}Hz")
    print(f"View with: python spectrogram.py view {output_path}")


def text_to_spectrogram_audio(text: str, output_path: str, duration: float = 3.0):
    """Create audio with text visible in spectrogram."""
    try:
        from PIL import Image, ImageDraw, ImageFont
        import numpy as np
    except ImportError:
        print("Error: Requires 'pillow', 'numpy'. Install with: pip install pillow numpy")
        sys.exit(1)

    # Create text image
    width = 800
    height = 256

    img = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fall back to default
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
        except:
            font = ImageFont.load_default()

    # Calculate text position (centered)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), text, fill=255, font=font)

    # Save temp image then convert
    temp_path = "/tmp/temp_spectrogram_text.png"
    img.save(temp_path)

    image_to_spectrogram_audio(temp_path, output_path, duration)


def view_spectrogram(audio_path: str, output_path: str = None):
    """View/save spectrogram of audio file."""
    try:
        import numpy as np
        from scipy.io import wavfile
        from scipy import signal
        import matplotlib.pyplot as plt
    except ImportError:
        print("Error: Requires 'numpy', 'scipy', 'matplotlib'. Install with:")
        print("  pip install numpy scipy matplotlib")
        sys.exit(1)

    # Load audio
    sample_rate, audio = wavfile.read(audio_path)

    # Handle stereo
    if len(audio.shape) > 1:
        audio = audio[:, 0]

    # Convert to float
    audio = audio.astype(float) / 32768.0

    # Compute spectrogram
    frequencies, times, spectrogram = signal.spectrogram(
        audio, sample_rate, nperseg=1024, noverlap=512
    )

    # Plot
    plt.figure(figsize=(12, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram + 1e-10), shading='gouraud')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.title(f'Spectrogram: {audio_path}')
    plt.colorbar(label='Power (dB)')
    plt.ylim(0, 10000)  # Limit to reasonable frequency range

    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"Saved spectrogram to: {output_path}")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description='ARG Spectrogram Tools')
    subparsers = parser.add_subparsers(dest='command', help='Command')

    # Image to audio
    img2aud = subparsers.add_parser('image-to-audio', help='Convert image to spectrogram audio')
    img2aud.add_argument('image', help='Input image file')
    img2aud.add_argument('output', help='Output WAV file')
    img2aud.add_argument('--duration', '-d', type=float, default=5.0, help='Duration in seconds')

    # Text to audio
    txt2aud = subparsers.add_parser('text-to-audio', help='Create audio with text in spectrogram')
    txt2aud.add_argument('text', help='Text to embed')
    txt2aud.add_argument('output', help='Output WAV file')
    txt2aud.add_argument('--duration', '-d', type=float, default=3.0, help='Duration in seconds')

    # View spectrogram
    view = subparsers.add_parser('view', help='View/save spectrogram of audio')
    view.add_argument('audio', help='Audio file to analyze')
    view.add_argument('--output', '-o', help='Save spectrogram to image file')

    args = parser.parse_args()

    if args.command == 'image-to-audio':
        image_to_spectrogram_audio(args.image, args.output, args.duration)
    elif args.command == 'text-to-audio':
        text_to_spectrogram_audio(args.text, args.output, args.duration)
    elif args.command == 'view':
        view_spectrogram(args.audio, args.output)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
