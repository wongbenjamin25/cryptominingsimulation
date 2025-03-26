"""
Primary Owner: Dr. Chen and Dr. Wang for DSE4211 2025
Description: Homework 2 practicing hash, mining and adjusting mining difficulty

- **Wong Hao Xue Benjamin**:
- **E0968961**:
"""

from datetime import datetime
import hashlib

class HashMethod:
    '''Hashes an input string using sha2 or sha3 256 method'''
    def __init__(self, userhashmethod):
        self.hashmethod = userhashmethod

    def ciphertext(self, inputstring):
        '''hashing user input text string to a transformed text message'''
        if self.hashmethod == 'hash256_sha2':
            return hashlib.sha256(inputstring.encode('utf-8')).hexdigest()
        elif self.hashmethod == 'hash256_sha3':
            return hashlib.sha3_256(inputstring.encode('utf-8')).hexdigest()
        elif self.hashmethod == 'hash256_shake':
            return hashlib.shake_256(inputstring.encode('utf-8')).hexdigest(32)
        else:
            raise ValueError('The userhashmethod {} is not one of the three hash 256 method'.format(self.hashmethod))

class TransactionGenerator:
    '''Generates testing transactions'''
    def __init__(self, hmethod):
        self.randomseed = 0
        self.hmethod = hmethod

    def generatetransaction(self):
        '''Generates random transaction for tests'''
        transaction = "Transaction between A and B. Add a random seed {} to make hash unique".format(self.randomseed)
        transactionhash = self.hmethod.ciphertext(transaction)
        self.randomseed += 1
        return transactionhash


class Block:
    '''Builts a unit of Block with previous hash, nonce, transaction data and current hash'''
    def __init__(self, hashprevblock, target, hmethod):
        self.transactions = []
        self.hashprevblock = hashprevblock
        self.hashmerkleblock = None
        self.target = target
        self.nonce = 0
        self.hmethod = hmethod

    def addtransaction(self, transactionnew):
        '''Adds new transaction data'''
        if not self.is_blockfull():
            self.transactions.append(transactionnew)
            self.hashmerkleblock = self.hmethod.ciphertext(str('-'.join(self.transactions)))

    def is_blockfull(self):
        '''Limits the size of a Block 1megabyte, e.g. 4000 transaction'''
        return len(self.transactions) >= 4000
    
    def is_blockreadytomine(self):
        '''Ready to mine if the block is full'''
        return self.is_blockfull()
    
    def __str__(self):
        return '-'.join([self.hashmerkleblock, str(self.nonce)])

    def applymining(self):
        '''Finds the nonce that meets the hashing Target and creates a timestamp'''
        hashcurrblock = self.hmethod.ciphertext(self.__str__())
        print("CURRENT BLOCK HASH = {}, TARGET = {}".format(hashcurrblock, self.target))
        if int(hashcurrblock, 16) < int(self.target, 16):
            timestamp = datetime.now()
            print(timestamp)
            print("Block was mined successfully with a reward of 3.125 BTC")
            print("It took {} steps to mine it".format(self.nonce))
            return True
        else:
            self.nonce += 1 
        return False
    

class BlockChain:
    '''Builts a chain of Blocks'''
    def __init__(self):
        self.blockchain = []

    def push(self, block):
        '''Adds blocks'''
        self.blockchain.append(block)

    def getlastblock(self):
        '''Gets the last added Block in the chain'''
        return self.blockchain[-1]

    def notify(self):
        '''Broadcasting the length and last block information'''
        mtime = datetime.now()
        utcmtime = datetime.timestamp(mtime)
        print("This new block has been added: {}".format(mtime))
        print("Timestamp in unix time format: {}".format(utcmtime))
        print("[block #{}]:{}".format(len(self.blockchain), self.getlastblock()))

def adjust_difficulty(mtimer, currblocktarget):
    '''Dynamically adjusts mining difficulty to ensure blocks take around 10 seconds'''
    if mtimer.total_seconds() < 10:
        print("Mining too fast! Increasing difficulty.")
        new_target_value = int(currblocktarget, 16) // 64  # Gradually increase difficulty
        currblocktarget = hex(new_target_value)[2:].zfill(len(currblocktarget))  # Format correctly
        print(f"🚨 New difficulty target: {currblocktarget}")
    elif mtimer.total_seconds() > 120:  # Prevent getting stuck
        print("Mining too slow! Resetting difficulty.")
        currblocktarget = "000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
    return currblocktarget

def miner():
    '''Demo a simplified miner that starts with the Genesis block'''
    prevblockheader = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    currblocktarget = "000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"

    hmethod = HashMethod("hash256_sha2")
    blockchain = BlockChain()
    transactiongenerator = TransactionGenerator(hmethod)

    

    # First Block
    block = Block(prevblockheader, currblocktarget, hmethod)
    for i in range(4211):
        block.addtransaction(transactiongenerator.generatetransaction())
    assert block.is_blockfull()
    assert block.is_blockreadytomine()
    mstart1 = datetime.now()
    while not block.applymining():
        continue

    blockchain.push(block)
    blockchain.notify()
    mtimer1 = datetime.now() - mstart1
    print("Block1 was mined and it took {} seconds".format(mtimer1))
    currblocktarget = adjust_difficulty(mtimer1, currblocktarget)

    # Second Block
    prevblockheader = hmethod.ciphertext(str(blockchain.getlastblock()))
    block2 = Block(prevblockheader, currblocktarget, hmethod)

    for i in range(4000):
        block2.addtransaction(transactiongenerator.generatetransaction())

    assert block2.is_blockfull()
    assert block2.is_blockreadytomine()
    mstart2 = datetime.now()
    while not block2.applymining():
        continue

    blockchain.push(block2)
    blockchain.notify()
    mtimer2 = datetime.now() - mstart2
    print("Block2 was mined and it took {} seconds".format(mtimer2))
    currblocktarget = adjust_difficulty(mtimer2, currblocktarget)

    # Third Block
    prevblockheader = hmethod.ciphertext(str(blockchain.getlastblock()))
    block3 = Block(prevblockheader, currblocktarget, hmethod)

    for i in range(4000):
        block3.addtransaction(transactiongenerator.generatetransaction())

    assert block3.is_blockfull()
    assert block3.is_blockreadytomine()
    mstart3 = datetime.now()
    while not block3.applymining():
        continue

    blockchain.push(block3)
    blockchain.notify()
    mtimer3 = datetime.now() - mstart3
    print("Block3 was mined and it took {} seconds".format(mtimer3))
    currblocktarget = adjust_difficulty(mtimer3, currblocktarget)

    print("-" * 40)
    print("SUMMARY")
    print("-" * 40)
    for i, blockadded in enumerate(blockchain.blockchain, start=1):
        print("Block #{} was added. It took {} steps to find it.".format(i, blockadded.nonce))
    print("Block1 took {} seconds".format(mtimer1))
    print("Block2 took {} seconds".format(mtimer2))
    print("Block3 took {} seconds".format(mtimer3))
    return mtimer1, mtimer2, mtimer3



def main():
    print("-" * 40)
    miner()
    print("-" * 40)

if __name__ == "__main__":
    main()
