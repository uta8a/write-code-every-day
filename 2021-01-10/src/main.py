from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Transaction:
  sender_address: int
  receiver_address: int
  value: float

@dataclass
class Wallet:
  address: int
  def send(self, receiver_address, value):
    return Transaction(self.address, receiver_address, value)

Ledger = list

alice = Wallet(1) # address 1
bob = Wallet(2) # address 2
ledger = Ledger()

transaction = alice.send(bob.address, 5) # alice -> bob `5` send
ledger.append(transaction)


