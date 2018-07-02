import hashlib

NEEDS_HEADER_HASH = [
    'x11',
    'x13',
    'x15',
    'quark',
]


def is_need_header_hash(algorithm):
    if algorithm in NEEDS_HEADER_HASH:
        return True
    return False


def hash_sha256d(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def hash_scrypt(data):
    import scrypt
    return scrypt.hash(data, data, 1024, 1, 1, 32)


def hash_x11(data):
    import x11_hash
    return x11_hash.getPoWHash(data)


def hash_x13(data):
    import x13_hash
    return x13_hash.getPoWHash(data)


def hash_x15(data):
    import x15_hash
    return x15_hash.getPoWHash(data)


def hash_quark(data):
    import quark_hash
    return quark_hash.getPoWHash(data)


ALGORITHMS = {
    'sha256': hash_sha256d,
    'scrypt': hash_scrypt,
    'x11': hash_x11,
    'x13': hash_x13,
    'x15': hash_x15,
    'quark': hash_quark,
}
