a = float(input('Enter the 1st coefficient (a): '))
b = float(input('Enter the 2nd coefficient (b): '))
c = float(input('Enter the 3nd coefficient (c): '))

d = b**2 - 4*a*c
x1 = (-b + d**0.5)/2*a
x2 = (-b - d**0.5)/2*a

print ("X1 = ",x1, " and X2 = ",x2)

