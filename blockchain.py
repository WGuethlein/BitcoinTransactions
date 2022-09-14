from flask import Flask, jsonify
import json
import datetime
import hashlib



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
            hash_operation = hashlib.sha256(str(newProof**2 - previousProof**2).encode()).hexdigest()

            #hashNoEncode = hashlib.sha256(
            #    str(newProof**2 - previous_proof**2)
            #).hexdigest()

            #see the different without encode
            #print(hashNoEncode)
            #print(hash_operation)

            #if the hash output returns a number with 5 0's at the end, checkProof becomes true
            if hash_operation[:5] == '00000':
                checkProof = True
            else:
                newProof += 1
        
        return newProof
        

    def hash(self, block):
        encodedBlock = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()

    def chainValid(self, chain):
        previousBlock = chain[0]
        blockIndex = 1

        while blockIndex < len(chain):
            block = chain[blockIndex]
            if block['previous_hash'] != self.hash(previousBlock):
                return False

            previousProof = previousBlock['proof']
            proof = block['proof']
            hashOperation = hashlib.sha256(str(proof**2 - previousProof**2).encode()).hexdigest()
            
            if hashOperation[:5] != '00000':
                return False
            previousBlock = block
            blockIndex += 1
        return True


app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previousBlock = blockchain.print_previous_block()
    previousProof = previousBlock['proof']
    proof = blockchain.proofWork(previousProof)
    previousHash = blockchain.hash(previousBlock)
    block = blockchain.createBlock(proof, previousHash)

    response = {
        'message': "A block is Mined",
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    
    return jsonify(response), 200


@app.route('/valid', methods = ['GET'])
def valid():
    valid = blockchain.chainValid(blockchain.chain)

    if valid:
        response = {'message': 'The Blockchain is valid'}
    else:
        response = {'message': 'The Blockchain is NOT valid'}
    return jsonify(response), 200

app.run(host='127.0.0.1', port=5000)