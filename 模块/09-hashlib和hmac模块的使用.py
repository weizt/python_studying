import hashlib
import hmac

# 这两个模块都是用来加密的
# hashlib 模块里主要支持两个算法 md5 和 sha 加密
# 加密方式：
'''
1.单向加密：只有加密的过程，不能解密 md5/sha
2.对称加密
3.非对称加密 rsa
'''
# MD5加密，需要将加密的内容转换成二进制
x = hashlib.md5()  # 生成一个md5对象
x.update('abc'.encode('utf8'))
print(x.hexdigest())
# 'abc' ==> 900150983cd24fb0d6963f7d28e17f72

# sha加密
H1 = hashlib.sha1('12345'.encode())
print(H1.hexdigest())
H2 = hashlib.sha224('12345'.encode())  # 指224位二进制位数，一个16进制占4位
print(H2.hexdigest())
H3 = hashlib.sha256('12345'.encode())
print(H3.hexdigest())
H4 = hashlib.sha384('12345'.encode())
print(H4.hexdigest())

# hmac加密，可以指定秘钥
h = hmac.new('h'.encode(), '你好'.encode())  # 指定’你好‘为密文，’h‘为密钥，并转换成二进制
result = h.hexdigest()  # 转换密文为16进制
print(result)
