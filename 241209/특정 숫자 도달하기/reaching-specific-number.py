n = list(map(int,input().split()))
sum = 0
cnt = 0
for num in n:
    if num >= 250 :
        break;
    sum += num
    cnt +=1

print(f"{sum} {sum/cnt:.1f}")
