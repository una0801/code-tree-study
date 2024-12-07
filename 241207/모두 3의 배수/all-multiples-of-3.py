a = [int(input())for _ in range(5)]
satisfied = True
for b in a:
    if b%3 != 0:
        satisfied = False
        break

if satisfied:
    print(1)
else: print(0)