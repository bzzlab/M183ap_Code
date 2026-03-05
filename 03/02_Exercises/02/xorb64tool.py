# Python script for XOR + Base64 encoding/decoding
# - Encodes text using XOR + Base64
# - Decodes Base64 + XOR
# - Uses a single-byte XOR key (the most common “default” XOR style)
#
# Example:
# python xorb64tool.py
# Enter the text: What is the meaning of life?
# Type 'e' to encode or 'd' to decode: e
# Enter XOR key (0–255): 25
# Encoded text:
# TnF4bTlwajltcXw5dHx4d3B3fjl2fzl1cH98Jg==

import base64

def xor_data(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)

def encode_xor_base64(text: str, key: int) -> str:
#??
#??

def decode_xor_base64(encoded_text: str, key: int) -> str:
#??
#??
#??

def main():
    text = input("Enter the text: ")
    mode = input("Type 'e' to encode or 'd' to decode: ").strip().lower()
    key = int(input("Enter XOR key (0–255): "))

    if mode == "e":
        print(f"Encoded text: {encode_xor_base64(text, key)}")
    elif mode == "d":
        print(f"Decoded text: {decode_xor_base64(text, key)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
