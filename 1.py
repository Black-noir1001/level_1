def flter(list):
    new_list = []
    for item in list :
        if isinstance(item , int ):
            new_list.append(item)
    return new_list

print(flter([1,2,3,4,"a" ,"b",5,6,"c"]))