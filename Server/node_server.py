import datetime
import hashlib
#import messenger_client
#from messenger_client import main
class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return  "\nBlockNo: "+str(self.blockNo) + "\nCurrent Block hash" +str(self.hash())+"\nBlock Data: " + str(self.data) + "\nTime: "+str(self.timestamp) +"\n--------------"

class Blockchain:

    diff = 5
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next
        f=open("blockchainData.txt","a+")
        f.write((str(block)))
        f.close()
        print(block)

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()
#messenger_client.party
#n=messenger_client.Sender.run(n)

#choice=int(input("Enter 1 to continue voting :"))
#global myvote=""
#if choice==1:
    #myvote=input("please enter your party :")
#blockchain.mine(Block(str(messenger_client.party)))

#while blockchain.head != None:
 #   print(blockchain.head)
  #  blockchain.head = blockchain.head.next