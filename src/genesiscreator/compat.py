def hexencode(str) -> str:
    return str.encode().hex()

def hexdecode(hex_str) -> bytes:
    return bytes.fromhex(hex_str)