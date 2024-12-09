score = list(map(float, input().split()))

sum_score = sum(score)
avg_score = f'{sum_score/8:.1f}'

print(avg_score)