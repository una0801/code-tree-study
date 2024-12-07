a=int(input())


for i in range(a,0,-1):
    for j in range(i):
        print('*',end = " ")
    print()

for i in range(2,a+1):
    for j in range(i):
        print('*',end= " ")
    print()