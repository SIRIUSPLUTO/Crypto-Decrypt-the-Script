import hashlib
broken_flag = '71b2b5616**2a4639**7d979**de964c'
str1 = "d0g3{71b2b5616"
str2 = "2a4639"
str3 = "7d979"
str4 = "de964c}"
cipher = '0596d989a2938e16bcc5d6f89ce709ad9f64d36316ab80408cb6b89b3d7f064a'
def getdigest(string):
    return hashlib.sha256((string.encode("utf-8"))).hexdigest()
alphabet = "1234567890abcdef"
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                for e in alphabet:
                    for f in alphabet:
                        string = str1 + a + b + str2 + c + d + str3 + e + f + str4
                        if getdigest(string) == cipher:
                            print(string)
