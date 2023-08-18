# 仿射密码
z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
     'U', 'V', 'W', 'X', 'Y', 'Z']


# 通过列表来表示Z整数环中的52个元素
def exgcd(a, b, arr):  # 通过拓展欧几里得定理来求a对于整数环中的逆元
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    r = exgcd(b, a % b, arr)
    tmp = arr[0]
    arr[0] = arr[1]
    arr[1] = tmp - int(a / b) * arr[1]
    return r


def Get_ei(a, b):
    arr = [0, 1, ]
    r = exgcd(a, b, arr)
    if r == 1:
        return int((arr[0] % b + b) % b)
    else:
        return -1


def encrypt(k1, k2, message):  # 加密过程
    a = str(message)
    t = ""

    for i in a:

        if i in z:

            c = z.index(i)
            Y = (k1 * c + k2) % 52
            t += z[Y]
        else:
            t += i
    return t
    # print(ord(i))


# *************begin************#

# **************end*************#

def decrypt(k1, k2, message):  # 解密过程
    k1_ = Get_ei(k1, 52)
    t = ""
    a = str(message)
    for i in a:
        if i in z:
            c = z.index(i)
            X = (k1_ * (c - k2)) % 52
            t += z[X]
        else:
            t += i
    return t


def main():
    mode = int(input())  # 1代表加密，0代表解密
    message = input()  # 待加密或解密的消息
    key1 = int(input())  # key的范围0~51之间
    key2 = int(input())  # key的范围0~51之间
    if mode == 1:
        translated = encrypt(key1, key2, message)
    else:
        translated = decrypt(key1, key2, message)
    print(translated)


if __name__ == '__main__':
    main()
