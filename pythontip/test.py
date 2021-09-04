n=int(input())
sum=0
for i in range(0,n):
	a=input()
	b=input()
	sum+=int(a)*int(b)
sum=sum/100
print("%.3f" %sum)