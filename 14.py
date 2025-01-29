def count_char_v1(char ,text):
    count = 0
    ls = list(text)
    for i in ls :
        if i == char :
            count += 1 
        else:
            continue
    return count

print(count_char_v1("e","iam senior software engineering")) # 5