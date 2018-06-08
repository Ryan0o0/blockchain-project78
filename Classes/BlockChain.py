from Block import Block
from time import sleep

class Blockchain:
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    chain = None

    #Creates the very first block of the chain and adds it to the chain
    def createGenesisBlock(self):
        block = Block("Genesis")
        self.chain = [block]

    #Adds a block that is given in the parameters to the chain
    def addBlockToChain(self, block):
        prev_block = self.chain[len(self.chain) - 1]
        block.prev_hash = prev_block.blockHash
        block.blockNo = prev_block.blockNo + 1
        block.blockHash = block.hash()
        self.chain.append(block)

bc = Blockchain()

bc.createGenesisBlock()

#Sleeps for 2 seconds
sleep(2)

bc.addBlockToChain(Block("Test"))

for block in bc.chain:
    print("--------------------")
    print("BlockNo: " + str(block.blockNo))
    print("Data: " + str(block.data))
    print("Previous hash: " + str(block.prev_hash))
    print("Timestamp: " + str(block.timestamp))
    print("Block hash: " + str(block.blockHash))