#Impot
import hashlib

#open nugget blockchain
f = open('Blockchain/1.block', "w")
g = open('Blockchain/2.block', "w")
h = open('Blockchain/3.block', "w")


#Block ///every block contains 2 transactions
class NuggetCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "\n-\n".join(transaction_list) + "\n-\n" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


#transactions
t1 = "Michael sends 2 NC to Eli"
t2 = "Luke sends 4 NC to Cain"
t3 = "Martin sends 67 NC to Passi"
t4 = "Thomas sends 0.3 NC to Eli"
t5 = "Passi sends 42.8 NC to Martin"
t6 = "Cain sends 17 NC to Luke"


# 2 transactions per block
#initial Block (first block) 
initial_block = NuggetCoinBlock("Initial Sctring", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash + "\n")
print("")

f.write(initial_block.block_hash)

#second block
second_block = NuggetCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash + "\n")
print("")

g.write(initial_block.block_hash + "\n" + second_block.block_hash)

#third block 
third_block = NuggetCoinBlock(initial_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash + "\n")
print("")

h.write(second_block.block_hash + "\n" + third_block.block_hash)


#close nugget blockchain
f.close()
g.close()
h.close()