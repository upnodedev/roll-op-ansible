#!/usr/bin/env python3

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
import sys
import json

# Generate english mnemonic words
mnemonicLanguage="english"
mnemonicText = ""
if len(sys.argv) >= 3:
    mnemonicLanguage = sys.argv[2]
if len(sys.argv) >= 2:
    mnemonicText = sys.argv[1]
else:
    mnemonicText = generate_mnemonic(language=mnemonicLanguage, strength=128)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # "meherett"

# Initialize Ethereum mainnet BIP44HDWallet
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
# Get Ethereum BIP44HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(
    mnemonic=mnemonicText, language=mnemonicLanguage, passphrase=PASSPHRASE
)
# Clean default BIP44 derivation indexes/paths
bip44_hdwallet.clean_derivation()

bip44_derivation_admin: BIP44Derivation = BIP44Derivation(
    cryptocurrency=EthereumMainnet, account=0, change=False, address=0
)
bip44_hdwallet.from_path(path=bip44_derivation_admin)
adminAccount = bip44_hdwallet.address()
adminKey = f"0x{bip44_hdwallet.private_key()}"
bip44_hdwallet.clean_derivation()

bip44_derivation_admin: BIP44Derivation = BIP44Derivation(
    cryptocurrency=EthereumMainnet, account=0, change=False, address=0
)
bip44_hdwallet.from_path(path=bip44_derivation_admin)
batcherAccount = bip44_hdwallet.address()
batcherKey = f"0x{bip44_hdwallet.private_key()}"
bip44_hdwallet.clean_derivation()

bip44_derivation_admin: BIP44Derivation = BIP44Derivation(
    cryptocurrency=EthereumMainnet, account=0, change=False, address=0
)
bip44_hdwallet.from_path(path=bip44_derivation_admin)
proposerAccount = bip44_hdwallet.address()
proposerKey = f"0x{bip44_hdwallet.private_key()}"
bip44_hdwallet.clean_derivation()

bip44_derivation_admin: BIP44Derivation = BIP44Derivation(
    cryptocurrency=EthereumMainnet, account=0, change=False, address=0
)
bip44_hdwallet.from_path(path=bip44_derivation_admin)
sequencerAccount = bip44_hdwallet.address()
sequencerKey = f"0x{bip44_hdwallet.private_key()}"
bip44_hdwallet.clean_derivation()

output = {
    "mnemonic" : bip44_hdwallet.mnemonic(),
    "adminAccount" : adminAccount,
    "adminKey" : adminKey,
    "batcherAccount" : batcherAccount,
    "batcherKey" : batcherKey,
    "proposerAccount" : proposerAccount,
    "proposerKey" : proposerKey,
    "sequencerAccount" : sequencerAccount,
    "sequencerKey" : sequencerKey
}

print(json.dumps(output))
