# The flag is: flag{y0u_d4_qu33n_0f_cr4ck1ngz}

# Get the content of the two buffer used during the checks
magic0 = b'\x1b\x51\x17\x2a\x1e\x4e\x3d\x10\x17\x46\x49\x14\x3d'
magic1 = b'\xeb\x51\xb0\x13\x85\xb9\x1c\x87\xb8\x26\x8d\x07'
babuzz = "babuzz"

# Firs part of the flag that is checked
flag = 'flag{'

# This is the first check done by the executable
# It checks the content of character of the string from position len("flag{") to len("flag{")+12 against magic0
# And its aim is to find the correct printable character in range between 0 and 256 that pass the checks in the 
# given input position
for i in range(0,13):
    for c in range(256):
        if int(c) ^ ord(babuzz[i%6]) == magic0[i]:
            flag = flag + chr(c)
            break

# This is the second check done by the executable
# It checks the content of character of the string from position len("flag{")+13 to len("flag{")+25 against magic1
# As before it checks the condition against all the printable character
const = 187
for i in range(0,12):
    for c in range(256):
        temp = (const + c) % 256
        if temp == magic1[i]:
            const = temp
            flag = flag + chr(c)
            break

# Add to the obtained flag the closing character
flag = flag + "}"

# Finally print the obtained falg
print(flag)



# from IPython import embed;
# embed()