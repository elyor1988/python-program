print("1 dan n gacha tub sonlar")
n=int(input('n = '))
x=[]
sanoq=0
for k in range(0, n+1):
    counter = 0

    for i in range(1, k+1):
        if k%i==0:
            counter=counter+1
    if counter==2:
        sanoq=sanoq+1
        x.append(k)
print(*x)
print(f'{sanoq} ta tub son bor')

