import cmath
a=float(input("Enter coefficient: "))
b=float(input("Enter coefficient: "))
c=float(input("Enter coefficient: "))
d=b*b-4*a*c
sol1= -b-(cmath.sqrt(d/(2*a)))
sol2=-b+(cmath.sqrt(d/(2*a)))
print("The roots of equation are {0} and {1}".format(sol1,sol2))