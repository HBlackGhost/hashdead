import sys
import time
from colorama import Fore
def we_working_g () :
    print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTRED_EX+" Okay "+Fore.LIGHTGREEN_EX+", We Working In Your Goal"+Fore.LIGHTBLUE_EX+" (Please Be Patient) ")
    time.sleep(2)
def one_line():
    time.sleep(2)
    print(Fore.LIGHTRED_EX+"[!]"+Fore.LIGHTGREEN_EX+f"{Fore.LIGHTRED_EX} hashdead{Fore.LIGHTGREEN_EX} Using Only Command-Line ")
    time.sleep(2)
    print (Fore.LIGHTRED_EX+"[!]"+Fore.LIGHTYELLOW_EX+" Try that : "+Fore.RESET+"python3 hashdead.py -h")  
    time.sleep(2)
def processing_comp():
    sys.stdout.write('\r')
    time.sleep(3)
    sys.stdout.write(Fore.LIGHTGREEN_EX+"[-] Processing complete           \n")
    sys.stdout.flush()
    time.sleep(3)
def not_found():
    print(Fore.LIGHTRED_EX+f"\n[!]{Fore.LIGHTYELLOW_EX} Failed To Found Your Hash {Fore.LIGHTCYAN_EX}Try With Another {Fore.LIGHTRED_EX}Wordlist")
def end () :
    print(Fore.LIGHTGREEN_EX+f"[-]"f" Thank you for {Fore.LIGHTBLUE_EX}using {Fore.LIGHTRED_EX}Rembil")
    print(Fore.LIGHTGREEN_EX+f"[-]"f"{Fore.LIGHTGREEN_EX} Created By {Fore.YELLOW}Black{Fore.WHITE} Ghost{Fore.LIGHTRED_EX} Hacker")
    