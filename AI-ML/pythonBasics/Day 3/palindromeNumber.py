a=int(input("Enter a number: "))
t=a
r=0
while t>0:
    r=r*10+t%10
    t=t//10
      
if a==r:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")