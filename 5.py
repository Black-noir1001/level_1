def sum_min_and_max_number(list):
    list.sort()
    return f"min : {list[0] + list[1]} \nmax : {list[-1] + list[-2]}" 
print(sum_min_and_max_number([1,6,8,3,9])) # 4 , 17
