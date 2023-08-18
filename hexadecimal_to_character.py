#十六进制转字符串
import re
a ='61666374667B317327745F73305F333435797D'
b = re.findall(r'.{2}',a)
flag = ''
for i in b:
	flag += chr(int(i,16))
print(flag)
