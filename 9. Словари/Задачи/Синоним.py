n = int(input())
syn = {}
for i in range(n):
    word1, word2 = input().split()
    syn[word1] = word2
    syn[word2] = word1
targ = input()
print(syn[targ])