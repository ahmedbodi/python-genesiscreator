# -*- coding: utf-8 -*-
"""Tests for Genesis Blocks for various coins."""
from genesiscreator.cli import main

def test_sha256_bitcoin_cli():
    """Test Bitcoin Genesis Block."""
    block_data = main()
    assert block_data['hashGenesisBlock'] == '0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    assert block_data['hashMerkleRoot'] == '0x4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
    assert block_data['nNonce'] == 2083236893
    assert block_data['nTime'] == 1231006505


