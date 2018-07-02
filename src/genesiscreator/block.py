import struct

from construct import Bytes
from construct import Struct

from genesiscreator.algorithms import ALGORITHMS
from genesiscreator.algorithms import hash_sha256d
from genesiscreator.algorithms import is_need_header_hash
from genesiscreator.transaction import create_genesis_transaction

BlockHeader = Struct('block_header',
                     Bytes('version', 4),
                     Bytes('hash_prev_bock', 32),
                     Bytes('hash_merkle_root', 32),
                     Bytes('time', 4),
                     Bytes('bits', 4),
                     Bytes('nonce', 4)
                     )


def create_block(pszTimestamp, pubkey, nValue, algorithm, nTime, nBits, nNonce, nVersion, test_mode=False):
    algorithm = algorithm.lower().strip()
    if algorithm not in ALGORITHMS:
        raise Exception('Invalid Algorithm Passed')

    block_data = {'pszTimestamp': pszTimestamp, 'pubkey': pubkey, 'nValue': nValue, 'algorithm': algorithm,
                  'nTime': nTime, 'nBits': nBits, 'nNonce': nNonce, 'nVersion': nVersion}

    # Create Coinbase Transaction
    tx = create_genesis_transaction(pszTimestamp, nValue, pubkey)

    # Calculate Merkle Root
    hash_merkle_root = hash_sha256d(tx)
    block_data['hashMerkleRoot'] = '0x' + hash_merkle_root[::-1].encode('hex_codec')

    # Construct block
    genesisblock = BlockHeader.parse('\x00' * 80)
    genesisblock.version = struct.pack('<I', nVersion)
    genesisblock.hash_prev_block = struct.pack('<qqqq', 0, 0, 0, 0)
    genesisblock.hash_merkle_root = hash_merkle_root
    genesisblock.time = struct.pack('<I', nTime)
    genesisblock.bits = struct.pack('<I', nBits)
    genesisblock.nonce = struct.pack('<I', nNonce)
    block = BlockHeader.build(genesisblock)

    # Hash Block
    target = (nBits & 0xffffff) * 2**(8 * ((nBits >> 24) - 3))

    # Edge case for testing
    if test_mode:
        sha256_hash = hash_sha256d(block)[::-1]
        header_hash = ALGORITHMS[algorithm](block)[::-1]
        if is_need_header_hash(algorithm):
            block_data['hashGenesisBlock'] = '0x' + header_hash.encode('hex_codec')
        else:
            block_data['hashGenesisBlock'] = '0x' + sha256_hash.encode('hex_codec')
        return block_data

    while True:
        sha256_hash = hash_sha256d(block)[::-1]
        header_hash = ALGORITHMS[algorithm](block)[::-1]

        if int(header_hash.encode('hex_codec'), 16) < target:
            block_data['nTime'] = nTime
            block_data['nNonce'] = nNonce
            if is_need_header_hash(algorithm):
                block_data['hashGenesisBlock'] = '0x' + header_hash.encode('hex_codec')
            else:
                block_data['hashGenesisBlock'] = '0x' + sha256_hash.encode('hex_codec')
            return block_data
        else:
            nNonce += 1
            if (nNonce > 4294967295):
                nTime += 1
                block = block[0:len(block) - 12] + struct.pack('<I', nTime)
            block = block[0:len(block) - 4] + struct.pack('<I', nNonce)
