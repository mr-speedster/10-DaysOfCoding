arr = [1,2,3,4,5]

newArr = []
while arr:
    mini = arr[0]
    for i in arr:
        if mini > i:
            mini = i
    newArr.append(mini)
    arr.remove(mini)
print(sum(newArr)-newArr[-1],sum(newArr)-newArr[0])
