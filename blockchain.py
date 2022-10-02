import json
import datetime
import hashlib

import math

class Blockchain:
           
    
    
    def __init__(self):
        #initiate chain
        self.chain = []
        #store the current hashes
        self.hash_lib = [0,0]
        #create the first block
        self.createBlock(proof=1, previous_hash=0)
        
        

    #create and add block to the chain
    def createBlock(self, proof, previous_hash):
        #create the structure of a block
        block = {
            #length of the chain + 1
            'index': len(self.chain) + 1,
            # time of transaction 
            'timestamp': str(datetime.datetime.now()),
            #nonce, iterations taken to create the desired hash
            'proof': proof,
            #show the hash of the second the last run (previous block)
            'previous_hash': self.hash_lib[-2],
            #show the hash of the last run (current block)
            'current_hash': self.hash_lib[-1]
        }
        # add the block to the chain
        self.chain.append(block)

        return block

    def print_previous_block(self):
        return self.chain[-1]

    def hash_array(hash_operation):
            return hash_operation

    
    def proofWork(self, previousProof):
        newProof = 1
        checkProof = False
      
        while checkProof is False:
            
            #hash the string of (newProof^2 - previousProof^2)
            hash_operation = hashlib.md5(str(newProof**2 - previousProof**2).encode()).hexdigest()
            #if it has 5 0's at the beginning, the hash is set
            if hash_operation[:5] == '00000':
                #set the proof to true
                checkProof = True
                #add the hash to the array
                self.hash_lib.append(hash_operation)
            else:
                #if it doesnt start with 5 0's, keep checking
                newProof += 1

        return newProof
        

    def hash(self, block):
        #the encoded block encoded in the JSON, without this the hex will be wrong
        encodedBlock = json.dumps(block, sort_keys = True).encode()
        # hash of the encoded block
        return hashlib.md5(encodedBlock).hexdigest()



    def chainValid(self, chain):
        #first block
        previousBlock = chain[0]
        blockIndex = 1

        #iterate through the chain
        while blockIndex < len(chain):
            block = chain[blockIndex]
            #if the hash of the previous block reported doesnt match the hash actual, its not valid
            if block['previous_hash'] != self.hash(previousBlock):
                return False

            previousProof = previousBlock['proof']
            proof = block['proof']
            hashOperation = hashlib.md5(str(proof**2 - previousProof**2).encode()).hexdigest()

            #if the first 56 digits do not equal 00000, its not valid
            if hashOperation[:5] != '00000':
                return False
            previousBlock = block
            blockIndex += 1
        return True

