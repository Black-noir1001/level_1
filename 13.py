def max_num(list):
    sum = 0
    num_list = []
    for i in list:
        if isinstance(i,int):
            num_list.append(i)
        elif isinstance(i,str):
            num_list.append(int(i))
    for x in num_list :
        sum += x
    return sum

print(max_num([1,2,"3"])) # 6