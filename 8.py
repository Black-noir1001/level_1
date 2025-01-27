def between(num1 ,num2):
    new_list = []
    for i in range(num1 , num2 +1) :
        new_list.append(i)
    return new_list

print(between(1,4)) # [1, 2, 3, 4]