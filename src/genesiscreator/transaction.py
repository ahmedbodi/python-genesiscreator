"""File containing functions for the creation of transactions, input and output scripts."""
import struct

from construct import Byte
from construct import Bytes
from construct import StaticField
from construct import Struct
from construct import UBInt32


def create_input_script(psz_timestamp):
    """Using a timestamp string create the input script."""
    psz_prefix = ''
    # use OP_PUSHDATA1 if required
    if len(psz_timestamp) > 76:
        psz_prefix = '4c'

    script_prefix = '04ffff001d0104' + psz_prefix + chr(len(psz_timestamp)).encode('hex')
    return (script_prefix + psz_timestamp.encode('hex')).decode('hex')


def create_output_script(pubkey):
    """Create an output script for paying to a pubkey from coinbase."""
    script_len = '41'
    OP_CHECKSIG = 'ac'
    return (script_len + pubkey + OP_CHECKSIG).decode('hex')


def create_genesis_transaction(psz_timestamp, coinbase_value, pubkey):
    """Create the genesis transaction from the details passed."""
    input_script = create_input_script(psz_timestamp)
    output_script = create_output_script(pubkey)

    transaction = Struct('transaction',
                         Bytes('version', 4),
                         Byte('num_inputs'),
                         StaticField('prev_output', 32),
                         UBInt32('prev_out_idx'),
                         Byte('input_script_len'),
                         Bytes('input_script', len(input_script)),
                         UBInt32('sequence'),
                         Byte('num_outputs'),
                         Bytes('out_value', 8),
                         Byte('output_script_len'),
                         Bytes('output_script', 0x43),
                         UBInt32('locktime'))

    tx = transaction.parse('\x00' * (127 + len(input_script)))
    tx.version = struct.pack('<I', 1)
    tx.num_inputs = 1
    tx.prev_output = struct.pack('<qqqq', 0, 0, 0, 0)
    tx.prev_out_idx = 0xFFFFFFFF
    tx.input_script_len = len(input_script)
    tx.input_script = input_script
    tx.sequence = 0xFFFFFFFF
    tx.num_outputs = 1
    tx.out_value = struct.pack('<q', coinbase_value)
    tx.output_script_len = 0x43
    tx.output_script = output_script
    tx.locktime = 0
    return transaction.build(tx)
