#base64异或
import base64

s='TkVLTFdUQVpvUlNda1ZXRUpAZVldTltgJCQhLCAgGSknPjc='
s=base64.b64decode(s)
for i in range(256):
	flag=""
	k=0
	for j in s:
		res=j^(k+i)
		flag+=chr(res)
		k+=1
	print(i,flag)
