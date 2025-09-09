n = int(input())
scores = list(map(int, input().split()))
scores.sort(reverse = True)
for i in range(len(scores)):
    if scores[i + 1] > scores[i]:
        print(scores[i - 1])
        break
