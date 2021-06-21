from sys import stdin
from math import ceil

input = stdin.readline

a, b, v = map(int, input().split())

print(ceil((v - b) / (a - b)))
