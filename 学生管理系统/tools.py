import hashlib


# 在加密的基础上再加密
def encrypt_password(passwd, x='lsdajflkd'):
    h = hashlib.sha256()
    h.update(passwd.encode('utf8'))
    h.update(x.encode('utf8'))
    return h.hexdigest()


# print(encrypt_password('1234455'))
