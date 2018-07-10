"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mgenesiscreator` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``genesiscreator.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``genesiscreator.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import sys

from genesiscreator import constants
from genesiscreator.block import create_block

parser = argparse.ArgumentParser()
parser.add_argument('--nTime', dest='nTime', default=1231006505,
                    type=int, help='the (unix) time when the genesisblock is created')

parser.add_argument('--pszTimestamp', dest='pszTimestamp', default='The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',
                    type=str, help='the pszTimestamp message found in the coinbase of the genesisblock')

parser.add_argument('--nNonce', dest='nNonce', default=2083236893,
                    type=int, help='the first value of the nonce that will be incremented when searching the genesis hash')

parser.add_argument('--algorithm', dest='algorithm', default='SHA256',
                    type=str, choices=['SHA256', 'Scrypt', 'X11', 'X13', 'X15'], help='the PoW algorithm to use for the genesis block')

parser.add_argument('--pubkey', dest='pubkey',
                    default='04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35'
                    '504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f',
                    type=str, help='the pubkey found in the output script')

parser.add_argument('--nValue', dest='nValue', default=50 * constants.COIN,
                    type=int, help='the value in coins for the output, full value '
                    '(exp. in bitcoin 5000000000 - To get other coins value: Block Value * 100000000)')

parser.add_argument('--nBits', dest='nBits', default=0x1d00ffff,
                    type=lambda x: int(x, 0), help='the target in hex')

parser.add_argument('--nVersion', dest='nVersion', default=1,
                    type=int, help='The Block Version')


def main(argv=sys.argv):
    args = parser.parse_args()
    print(args)

    block_data = create_block(args.pszTimestamp, args.pubkey, args.nValue, args.algorithm,
                              args.nTime, args.nBits, args.nNonce, args.nVersion)

    print("""
        Algorithm: {algorithm}
        Hash Merkle Root: {hashMerkleRoot}
        pszTimestamp: {pszTimestamp}
        pubkey: {pubkey}
        nTime: {nTime}
        nBits: {nBits}
        nNonce: {nNonce}
        hashGenesisBlock: {hashGenesisBlock}
    """.format(**block_data))
    return block_data
