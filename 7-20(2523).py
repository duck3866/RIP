n = int(input())
for i in range(1,n+1):
    for j in range(1):
        print('*'*i)
n -= 1
for i in range(n,0,-1):
    for j in range(1):
        print('*'*i)