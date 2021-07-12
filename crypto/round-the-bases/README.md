# round-the-bases

I recognised the repeating string `9mTfc:..Zt9mTZ_:` so I used a text editor to insert a new line at the begining of each occurance.
Then the only variation between the strings became clear, as there were 264 occurances (264/8 = 33.0) ((8 bits for a char)) I assumed its just some binary representation. 
```
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0
```
I wrote a script which decoded every 8 bits and added them to a flag which I printed at the end.
