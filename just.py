my_list = [-15,15, 1, 23, -64]
new_list = []

for i in range(0,5):
    for j in range(1,5):
        if(my_list[i]>my_list[j]):
            temp=my_list[i]
            my_list[i]=my_list[j]
            my_list[j]=my_list[i]

print(my_list)
