import hashlib
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
result = b'\xe85.v\xe2`\xa3\x1e\xb2f\x01/p\xdf\x9a\x10'
with open("dictionary.txt","r") as list_file:
    pos_pw_list = list_file.readlines()
for password in pos_pw_list:
    if hash_pw(password.replace("\n","")) == result:
        print(password)
        break