# -*- coding: utf-8 -*-
"""Tests for Genesis Blocks for various coins."""

from genesiscreator.block import create_block
from genesiscreator.constants import COIN


def test_sha256_bitcoin():
    """Test Bitcoin Genesis Block."""
    block_data = create_block(
        'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',
        '04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f',
        50 *
        COIN,
        'SHA256',
        1231006505,
        0x1d00ffff,
        2083236893,
        1,
        True)
    assert block_data['hashGenesisBlock'] == '0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    assert block_data['hashMerkleRoot'] == '0x4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
    assert block_data['nNonce'] == 2083236893
    assert block_data['nTime'] == 1231006505


def test_scrypt_litecoin():
    """Test Litecoin Genesis Block."""
    block_data = create_block(
        'NY Times 05/Oct/2011 Steve Jobs, Apple’s Visionary, Dies at 56',
        '040184710fa689ad5023690c80f3a49c8f13f8d45b8c857fbcbc8bc4a8e4d3eb4b10f4d4604fa08dce601aaf0f470216fe1b51850b4acf21b179c45070ac7b03a9',
        50 *
        COIN,
        'Scrypt',
        1317972665,
        0x1e0ffff0,
        2084524493,
        1,
        True)
    assert block_data['hashMerkleRoot'] == '0x97ddfbbae6be97fd6cdf3e7ca13232a3afff2353e29badfab7f73011edd4ced9'
    assert block_data['nNonce'] == 2084524493
    assert block_data['nTime'] == 1317972665
    assert block_data['hashGenesisBlock'] == '0x12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2'


def test_x11_dash():
    """Test Dash Genesis Block."""
    block_data = create_block(
        'Wired 09/Jan/2014 The Grand Experiment Goes Live: Overstock.com Is Now Accepting Bitcoins',
        '040184710fa689ad5023690c80f3a49c8f13f8d45b8c857fbcbc8bc4a8e4d3eb4b10f4d4604fa08dce601aaf0f470216fe1b51850b4acf21b179c45070ac7b03a9',
        50 *
        COIN,
        'X11',
        1390095618,
        0x1e0ffff0,
        28917698,
        1,
        True)
    assert block_data['hashMerkleRoot'] == '0xe0028eb9648db56b1ac77cf090b99048a8007e2bb64b68f092c03c7f56a662c7'
    assert block_data['nNonce'] == 28917698
    assert block_data['nTime'] == 1390095618
    assert block_data['hashGenesisBlock'] == '0x00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6'


def test_quark_pivx():
    """Test PIVX Genesis Block."""
    block_data = create_block(
        'U.S. News & World Report Jan 28 2016 With His Absence, Trump Dominates Another Debate',
        '04c10e83b2703ccf322f7dbd62dd5855ac7c10bd055814ce121ba32607d573b8810c02c0582aed05b4deb9c4b77b26d92428c61256cd42774babea0a073b2ed0c9',
        250 *
        COIN,
        'Quark',
        1454124731,
        0x1e0ffff0,
        2402015,
        1,
        True)
    assert block_data['hashMerkleRoot'] == '0x1b2ef6e2f28be914103a277377ae7729dcd125dfeb8bf97bd5964ba72b6dc39b'
    assert block_data['nNonce'] == 2402015
    assert block_data['nTime'] == 1454124731
    assert block_data['hashGenesisBlock'] == '0x0000041e482b9b9691d98eefb48473405c0b8ec31b76df3797c74a78680ef818'
