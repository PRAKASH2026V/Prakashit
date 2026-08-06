n=int(input("enter the value"))
nrev=0
while(n!=0):
    r=n%10
    nrev=(nrev*10)+r
    n//=10
print("reverse digit=",nrev)
if(n==nrev):
    print("Palindrome")
else:
    print("Not Palindrome")
n=int(input("Enter series value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial=",fact)
