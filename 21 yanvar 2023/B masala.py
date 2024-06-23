n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in matrix:
    if (i[1]-i[0])%(i[2]+i[3]):
        print(-1)
    else:
        print((i[1]-i[0])//(i[2]+i[3]))