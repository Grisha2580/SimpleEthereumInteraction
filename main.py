from web3 import Web3
import numpy
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/5463e6e350cf40089bcb3505cba6f67a"))




def count_average_transactions(start_block=0, finish_block=web3.eth.blockNumber):
    amounts = []

    for x in range(start_block, finish_block + 1):
        block = web3.eth.getBlock(x)
        transactions_amount = len(block['transactions'])
        amounts.append(transactions_amount)

    return numpy.mean(amounts)

start_block_example = 800000
finish_block_example = 800010


example = count_average_transactions(start_block_example, finish_block_example)

print('From block {} to the {} block there are on average {} transactions per block'.format(start_block_example,
                                                                                  finish_block_example, example))





