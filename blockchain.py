class BlockChain:

    def __init__(self):
        self.blockchain = []

    def add_block(self, transaction):
        if len(self.blockchain) == 0:
            self_hash = hash((transaction, 0))
            self.blockchain.append((0, transaction, self_hash))
        else:
            parent_hash = self.blockchain[len(self.blockchain) - 1][2]
            self_hash = hash((transaction, parent_hash))
            self.blockchain.append((parent_hash, transaction, self_hash))

        return self_hash

    def find_block_by_hash(self, self_hash, index):
        if self.blockchain[index][2] == self_hash:
            return index

        if index < len(self.blockchain) - 1:
            return self.find_block_by_hash(self_hash, index + 1)
        else:
            return None

    def update_blockchain(self, self_hash, update):
        target_block_pos = self.find_block_by_hash(self_hash, 0)
        if target_block_pos is None:
            print("invalid hash")
            return

        target_block = self.blockchain[target_block_pos]
        new_hash = hash((update, target_block[0]))
        self.blockchain[target_block_pos] = (target_block[0], update, new_hash)
        self.update_further_chain(target_block_pos + 1, new_hash)
        return new_hash

    def update_further_chain(self, target_block_pos, parent_hash):
        if target_block_pos >= len(self.blockchain):
            return

        target_block = self.blockchain[target_block_pos]
        self.blockchain[target_block_pos] = (parent_hash, target_block[1], hash((target_block[1], parent_hash)))
        self.update_further_chain(target_block_pos + 1, target_block[2])

    def proof_of_work(self, index=1):
        if index >= len(self.blockchain):
            return True

        current_block = self.blockchain[index]
        prev_block = self.blockchain[index - 1]
        if current_block[0] == prev_block[2]:
            return self.proof_of_work(index + 1)
        else:
            return False
