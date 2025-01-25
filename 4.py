p = print

def sum_of_small_num(list):
    list.sort()
    return list[0] +list[1]

p(sum_of_small_num([1,6,7,2]))