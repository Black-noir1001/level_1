def connter(s , cont):
    count = 0
    for i in range(len(s)):
        if s[i:i+len(cont)] == cont :
            count += 1
    return count

print(connter("hh" , "h"))