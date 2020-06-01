from ctypes import string_at
from sys import getsizeof
from binascii import hexlify
a = 2333
print(hexlify(string_at(0x0643A498,getsizeof(a))))

