import random

def coin_flip():
    if random.random() >= 0.5:
        return 'head'
    else:
        return 'tail'
    
print(coin_flip())