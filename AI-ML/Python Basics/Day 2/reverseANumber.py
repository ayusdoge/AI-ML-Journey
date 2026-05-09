a=int(input("Enter a number: "))
d=int(0)
while a>0:
    d=d*10+a%10
    a=a//10
print("Reverse of the number is: ",d)