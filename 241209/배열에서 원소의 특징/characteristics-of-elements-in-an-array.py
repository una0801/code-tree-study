arr = list(map(int,input().split()))
cnt = 0
for i in range(1, len(arr)): 
    if arr[i] % 3 == 0:  
        print(arr[i - 1]) 
        break
