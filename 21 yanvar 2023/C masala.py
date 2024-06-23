n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
for i in matrix:
    if i[0]>i[1]+i[2]+1 or i[1]>i[0]+i[2]+1 or i[2]>i[0]+i[1]+1:
        print('no')
    else:
        print('yes')
