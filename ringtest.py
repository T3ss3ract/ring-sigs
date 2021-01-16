from linkable_ring_signature import ring_signature, verify_ring_signature

from ecdsa.util import randrange
from ecdsa.curves import SECP256k1

def pr2():
    print("======================")

def generate_ring_sig_default(message):
    number_participants = 10
    x = [randrange(SECP256k1.order) for i in range(number_participants)]
    i = 2
    y = list(map(lambda xi: SECP256k1.generator * xi, x))
    signature = ring_signature(x[i], i, message, y)
    try:
        assert verify_ring_signature(message, y, *signature)
    except AssertionError as e:
        print(e)
    return (message, y, signature)

number_participants = 10
x = [ randrange(SECP256k1.order) for i in range(0, number_participants)]
y = list(map(lambda xi: SECP256k1.generator * xi, x))
# message = "Every move we made was a kiss"

# i = 2
# signature = ring_signature(x[i], i, message, y)

# print(message)
# print("======")
# print(signature)
# print("======")
# print(verify_ring_signature(message, y, *signature))
# assert(verify_ring_signature(message, y, *signature))
print("===========")
print("===========")
print(generate_ring_sig_default("hello world"))
pr2()
print(generate_ring_sig_default("jakub balicki"))
pr2()
print(generate_ring_sig_default("you're a pube"))
pr2()
# assert verify_ring_signature(message, y, *signature)

class generic_message:
    def __init__(self, message):
        self.msg = message
        self.sig = generate_ring_sig_default(self.msg)

    def get_rsig(self):
        return self.sig

    def print_rsig(self):
        print(self.sig)

m = generic_message("what is the use of this")
t = generic_message("please help me")

# print(m.get_rsig())
# print(t.get_rsig())
xx = m.get_rsig()
yy = m.get_rsig()
zz = m.get_rsig()
print(verify_ring_signature(xx[0], xx[1], *xx[2]))
tt = t.get_rsig()
print(verify_ring_signature(tt[0], tt[1], *tt[2]))
