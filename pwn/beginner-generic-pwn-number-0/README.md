# beginner-generic-pwn-number-0

We are reading as many bytes as we want (due to gets) into a 32 byte long buffer located at ``rsp``. We just need to overwrite a variable located at ``rsp+0x28`` to be equal to -1.
