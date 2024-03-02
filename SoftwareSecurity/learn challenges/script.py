#!/usr/bin/env python3

# Importa la libreria di pwntool
import re
from pwn import *

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13003
    path = './sw-20'
    exe = ELF("./sw-20")
    
    dic = exe.sym

    print(dic)
    #time.sleep(5)

    r = remote(HOST, PORT)

    print(r.recvuntil(b"Invia un qualsiasi carattere per iniziare ...").decode())
    r.sendline(b"a")
    
    for function in dic:

        shellcode = asm(function)
        r.sendline(shellcode)

        r.interactive()


if __name__ == "__main__":
    main()
