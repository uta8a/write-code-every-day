from __future__ import annotations
from dataclasses import dataclass
import json
import dataclasses as dc

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


