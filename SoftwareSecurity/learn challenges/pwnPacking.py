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
    PORT = 13001
    r = remote(HOST, PORT)

    r.recvuntil(b"Invia un qualsiasi carattere per iniziare ...")

    r.sendline(b"a")

    # chiude la socket
    #r.close()
    for i in range(1,101):
        

        prompt = r.recvuntil(b"\n").decode()

        if(i>1):
            print("Correct result. Continuing")
        # Extract address and format
        # Estrai l'indirizzo usando un'espressione regolare
        match = re.search(r"0x([0-9a-fA-F]+) packed a (\d+)-bit", prompt)

        while not match:
            print("cerco il prompt corretto")
            prompt = r.recvuntil(b"\n").decode()
            match = re.search(r"0x([0-9a-fA-F]+) packed a (\d+)-bit", prompt)
        print(prompt)
 
        if match:

            # Assegna l'indirizzo alla variabile "address"
            address = int(match.group(1), 16)
            # Assegna il formato alla variabile "format"
            format = int(match.group(2))
        else:
            ("nuessuna corrispondenza trovata")
        # Stampa i valori estratti
        print(f"Indirizzo: {hex(address)}")
        print(f"Formato: {format}")
        
        print(address)
        if (format == 64):
            print("packing a 64-bit")
            packedAddress = p64(address)
        else:
            print("packing a 32-bit")
            packedAddress = p32(address)

        print("sending ", packedAddress)

        r.send(packedAddress)
    
    r.interactive()

if __name__ == "__main__":
    main()
