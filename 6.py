p = print

def check_list(list):
    return len(list) != len(set(list))

p(check_list([12,2,3,34,4,5]))