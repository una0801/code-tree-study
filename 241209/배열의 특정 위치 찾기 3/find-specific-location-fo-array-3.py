arr = list(map(int,input().split()))
cnt = 0
for num in arr:
    if num == 0:
        break
    cnt +=1

print(sum(arr[cnt-3:cnt]))