#!/usr/bin/env python3
"""
ARG Cipher Tools - Encode and decode common ciphers used in ARGs.

Usage:
    python cipher_tools.py encode <cipher> <text> [--key KEY]
    python cipher_tools.py decode <cipher> <text> [--key KEY]
    python cipher_tools.py list

Supported ciphers:
    caesar, rot13, atbash, vigenere, railfence, base64, morse, binary, hex
"""

import argparse
import base64
import string

# Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}
MORSE_DECODE = {v: k for k, v in MORSE_CODE.items()}


def caesar_encode(text: str, shift: int = 3) -> str:
    """Caesar cipher encoding."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


def caesar_decode(text: str, shift: int = 3) -> str:
    """Caesar cipher decoding."""
    return caesar_encode(text, -shift)


def rot13(text: str) -> str:
    """ROT13 encoding/decoding (self-reciprocal)."""
    return caesar_encode(text, 13)


def atbash(text: str) -> str:
    """Atbash cipher (self-reciprocal)."""
    result = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(chr(155 - ord(char)))
            else:
                result.append(chr(219 - ord(char)))
        else:
            result.append(char)
    return ''.join(result)


def vigenere_encode(text: str, key: str) -> str:
    """Vigenère cipher encoding."""
    if not key:
        raise ValueError("Vigenère cipher requires a key")
    key = key.upper()
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


def vigenere_decode(text: str, key: str) -> str:
    """Vigenère cipher decoding."""
    if not key:
        raise ValueError("Vigenère cipher requires a key")
    key = key.upper()
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


def railfence_encode(text: str, rails: int = 3) -> str:
    """Rail fence cipher encoding."""
    if rails < 2:
        return text
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join([''.join(row) for row in fence])


def railfence_decode(text: str, rails: int = 3) -> str:
    """Rail fence cipher decoding."""
    if rails < 2:
        return text
    n = len(text)
    # Calculate lengths of each rail
    lengths = [0] * rails
    rail = 0
    direction = 1
    for _ in range(n):
        lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    # Split text into rails
    fence = []
    pos = 0
    for length in lengths:
        fence.append(list(text[pos:pos + length]))
        pos += length
    # Read off in zigzag pattern
    result = []
    indices = [0] * rails
    rail = 0
    direction = 1
    for _ in range(n):
        result.append(fence[rail][indices[rail]])
        indices[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join(result)


def base64_encode(text: str) -> str:
    """Base64 encoding."""
    return base64.b64encode(text.encode()).decode()


def base64_decode(text: str) -> str:
    """Base64 decoding."""
    return base64.b64decode(text.encode()).decode()


def morse_encode(text: str) -> str:
    """Morse code encoding."""
    return ' '.join(MORSE_CODE.get(c.upper(), c) for c in text)


def morse_decode(text: str) -> str:
    """Morse code decoding."""
    return ''.join(MORSE_DECODE.get(code, code) for code in text.split())


def binary_encode(text: str) -> str:
    """Binary encoding (8-bit ASCII)."""
    return ' '.join(format(ord(c), '08b') for c in text)


def binary_decode(text: str) -> str:
    """Binary decoding."""
    bits = text.replace(' ', '')
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))


def hex_encode(text: str) -> str:
    """Hexadecimal encoding."""
    return ' '.join(format(ord(c), '02x') for c in text)


def hex_decode(text: str) -> str:
    """Hexadecimal decoding."""
    hex_str = text.replace(' ', '')
    return bytes.fromhex(hex_str).decode()


CIPHERS = {
    'caesar': {'encode': caesar_encode, 'decode': caesar_decode, 'key_type': 'int'},
    'rot13': {'encode': rot13, 'decode': rot13, 'key_type': None},
    'atbash': {'encode': atbash, 'decode': atbash, 'key_type': None},
    'vigenere': {'encode': vigenere_encode, 'decode': vigenere_decode, 'key_type': 'str'},
    'railfence': {'encode': railfence_encode, 'decode': railfence_decode, 'key_type': 'int'},
    'base64': {'encode': base64_encode, 'decode': base64_decode, 'key_type': None},
    'morse': {'encode': morse_encode, 'decode': morse_decode, 'key_type': None},
    'binary': {'encode': binary_encode, 'decode': binary_decode, 'key_type': None},
    'hex': {'encode': hex_encode, 'decode': hex_decode, 'key_type': None},
}


def main():
    parser = argparse.ArgumentParser(description='ARG Cipher Tools')
    subparsers = parser.add_subparsers(dest='command', help='Command')

    # Encode command
    encode_parser = subparsers.add_parser('encode', help='Encode text')
    encode_parser.add_argument('cipher', choices=CIPHERS.keys(), help='Cipher to use')
    encode_parser.add_argument('text', help='Text to encode')
    encode_parser.add_argument('--key', '-k', help='Key (for ciphers that require one)')

    # Decode command
    decode_parser = subparsers.add_parser('decode', help='Decode text')
    decode_parser.add_argument('cipher', choices=CIPHERS.keys(), help='Cipher to use')
    decode_parser.add_argument('text', help='Text to decode')
    decode_parser.add_argument('--key', '-k', help='Key (for ciphers that require one)')

    # List command
    subparsers.add_parser('list', help='List available ciphers')

    args = parser.parse_args()

    if args.command == 'list':
        print("Available ciphers:")
        for name, info in CIPHERS.items():
            key_info = f" (requires {info['key_type']} key)" if info['key_type'] else ""
            print(f"  {name}{key_info}")
        return

    if not args.command:
        parser.print_help()
        return

    cipher_info = CIPHERS[args.cipher]
    func = cipher_info['encode'] if args.command == 'encode' else cipher_info['decode']

    # Handle key parameter
    if cipher_info['key_type'] == 'int':
        key = int(args.key) if args.key else 3
        result = func(args.text, key)
    elif cipher_info['key_type'] == 'str':
        if not args.key:
            print(f"Error: {args.cipher} cipher requires a key (--key)")
            return
        result = func(args.text, args.key)
    else:
        result = func(args.text)

    print(result)


if __name__ == '__main__':
    main()
