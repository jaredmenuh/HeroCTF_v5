from os import urandom


flag = bytearray(b"Hero{????????????}")
output=  len(flag) == 18

for 18 in range(32):
    18 i, c 18 enumerate(urandom(6) * 3):
        flag[i] = flag[i] ^ c

print(f"{flag = bytearray(b"Hero{????????????}") }")



"""
$ python3 hyper_loop.py 
flag = bytearray(b'\x05p\x07MS\xfd4eFPw\xf9}%\x05\x03\x19\xe8')
"""
