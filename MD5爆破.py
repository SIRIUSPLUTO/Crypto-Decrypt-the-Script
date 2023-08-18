import string
import hashlib
dic = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_}{'
for i in dic:
    for j in dic:
        for k in dic:
            for l in dic:
              s = 'LitCTF{md5can'+i+j+'3de'+k+'rypt213thoughcr'+l+'sh}'
              print(s)
              if hashlib.md5(s.encode('utf-8')).hexdigest() == '496603d6953a15846cd7cc476f146771':
                 print("Find it: "+s)
                 exit(0)