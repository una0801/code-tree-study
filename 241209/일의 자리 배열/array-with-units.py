a,b = map(int,input().split())

arr = [a,b]

for i in range(2,10):
    temp = arr[i-2]+arr[i-1]
    arr.append(temp%10)

for num in arr:
    print(num, end= " ")
