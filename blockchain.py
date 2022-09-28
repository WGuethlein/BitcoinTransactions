import json
import datetime
import hashlib
from RSA import encryption, decryption
import math

class Blockchain:

    def __init__(self):
        #initiate chain
        self.chain = []
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
            'proof': proof,
            'previous_hash': previous_hash
        }
        # add the block to the chain
        self.chain.append(block)

        return block

    def print_previous_block(self):
        return self.chain[-1]


    def proofWork(self, previousProof):
        newProof = 1
        checkProof = False

        while checkProof is False:
            
            #hash the string of (newProof^2 - previousProof^2)
            hash_operation = hashlib.md5(str(newProof**2 - previousProof**2).encode()).hexdigest()

            if hash_operation[:5] == '00000':
                checkProof = True
            else:
                newProof += 1

        return newProof
        

    def hash(self, block):
        encodedBlock = json.dumps(block, sort_keys = True).encode()
        return hashlib.md5(encodedBlock).hexdigest()



    def chainValid(self, chain):
        previousBlock = chain[0]
        blockIndex = 1

        while blockIndex < len(chain):
            block = chain[blockIndex]
            if block['previous_hash'] != self.hashWithRSA(previousBlock):
                return False

            previousProof = previousBlock['proof']
            proof = block['proof']
            hashOperation = hashlib.md5(str(proof**2 - previousProof**2).encode()).hexdigest()
            
            if hashOperation[:5] != '00000':
                return False
            previousBlock = block
            blockIndex += 1
        return True


    def hashWithRSA(self, block):
        prime1 = int(0xeb628434bcc2b89bafb2fe3e64a932dc8be90c11e954589c1120c938882ee8bba786be21787305a9bcb63c9f7ac3c2838f0c8458acfc2b62e7cbf8c1598a6d8c0d9e343662e37e37aefbe49b3fce5caafb36f03aa154fd996f15d6cec4e8f8f163182ff7c533eb40140e36861cf38e592e45127e3e02a284fcf956b0d84efc6d000ecd9b6d089f122a84725478e2cf86fce5170960c9ce838a2d71703e4ba6bcdf4e303fff1fb1e8236e02484e87f1da1857a8dabdeb5eb045673b1a06c1ff08c5c21271a432c35c6c9b38137102d9929311903afbd1ae0573e72b4b381eb6bd154236073eaa422bc98be4f141bb722a51b68a287a896bf53a79c43646842eff)
        prime2 = int(0xceb052c9732614fee3c0a197a5ae0fcd83422243918ab83bc678656ae0344232a7c1070b7d5aabaae2bda96bf590da4830238b606f24b29626f1bfa00cce39f5f9bb9c1c3ead98f2055e373abf01e1fe1c816e12e0ed13791461c435123dad8cbe80e474f753aa9d115a8b93c167adceaee5a18ceedef88d307427fc495d9e44d4268ba83c4a65c4667b7df79f342639da3ddd2777926848855ca0068668efe7f27d65f455074c960bbc168bfb3a1225cd6f42585ddba6b3484f36707524133b81dd01d062591fec1b756766aeebe667bf9e2480eebb5964bc5eaff4b165e142772ce64b229a7258667a3964f08e06dfbfe3e3c1cf918395b89c1fdb18907711)
        n = math.lcm((prime1-1)+(prime2-1))
        e = 65537
        m = json.dumps(block, sort_keys = True).encode()
        
        return encryption(n, m, e)

