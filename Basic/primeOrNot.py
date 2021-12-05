num=int(input("Enter the number"))
flag=0
for i in range(2,int(num/2)):
    if(num%i==0):
        flag=1
        break
if flag==1:
    print("The number is not prime")
else:
    print("The number is prime")