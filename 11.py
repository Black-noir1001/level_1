def editor_v1(ch , ind , ed):
    k = list(ch)
    k[ind] = ed
    return ("".join(k) ) 

def editor_v2(ch ,ind ,ed):
   return ch[:ind]+ ed +ch[ind+1:]

print(editor_v1("Nour" , 2 ,"o")) # Noor
print(editor_v2("Nour" , 0 ,"o")) # oour