def sum_ev_or_od(list):
    sum  = 0
    for nums in list :
        sum += nums
    if sum % 2 == 0:
        return "even"
    else :
        return "odd"

print(sum_ev_or_od([1,2]))