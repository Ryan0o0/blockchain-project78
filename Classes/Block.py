import datetime
import hashlib

#hashed data = digital signature of a block

class Block:
    blockNo = 0
    timestamp = None
    nonce = 0
    data = None
    prev_hash = 0x0
    blockHash = 0x0



    def __init__(self, data):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.blockHash = self.hash()

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.blockNo).encode('utf-8')
        + str(self.data).encode('utf-8')
        + str(self.prev_hash).encode('utf-8')
        + str(self.timestamp).encode('utf-8')
        )
        return h.hexdigest()