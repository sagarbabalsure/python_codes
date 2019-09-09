import string
def intreverse(n):
	r=0
	while n!=0:
		r=(r*10)+(n%10)
		n=n/10
	return r

def matches(s):
	x=0
	for i in s:
		if i=='(':
			x=x+1
		elif i==')':
			x=x-1

	if x==0:
		return True
	else:
		return False

t=int(input("ENter number:"))
print(intreverse(t))
s=str(raw_input("ENter the string:"))
print(matches(s))