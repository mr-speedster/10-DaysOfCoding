num=int(input("Enter the number"))
temp=num
sum=0
rem=0
while(num>0):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=int(num/10)

if(sum==temp):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")