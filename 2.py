def flutter_list(list):
    new_list = []
    for i in range(len(list)) :
        if i not in new_list and isinstance(list[i],int) :
            new_list.append(list[i])
        else :
            continue
    return new_list

print(flutter_list([1,2,"a",3,4,"b",5,6,"c"])) # [1,2,3,4,5,6]