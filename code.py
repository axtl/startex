from random import choice
from string import hexdigits

def randbits(bitlen):
    return ''.join(choice(hexdigits)\
        for i in xrange(bitlen))
