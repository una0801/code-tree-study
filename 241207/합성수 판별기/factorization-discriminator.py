a = int(input())
is_composite = False
for i in range(1,a+1):
    if a%i==0:
        is_composite = True
        break

if is_composite:
    print('C')
else: print('N')