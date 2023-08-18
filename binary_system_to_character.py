#二进制转字符串
import re
a ='你的二进制串'
b = re.findall(r'.{8}',a)
flag = ''
for i in b:
	flag += chr(int(i,2))
print(flag)
