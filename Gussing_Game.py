import os
import platform
import random
p = print
def clean_screen ():
    plat = platform.system()
    if plat == "Windows" :
        os.system("cls")
    elif plat == "Linux" :
        os.system("clear")
    else :
        p("not_support")

def screen(type):

    f_s =  ("""
    ###########################
    # Welcome in Gussing Game #
    ###########################

    Choise :

    1. Gussing Numbers
    2. Exit
    """)

    n_g = ("""
    ##############################
    # Welcome in Gussing Numbers # 
    #       Hot or Cold          #
    ##############################

         >>> ( 1 to 10 ) <<<
    """)

    if type == "screen" :
        print(f_s)
    elif type == "numbers" :
        print(n_g)

def Gu_nu():

    limt = 0
    clean_screen()
    screen("numbers")
    num = random.randint(1,10)

    while limt < 5 :
        gs = int(input("Enter Yiur Guss :>> "))
        diff = abs(num - gs)
        if gs == num :
            print("Congratulations you win 😊🎉")
            break
        if diff == 1:
            p("This is very hot!")
        elif diff == 2:
            p("This is hot!")
        elif diff == 3:
            p("This is warm.")
        elif diff == 4:
           p("This is cold.")
        else:
           p("This is very cold.")  
        limt += 1
        if limt == 5 :
            p("iam sorry you lost , please try again 😢")
            
clean_screen()
screen("screen")

ch = int(input(">> "))
if ch == 1 :
    Gu_nu()
elif ch == 2 :
    exit()
else :
    p("please try again you input is has mastake")