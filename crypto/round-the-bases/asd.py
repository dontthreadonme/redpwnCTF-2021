
flag_scr = open("round-the-bases2", "r").read().split()

"""
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D # 1
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D # 0

chr(0b01100110) = > "f"
"""

flag = ""
byte = ""
i = 0
for bit in flag_scr:
    if i % 8 == 0:
        if byte:
            flag += chr(int(byte, 2))
        byte = "0b"
    if "IIcu9mTN" in bit:
        byte += "0"
    if "K0o09mTN" in bit:
        byte += "1"
    i += 1


print("".join(flag))
