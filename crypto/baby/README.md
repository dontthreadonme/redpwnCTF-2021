# baby

In this challenge we are given three numbers, an n, e and c, which I recognised as pieces of RSA. 
```n = 228430203128652625114739053365339856393
e = 65537
c = 126721104148692049427127809839057445790```

The n was small enough to factor using wolfram alpha into two prime numbers.
```12546190522253739887×18207136478875858439 (2 distinct prime factors)```

I then calculated the tottient to find the d which I used to decrypt the cypthertext.
