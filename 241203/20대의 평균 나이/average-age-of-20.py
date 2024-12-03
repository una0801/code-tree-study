sum = 0
cnt = 0
while True:
    a = int(input())
    if 20 <= a <30:
        sum +=a
        cnt +=1
    else: break

print(f"{sum/cnt:.2f}")