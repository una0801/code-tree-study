n = int(input())  
num = list(map(int, input().split()))  


arr = [0] * 10  


for i in num:
    arr[i] += 1

for i in range(1, 10):
    print(arr[i])
