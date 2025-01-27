def checker_list (list):
    if len(set(list)) == len(list):
        return "this list is clear"
    else :
        return "this list unclear"
    
print(checker_list([1,2,3,1])) # this list unclear