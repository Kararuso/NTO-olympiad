## Task 1
price = int(input())
sale1 = min(price*0.08, 100)
sale2 = price*0.05
print('{0:g}'.format(max(sale1, sale2)))



##Task 2
def add(x, y):
    return list(map(lambda a, b: a + b, x, y))
n = int(input())
members = list(map(int, input().split()))
print(' '.join(list(map(str, add(members + [0],[0]+members)))))






## Task 3 (v. 1)
n = int(input()) 
n -= 1
a = [""]*n
b = [""]*n
c = [""]*(n+1)
for i in range(n):
    b[i] = [0] * 3

k=0
for i in range(n):
    a[i] = input()
    for j in range(len(a[i])):
        if a[i][j] == " ":
            b[k][0] = a[i][0:j]
            b[k][1] = a[i][-(len(a[i])-j-1):]
            k += 1

f = 0
for i in range(n):
    for j in range(n):
        if b[i][1] == b[j][0]:
           b[i][2] = "net"
for i in range(n):    
    if b[i][2] != "net":
       f = i
c[0] = b[f][1]
c[1] = b[f][0]
for i in range(2, n):
    for j in range(n):
        if b[j][1] == c[i-1]:
            c[i] = b[j][0]
f = 0
for i in range(n):
    for j in range(n):
        if b[i][0] == b[j][1]:
           b[i][2] = "est"
for i in range(n):    
    if b[i][2] != "est":
       f = i
c[n] = b[f][0] 
for i in range(n+1):
    print(c[i])


## Task 3 (v.2)
n = int(input())
first, second= ['']*(n-1), ['']*(n-1)
for i in range(n-1):
    first[i], second[i] = input().split()
result = ['']*n
for i in second:
    if i not in first:
        result[0]=i
for i in range(n):
    current_name = result[i]
    for name, j in zip(second, range(n-1)):
        if name==current_name:
            result[i+1]=first[j]
print('\n'.join(result))





## Task 4
# put your python code here
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
