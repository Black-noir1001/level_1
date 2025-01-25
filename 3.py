p = print
def negi_nums(num):
    if num < 0 :
        return num
    elif num > 0 :
        return num * -1
    else:
        return "none"

p(negi_nums(1))