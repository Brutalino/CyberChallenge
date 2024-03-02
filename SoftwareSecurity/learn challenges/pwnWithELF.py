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
    PORT = 13002
    path = './sw-19'
    exe = ELF("./sw-19")
    
    dic = exe.sym

    print(dic)
    #time.sleep(5)

    r = remote(HOST, PORT)

    print(r.recvuntil(b"Invia un qualsiasi carattere per iniziare ...").decode())
    r.sendline(b"a")

    for i in range(1,21):
        
        prompt = r.recvuntil(b":").decode()
        #print(prompt)

        if(i>1):
            print("Correct address. Continuing")
        
        match = re.search(r"> ([^:]+):", prompt)

        print(prompt)
 
        if match:
            function = match.group(1)
        else:
            ("nuessuna corrispondenza trovata")
        # Stampa i valori estratti

        address = hex(dic[function])
        #print(type(address))
        print(f"Function: {function}")

        print(f"Function Address: {address}")

        print("Sending ", address)

        r.sendline(address)

    r.interactive()

if __name__ == "__main__":
    main()
