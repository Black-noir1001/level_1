def power_numbers(num,powr):
    result = 1
    for i in range(powr) :
        result *= num
    return result

def conti(list):
    for i in range(2):
        k = list[-1]
        list.append(k+1)
    return (list)

def editor_v1(ch , ind , ed):
    k = list(ch)
    k[ind] = ed
    return ("".join(k) ) 

def editor_v2(ch ,ind ,ed):
   return ch[:ind]+ ed +ch[ind+1:]

def isVoild(passw):
        if   passw.isdigit() and len(passw) == 4:
            return (True)
        else :
            return (False)

def max_num(list):
    sum = 0
    num_list = []
    for i in list:
        if isinstance(i,int):
            num_list.append(i)
        elif isinstance(i,str):
            num_list.append(int(i))
    for x in num_list :
        sum += x
    return sum

def count_char_v1(char ,text):
    count = 0
    ls = list(text)
    for i in ls :
        if i == char :
            count += 1 
        else:
            continue
    return count

def ignore_elem(num ,list):
    new_list = []
    for i in list :
        if i == num :
            continue
        else :
            new_list.append(i)
    return(new_list)

def flutter_list(list):
    new_list = []
    for i in range(len(list)) :
        if i not in new_list and isinstance(list[i],int) :
            new_list.append(list[i])
        else :
            continue
    return new_list

def sum_of_postive_numbers(list):
    sum = 0
    for i in list :
        if i > 0:
            sum += i 
    return sum 

def negitve_return(num):
    if num < 0 :
        return num
    else:
        return num * -1
    
def sum_min_and_max_number(list):
    list.sort()
    return f"min : {list[0] + list[1]} \nmax : {list[-1] + list[-2]}" 

def count_word(string):
    count = 1
    sr = list(string)
    for i in range(len(sr)):
        if sr[i] == " " :
            count += 1
    print(count)

def checker_list (list):
    if len(set(list)) == len(list):
        return "this list is clear"
    else :
        return "this list unclear"
    
def between(num1 ,num2):
    new_list = []
    for i in range(num1 , num2 +1) :
        new_list.append(i)
    return new_list

def checker_sum_odd_or_even(list):
    sum = 0
    for i in list :
        sum += i
    if sum % 2 == 0 :
        return "even"
    else :
        return "odd"