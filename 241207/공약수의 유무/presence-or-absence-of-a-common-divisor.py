a,b = map(int,input().split())
is_common = False
for i in range(a,b+1):
    if 1920%i == 0 and 2880%i == 0:
        is_common = True
        break

if is_common:
    print(1)
else: print(0)