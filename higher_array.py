def func(arr, n):
    count = 0
    for i in range(n):
        temp = arr[i]
    
        for j in range(i+1, n):
            flag = True
            if temp < arr[j]:
                flag = False
                break
        if flag:
            count += 1
    return count 
print(func([2, 8, 9, 7, 4, 2], 6))