import pyfiglet
from colorama import Fore
def banner() :
    text_1 ="H A S H D E A D "
    text_2=pyfiglet.figlet_format(text_1 )
    print(Fore.RED+text_2,end="")
