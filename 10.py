def conti(list):
    for i in range(2):
        k = list[-1]
        list.append(k+1)
    return (list)

print(conti([1,2,3])) # [1, 2, 3, 4, 5] 