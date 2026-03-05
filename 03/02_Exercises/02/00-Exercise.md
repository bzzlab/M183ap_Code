### Exercise: XOR encoding (Crypto Basics - Introduction to XOR Encoding)
###  Prerequisite
1. You have a python runtime version 3.x installed 

### Introduction
With the so-called "default XOR encoding", which isn’t a formally defined standard, IT professionals usually mean:
Plaintext → XOR with a key (often a single byte) → Base64 encode
XOR (especially single-byte XOR) is not secure — it's obfuscation, not encryption.
It’s fine for Malware analysis, learning cryptography basics but definitely NOT advisable for protecting information.


### Task - XOR encoding with Python scripts
Before you continue your journey on OWASP A2 - Cryptographic Failures
you need some tools in order to progress.

1. As a preparation task fill the gaps to the provided python script ```xorb64tool.py```. See therefore the example output of the tool.
2. Decode with the xorb64tool the following string 
```
Un92dnU6TXVodn47
```

