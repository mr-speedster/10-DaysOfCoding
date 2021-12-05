#code
A=[]
N=int(input("Enter the size"))
print("Enter the Elements")
for i in range(0,N):
    element=input()
    A.append(element)

for j in range(N,0,-1):
    print(A[j])
