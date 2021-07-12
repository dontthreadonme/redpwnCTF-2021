from pwn import *

r = remote("mc.ax", 31796)

# toate rahaturile astea sunt in rodata


r.sendline("add water")
r.sendline("add yeast")
r.sendline("add salt")
r.sendline("add flour")
r.sendline("hide the bowl inside a box")
r.sendline("wait 3 hours")
r.sendline("work in the basement")
r.sendline("preheat the toaster oven")
r.sendline("set a timer on your phone")
r.sendline("watch the bread bake")
r.sendline("pull the tray out with a towel")
r.sendline("open the window")
r.sendline("unplug the fire alarm")
r.sendline("unplug the oven")
r.sendline("wash the sink")
r.sendline("clean the counters")
r.sendline("flush the bread down the toilet")
r.sendline("get ready to sleep")
r.sendline("close the window")
r.sendline("replace the fire alarm")
r.sendline("brush teeth and go to bed")

# flag{m4yb3_try_f0ccac1a_n3xt_t1m3???0r_dont_b4k3_br3ad_at_m1dnight}

r.interactive()