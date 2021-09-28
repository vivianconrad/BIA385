x = int(input())
y = int(input())
z = int(input())

if x == y and x != z :
    eqalInts = 2
elif y == z and y != x :
    eqalInts = 2
elif z == x and z != y :
    eqalInts = 2

elif x == y and x == z :
    eqalInts = 3
elif y == z and y == x :
    eqalInts = 3
elif z == x and z == y :
    eqalInts = 3

print(eqalInts)