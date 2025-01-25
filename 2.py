def sum_of_pos(list):
    sum = 0
    for nums in list :
        if nums > 0 :
            sum += nums
    return sum
print(sum_of_pos([1,2,-9]))