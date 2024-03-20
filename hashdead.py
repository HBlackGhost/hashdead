#! /usr/bin/python3
import hashlib
import argparse
import sys
import subprocess
from colorama import Fore
from modules import menues, banner
sys.stdout.write("\033[H\033[J")
banner.banner()
praser = argparse.ArgumentParser(description=Fore.LIGHTGREEN_EX+"hashdead script cracks hashes by comparing hashes generated from a wordlist with a provided hash file. It supports MD5, SHA-1, and SHA-256 algorithms"+Fore.LIGHTYELLOW_EX)
praser.add_argument('-A' ,dest="ALGORITHM" ,help="Your Hash Algorithm",choices=["md5","sha1",'sha256'])
praser.add_argument('-HF' ,dest="HASH_FILE" ,help="Your Hash File That You Want To Crack ")
praser.add_argument('-W' ,dest="WORDLIST" ,help="Your Wordlist File")
praser.add_argument('-U' ,dest="UP" ,help="The Path Of hashdead")
args = praser.parse_args()
if args.UP != None :
    com= subprocess.run(f'sudo {args.UP}/updating_tool.sh',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
    print(Fore.LIGHTGREEN_EX,"[-]",Fore.LIGHTGREEN_EX,"[-]",com.stdout,com.stderr)
    exit()
elif args.UP == None :
    if args.ALGORITHM != None and args.HASH_FILE != None and args.WORDLIST != None :
        try:
            with open(args.WORDLIST, 'r',encoding='latin-1') as file:
                with open(args.HASH_FILE, 'r',encoding='latin-1') as f:
                    x=f.read().strip()
                    processed_lines = 0
                    total_lines = sum(1 for line in open(args.WORDLIST, 'r', encoding='latin-1'))
                    menues.we_working_g()
                    for line in file:
                        hash_object = hashlib.new(args.ALGORITHM)
                        hash_object.update(line.strip().encode())
                        hash_chiper = hash_object.hexdigest()
                        processed_lines += 1
                        progress = int((processed_lines / total_lines) * 100)
                        sys.stdout.write('\r')
                        sys.stdout.write(f"{Fore.LIGHTGREEN_EX}[-] {Fore.LIGHTRED_EX}Processing... "+Fore.LIGHTBLUE_EX+"{}%".format(progress) )
                        sys.stdout.flush()
                        if x == hash_object.hexdigest() :
                            word =line.strip()
                            s= True
                            break      
                        else:
                            s= False
                    if s == True:
                        print(Fore.LIGHTGREEN_EX+f"\n[-]{Fore.LIGHTYELLOW_EX} We Found Your Hash {Fore.WHITE}--> ",Fore.LIGHTRED_EX+word)
                    else:
                        menues.not_found()
                menues.processing_comp()
                menues.end()
        except KeyboardInterrupt :
           print("");menues.end()
    else :
        menues.one_line()   
        menues.end()


