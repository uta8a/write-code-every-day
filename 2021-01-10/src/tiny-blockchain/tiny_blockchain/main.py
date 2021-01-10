from __future__ import annotations
from dataclasses import dataclass
import json
import dataclasses as dc
from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.Hash import SHA
from Cryptodome.PublicKey import RSA
import binascii

def decode_key(key):
  if isinstance(key, str):
    return key
  return binascii.hexlify(key.exportKey(format='DER')).decode('ascii')

def encode_key(key):
  if isinstance(key, object):
    return key
  return RSA.importKey(binascii.unhexlify(key))

@dataclass
class Transaction:
  sender_address: str
  receiver_address: str
  value: float
  sign: str = None

  def str_data(self) -> str:
    d = dc.asdict(self)
    del d["sign"]
    return json.dumps(d)

  def json_dumps(self) -> str:
    return json.dumps(dc.asdict(self))
  @classmethod
  def json_loads(cls, string) -> Transaction:
    return cls(**json.loads(string)) # ?


# AttributeError: 'PKCS115_Cipher' object has no attribute 'sign'
@dataclass
class Wallet:
  def __init__(self):
    key = RSA.generate(1024)
    self.private_key = decode_key(key)
    self.address = decode_key(key.publickey())

  def sign_transaction(self, transaction) -> Transaction:
    signer = PKCS1_v1_5.new(encode_key(self.private_key))
    h = SHA.new(transaction.str_data().encode())
    return dc.replace(transaction, sign=signer.sign(h).hex())
  
  def send(self, receiver_address, value) -> Transaction:
    transaction = Transaction(self.address, receiver_address, value)
    return self.sign_transaction(transaction)

def verify_transaction(transaction) -> bool:
  if transaction.sign is None:
    return False
  h = SHA.new(transaction.str_data().encode())
  verifier = PKCS1_v1_5.new(encode_key(transaction.sender_address))
  return verifier.verify(h, binascii.unhexlify(transaction.sign))

Ledger = list

alice = Wallet() # auto generated address
bob = Wallet()
ledger = Ledger()

transaction = alice.send(bob.address, 5) # alice -> bob `5` send
ledger.append(transaction)

# Ok
print("Verify: {}".format(verify_transaction(transaction)))

# NG
transaction.value = 7
print("Verify(Tamper): {}".format(verify_transaction(transaction)))
