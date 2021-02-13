# The flag is: flag{y0u_d4_qu33n_0f_cr4ck1ngz}


magic0 = b'\x1b\x51\x17\x2a\x1e\x4e\x3d\x10\x17\x46\x49\x14\x3d'
magic1 = b'\xeb\x51\xb0\x13\x85\xb9\x1c\x87\xb8\x26\x8d\x07'
babuzz = "babuzz"


flag = 'flag{'

for i in range(0,13):
    for c in range(256):
        if int(c) ^ ord(babuzz[i%6]) == magic0[i]:
            flag = flag + chr(c)
            break

const = 187
# from IPython import embed;
# embed()
for i in range(0,12):
    for c in range(256):
        temp = (const + c) % 256
        if temp == magic1[i]:
            const = temp
            flag = flag + chr(c)
            break

flag = flag + "}"

print(flag)



# from IPython import embed;
# embed()