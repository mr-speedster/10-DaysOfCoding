row=int(input("Enter the number of rows \n"))
for i in range(0,row):
    for j in range(0,row-int(i)):
        print("",end="\t")
    for k in range(0,((int(i)*2)-1)):
        print("*",end="\t")
    print("\n")