numbers=[]
sum=0
size=int(input("Enter the size of the array"))
print("Enter the numbers")
for i in range(0,size):
    num=int(input())
    numbers.append(num)
for j in numbers:
    sum=sum+j
print(sum)