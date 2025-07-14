from flask import Flask, jsonify, request
from uuid import uuid4
from blockchain import Blockchain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block['proof'])

    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)

    block = blockchain.new_block(proof)

    # Compute and add hash here, separately
    block_with_hash = block.copy()
    block_with_hash['hash'] = blockchain.hash(block)

    return jsonify(block_with_hash), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    chain_with_hashes = []
    for block in blockchain.chain:
        block_copy = block.copy()
        block_copy['hash'] = blockchain.hash(block)
        chain_with_hashes.append(block_copy)

    return jsonify({'chain': chain_with_hashes, 'length': len(chain_with_hashes)}), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    for node in nodes:
        blockchain.register_node(node)
    return jsonify({'message': 'New nodes added', 'nodes': list(blockchain.nodes)}), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    if replaced:
        # Chain replaced – return it with hashes
        new_chain = []
        for block in blockchain.chain:
            block_copy = block.copy()
            block_copy['hash'] = blockchain.hash(block)
            new_chain.append(block_copy)
        return jsonify({'message': 'Our chain was replaced', 'new_chain': new_chain}), 200

    # Chain is authoritative – return with hashes
    authoritative_chain = []
    for block in blockchain.chain:
        block_copy = block.copy()
        block_copy['hash'] = blockchain.hash(block)
        authoritative_chain.append(block_copy)
    return jsonify({'message': 'Our chain is authoritative', 'chain': authoritative_chain}), 200

if __name__ == '__main__':
    app.run(port=5000)
