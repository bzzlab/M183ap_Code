# Python script: auto-detect hash type
# Hash auto-detection is heuristic-based, not guaranteed. Why?
# * Many hash algorithms produce the same length
# * Encodings (hex / base64) overlap
# * Salts can change everything
#
# So what we do is educated guessing based on:
# * Length
# * Character set
# * Common patterns
#
# That’s usually good enough as first move.
#
# Common hash fingerprints
# | Length | Charset                    | Likely Hash         |
# | ------ | -------------------------- | ------------------- |
# | 32     | hex                        | MD5                 |
# | 40     | hex                        | SHA1                |
# | 56     | hex                        | SHA224              |
# | 64     | hex                        | SHA256              |
# | 96     | hex                        | SHA384              |
# | 128    | hex                        | SHA512              |
# | 32     | hex, starts with `$P$`     | PHPass              |
# | 34     | starts with `$2a$`, `$2b$` | bcrypt              |
# | varies | base64                     | SHA / HMAC / custom |
# | varies | contains `:`               | salted / combo      |
#
# Example
# python plainhash3.py
# Enter hash: 8D969E....
# [+]
# Possible
# algorithms: SHA256
# [+]
# Trying SHA256...
# � MATCH FOUND �
# Algorithm: SHA256
# Password: <try-yourself :-) >


import hashlib
import re

def detect_algorithms(hash_value: str):
    hash_value = hash_value.strip()
    algos = []

    if re.fullmatch(r"[a-fA-F0-9]+", hash_value):
        length = len(hash_value)

#??
#??
#??
#??
#??
#??
#??
#??
#??
#??
#??
#??
#??
#??

    return algos

def hash_text(text: str, algo: str) -> str:
#??
#??
    return h.hexdigest().upper()

def crack_hash(hash_value: str, passwords: list):
    hash_value = hash_value.upper()
    algos = detect_algorithms(hash_value)

    if not algos:
        print("[-] Unable to detect hash type")
        return

    print(f"[+] Possible algorithms: {', '.join(algos)}")

#??
#??
#??
#??
#??
#??
#??
#??
#??

    print("[-] No match found")

def main():
    hash_value = input("Enter hash: ")

    with open("wordlist.txt", "r", encoding="utf-8", errors="ignore") as f:
        passwords = [line.strip() for line in f]
        crack_hash(hash_value, passwords)

if __name__ == "__main__":
    main()

