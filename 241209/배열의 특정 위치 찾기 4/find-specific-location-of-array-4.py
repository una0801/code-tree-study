arr = list(map(int,input().split()))
cnt = 0
sum_num = 0
for num in arr:
    if num == 0:
        break
    if num%2==0:
        cnt+=1
        sum_num+=num
print(f"{cnt} {sum_num}")