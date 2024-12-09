n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
cnt = 0 
for num in arr:
    if (sum(num)/4) >= 60:
        print('pass')
        cnt +=1
    else: print('fail')
print(cnt)