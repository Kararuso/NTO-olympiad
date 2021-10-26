import itertools

numbers = list(map(int, input().split()))
permuts = list(itertools.permutations(numbers))

for r in permuts:
    d = r[0]
    if r[1]+r[2]>d and r[3]+r[4]>d and d+r[1]>r[2] and d+r[2]>r[1] and d+r[3]>r[4] and d+r[4]>r[3]:
        print(' '.join(list(map(str, r))))
        break
else:
    print(0)