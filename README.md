# HashDead
## Overview
 [`hashdead`](https://github.com/HBlackGhost/hashdead.git) hashdead script cracks hashes by comparing hashes generated from a wordlist with a
provided hash file. It supports MD5, SHA-1, and SHA-256 algorithms
## Features
- Supports MD5, SHA-1, and SHA-256 hashing algorithms.
- Uses a wordlist to crack hashes efficiently.
## Options 
  `-h, --help `        Show this help message and exit
  
  `-A ALGORITHM`       Your Hash Algorithm
  
  `-HF HASH_FILE `     Your Hash File That You Want To Crack
  
 ` -W WORDLIST`        Your Wordlist File
  
## Installation and Running
```bash
git clone https://github.com/HBlackGhost/hashdead.git
cd /Downloads/hashdead
pip3 install -r requirements.txt
python3 hashdead.py -A  [md5,sha1,sha265  -HF  [The Path of Hash File] -W  [The Path Of Wordlist File]
```
