def ignore_elem(num ,list):
    new_list = []
    for i in list :
        if i == num :
            continue
        else :
            new_list.append(i)
    return(new_list)

print(ignore_elem(5 , [1,2,3,4,5,6,7,8,9,5,5,5])) # [1,2,3,4,6,7,8,9]