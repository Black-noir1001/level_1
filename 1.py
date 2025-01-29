import os
import platform

p = print
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
            inp1 = int(input("Enter frist number >>> "))
            inp2 = input("Enter opration >>> ")
            inp3 = int(input("Enter secound number >>> "))
            p (f"the result : {calculator(inp1,inp3,inp2)}")
        elif ch == "2" :
            exit() 
        else :
            p("try again")   
            
def calculator(num1 , num2 , opra):
    try :
        if opra == "+" :
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
        else :
            return "please try agin"
    except ValueError:
        print("you input is uncorrect , please try again")

inp1 = int(input("Enter frist number >>> "))
inp2 = input("Enter opration >>> ")
inp3 = int(input("Enter secound number >>> "))
p (f"the result : {calculator(inp1,inp3,inp2)}")
re_fun()