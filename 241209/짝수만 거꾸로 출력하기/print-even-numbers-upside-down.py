n = int(input())
arr = list(map(int,input().split()))

reverse = arr[::-1]

for num in reverse:
    if num%2 == 0:
        print(num,end=" ")