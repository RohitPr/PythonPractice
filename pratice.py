import basehash

a = "ROHIT"
b = hash(1)

hash_fn = basehash.base36()

print(b)
unhashed = hash_fn.unhash('M8YZRZ')

print(unhashed)
