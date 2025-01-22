import hashlib
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
result = b'\x16\x02m`\xff\x9bTA\x0b45\xb4\x03\xaf\xd2&'
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

for password in pos_pw_list:
    if hash_pw(password) == result:
        print(password)
        break