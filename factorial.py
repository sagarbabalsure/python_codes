
a=int(input("Enter any number: "))
b=1
if (a<0):
	print("factorial is not possible")
elif (a==1):
	print("factorial is one")
else:
    for i in range(b,a+1):
    	b=b*i
    	
print(b)
