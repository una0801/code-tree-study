a = int(input())

for i in range(1,a):
    for j in range(i):
        print('*',end= "")
    print()
    print()

for i in range(a,0,-1):
    for j in range(i):
        print('*',end="")
    print()
    print()