import os
import platform

scr = """
```````````````````````````````
``  Welcome in Calculator    ``
`` >>   ( + * % / - ^ )      ``
```````````````````````````````
"""
p = print
list_op = ["*","-","+","/","^","//"]

def clear_screen():
    plat = platform.system()
    if plat == "Windows" :
        os.system("cls")
    elif plat == "Linux" :
        os.system("clear")
    else :
        p("not_support") 

def re_fun():
    while 1 :
        ch = input("1.Contiune or 2.Exit :> ")
        if ch == "1" :
            clear_screen()
            p(scr)
            inp1 = input("Enter frist number >>> ")
            inp2 = input("Enter opration >>> ")
            inp3 = input("Enter secound number >>> ")
            if isinstance(inp1 , int) and isinstance(inp3 , int) and inp2 in list_op:
                p (f"the result {inp1} {inp2} {inp3} = {calculator(inp1,inp3,inp2)}")
            else :
                print("your input is uncorrect , pleace try again")
                re_fun()
        elif ch == "2" :
            exit() 
        else :
            p("try again")   

def calculator(num1 , num2 , opra):
    try :
        if opra == "+":
            return num1 + num2
        elif opra == "-" :
            return num1 - num2
        elif opra == "*" :
            return num1 * num2
        elif opra == "/" :
            return num1 / num2
        elif opra == "%" :
            return num1 % num2
        elif opra == "//" :
            return num1 // num2
        elif opra == "^" :
            result = 1
            for i in range(num2):
                result *= num1
            return result
        else :
            return "please try agin"
    except ValueError:
        print("you input is uncorrect , please try again")

clear_screen()
p(scr)
inp1 = input("Enter frist number >>> ")
inp2 = input("Enter opration >>> ")
inp3 = input("Enter secound number >>> ")

if isinstance(inp1 , int) and isinstance(inp3 , int) and inp2 in list_op:
    p (f"the result {inp1} {inp2} {inp3} = {calculator(inp1,inp3,inp2)}")
else  :
    print("your input is uncorrect , pleace try again")
    re_fun()