import os
import platform

p = print
plat = platform.system()
if plat == "Windows" :
    os.system("cls")
elif plat == "Linux" :
    os.system("clear")
else :
    p("not_support") 

def calculator(num1 , num2 , opra):

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

inp1 = int(input("Enter frist number >>> "))
inp2 = input("Enter opration >>> ")
inp3 = int(input("Enter secound number >>> "))
p (f"the result : {calculator(inp1,inp3,inp2)}")