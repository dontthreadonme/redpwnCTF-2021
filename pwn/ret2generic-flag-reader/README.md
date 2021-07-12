# ret2generic-flag-reader

The interesting function here that prints the flag is located at ``0x4011f6``. With ``gets()`` we get to write as much as we want, so we only have to fill the buffer of lenght 32 and write over the return address.
