import sys
from queue import Queue, PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

def nextNumber(secret):
    #Multiply by 64
    n = secret * 64
    #Mix into secret
    secret = n ^ secret
    #prune
    secret = secret % 16777216 
    n = int(secret / 32)
    secret = n ^ secret
    secret = secret % 16777216 
    n = secret * 2048
    secret = n ^ secret
    secret = secret % 16777216 
    return secret


answer = 0
for line in lines:
    secret = int(line)
    for i in range(2000):
        secret = nextNumber(secret)
    answer += secret

print(answer)