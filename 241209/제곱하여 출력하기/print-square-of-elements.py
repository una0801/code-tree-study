n = int(input())
arr = list(map(int,input().split()))

new_arr = [num **2 for num in arr]
for new in new_arr:
    print(new,end= " ")