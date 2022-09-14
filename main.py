import blockchain as ONUChain
from flask import Flask, jsonify

# http://127.0.0.1:5000/mine_block
# http://127.0.0.1:5000/get_chain
# http://127.0.0.1:5000/valid


app = Flask(__name__)

blockchain = ONUChain.Blockchain()

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