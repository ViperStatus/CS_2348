#Sokheng Ka 1968133

#First Problem
a = int(input())
b = int(input())
c = int(input())
#Second Problem
d = int(input())
e = int(input())
f = int(input())

verified_sol = False

for x in range(-10,11):
    for y in range(-10,11):
        if a*x+b*y == c and d*x+e*y == f:
            print(f'{x} {y}')
            verified_sol = True
            break
if not verified_sol:
    print('No solution')