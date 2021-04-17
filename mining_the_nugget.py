#YT Turorial: https://www.youtube.com/watch?v=ZhnJ1bkIWWk&t=1022s
#Imports
from hashlib import sha256
import time
import sys


#loading animation
def loading():
	blah="\|/-\|/-"
	for l in blah:
		sys.stdout.write(l)
		sys.stdout.flush()
		sys.stdout.write('\b')
		time.sleep(0.2)


#max nonce (max power to unse to mine)
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):

    prefix_str = '0'*prefix_zeros

    for nonce in range(MAX_NONCE):

        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        if new_hash.startswith(prefix_str):

            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45,
    Mando1->Cara2->3
    '''
    difficulty=4  # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    
    start = time.time()

    print("start mining ⛏️")
    loading()

    new_hash = mine(5,transactions,'0000000x459331876269aeded838969fa08f5b027d50486e774910c77ea10281e2e4eac9', difficulty)

    total_time = str((time.time() - start))

    print(f"end mining. Mining took: {total_time} sec.")

    print(new_hash)
