#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"a")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    # r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"something", b"Ciao!")

    # solo dopo che viene ricevuta la stringa "something"
    #r.sendlineafter(b"something", b"Ciao!")

    # .recv() riceve e ritorna al massimo 1024 bytes dalla socket
    # data = r.recv(1024)

    # .recvline() legge dalla socket fino ad un newline
    #data = r.recvline()

    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"
    # data = r.recvuntil(b"something")

    # permette di interagire con la connessione direttamente dalla shell
    #r.interactive()

    r.recvuntil(b"Invia un qualsiasi carattere per iniziare ...")

    r.sendline(b"a")

    # chiude la socket
    #r.close()
    for i in range(1,11):


        r.recvuntil(b"[")
        operation = r.recv(1)

        if(operation == b"+"):
            r.recvuntil(b"somma questi numeri")
            r.recv(2)
            numbers = r.recvuntil(b"]", drop=True).split(b", ")
            numbers = [int(number.decode()) for number in numbers]

            sum = 0
            for number in numbers:
                sum += number
                
            r.sendline(str(sum).encode())

    
    r.interactive()

if __name__ == "__main__":
    main()
