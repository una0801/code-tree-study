n = int(input())
num = list(map(float, input().split()))

sum_num = sum(num)
avg = f'{sum_num / n:.1f}'

print(avg)

if avg >= "4.0":
    print('Perfect')
elif avg >= "3.0":
    print('Good')
else: print('Poor')





