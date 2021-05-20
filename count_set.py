def country(n):
    count= []
    for a in range(n):
        count.append(input())
    new_set = set(count)
    return(len(new_set))
    

number = int(input("Enter Number"))
print(country(number))