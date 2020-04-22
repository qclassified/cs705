"""
Assignment 1
CS 705 Cryptography and Blockchain
Spring 2020
Department of Computer Science and Engineering
University of Nevada, Reno

Student Name: Farhan Sadique
"""

import random
from hashlib import sha256
from datetime import datetime as dt


def sha40(data):  # sha40 (40 bits) is sufficient for this example
  return sha256(data.encode('utf-8')).hexdigest()[:10]


class User:  
  def __init__(self, name):
    self.name = name              # User identity = name

  def __str__(self):
    return self.name


class Miner(User):                # Miners can also be users (send coin)
  def __init__(self, name, cpu):
    assert type(cpu) == int, "Miner cpu power must be integer"
    self.cpu = cpu                # cpu power of miner (integer > 1)
    super().__init__(name)

  def __str__(self):
    return '{} (CPU Power = {})'.format(self.name, self.cpu)
  

class Transaction: 
  def __init__(self, _from, to, val):
    self._from = _from            # sender
    self.to = to                  # recipient
    self.val = val                # amount of coins sent
    self.hash = sha40(str(self))  # transaction hash needed for merkle root

  def __str__(self):              # print format = 'Sender -> Recipient: amount'
    return '{} -> {}: {:.2f}'.format(self._from.name, self.to.name, self.val)


class Block:  
  difficulty = 0x00FFFFFFFF                 # default mining difficulty
  
  def __init__(self, transactions=['genesis'], prev_block=None):
    self.time = str(dt.now())
    self.transactions = transactions
    self.nonce = 0
    
    if transactions == ['genesis']:         # create genesis block
      self.miner, self.index = 'genesis', 0 # genesis block parameters
      self.prev_hash, self.merkle_root = '0000000000', 'aeebad4a79'
      return 

    self.index = prev_block.index + 1       # this block index = previous index + 1
    self.prev_hash = prev_block.hash        # hash of previous block
    self.merkle_tree = []                   # store entire merkle tree for verifiability
    self.merkle_root = self.get_merkle_root([t.hash for t in transactions])

  @property
  def hash(self):                           # gets hash of this block
    return sha40(self.merkle_root + self.prev_hash + str(self.nonce) + self.time)

  def get_merkle_root(self, hash_list):     # merkle root of transaction hashes
    self.merkle_tree += hash_list           # update merkle tree of block
    if len(hash_list) == 1: return hash_list[0]
    new_hash_list = []
    for i in range(0, len(hash_list)-1, 2):
        new_hash_list.append(sha40(hash_list[i] + hash_list[i+1]))
    if len(hash_list) % 2 == 1: # odd, hash last item twice
        new_hash_list.append(sha40(hash_list[-1] + hash_list[-1]))
    return self.get_merkle_root(new_hash_list)

  def mine(self, miner):                    # mine block to `show PoW = get Nonce'
    while int(self.hash, 16) >= self.difficulty: self.nonce += 1
    self.miner = miner                      # miner who mined this block

  def __str__(self):                        # print block info in a nice manner
    return '''Block # {}, Time: {}, Nonce: {}, Miner: {}
Hash: {}, Previous hash: {}, Merkle root: {},\n{} Transactions: {}'''\
      .format(self.index, self.time, self.nonce, str(self.miner),
          self.hash, self.prev_hash, self.merkle_root,
          len(self.transactions), [str(t) for t in self.transactions])
      

### =====================================================================
### ========================== SIMULATION ===============================
### =====================================================================
  
transactions_queue = []               # global queue for requested transactions
miners_cpu = []                       # more cpu means more occurrence in this list 
blockchain = []                       # global list for entire blockchain
Block.difficulty = 0x000FFFFFFF       # mining (PoW) difficulty, smaller = more work

### =============== Create Users ===============

Alice = User('Alice')                 
Bob = User('Bob')
Charlie = User('Charlie')
Eve = User('Eve')

Users = [Alice, Bob, Charlie, Eve]


### =============== Create Miners ===============

Oscar = Miner('Oscar', 1)             # Oscar has cpu power = 1  
Trudy = Miner('Trudy', 2)             # Trudy has cpu power = 2
Victor = Miner('Victor', 3)           # ... and so on
Wendy = Miner('Wendy', 4)

miners = [Oscar, Trudy, Victor, Wendy]


### =============== Modify miners by CPU Power ===============

for m in miners: miners_cpu += [m]*m.cpu


### =============== Generate Random Transactions and Print =============

num_transactions = random.randint(1, 15)      # Random number of transactions 1 to 15

for i in range(num_transactions):
  sender, receiver = random.sample(Users, 2)  # Random sender, receiver
  amount = random.uniform(0.0, 100.0)         # Random amount in [0, 100]
  t = Transaction(sender, receiver, amount)   # create transactions
  transactions_queue.insert(0, t)


print("\n{} Transactions Requested:\n(Sender -> Receiver: Amount)"
      .format(num_transactions))
for t in transactions_queue[::-1]:
  print(t)


### =============== Create Genesis Block ===============

genesis = Block()
blockchain.append(genesis)                    # Include genesis block in blockchain


### =============== Mine Transactions into Blocks ===============

while transactions_queue:
  miner = random.choice(miners_cpu)           # Miner with more cpu is more probable
  remaining = len(transactions_queue)         # remaining # of transactions in queue
  n = random.randint(1, remaining)            # number of transactions in this block

  t = []                                      # transactions in this block
  for i in range(n):
    t.append(transactions_queue.pop())

  block = Block(t, blockchain[-1])            # create block with transactions
  block.mine(miner)                           # mine block to show PoW
  blockchain.append(block)                    # include block in blockchain

    
### =============== Print Entire Blockchain ===============
  
print('\n-------------------------------------\n{} transactions mined into {} blocks'
      .format(num_transactions, len(blockchain)-1))

for b in blockchain:
  print('-------------------------------------')
  print(b)




