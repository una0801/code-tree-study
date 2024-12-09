arr = list(map(int,input().split()))
cnt = 0
arr_sum = 0
for num in arr:
    if num == 0:
        break    
    cnt+=1
    arr_sum +=num

print(f"{arr_sum} {arr_sum/cnt:.1f}")