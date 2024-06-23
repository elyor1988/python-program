n=int(input())
s=input()
L=s.count('L')
if L>2:
    L=2
R=s.count('R')
if R>2:
    R=2
print(L+R+1)


