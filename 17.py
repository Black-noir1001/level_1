import os
import platform
import json
import datetime

ti = datetime.datetime.now().strftime("%H:%M:%S")
f = open("user_data.json" , "r+")
data = json.load(f)


def reco_fun():

    ...
def write_fun():
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)

def clean_screen():
    plat = platform.system()
    if plat == "Windows" :
        os.system("cls")
    elif plat == "Linux" :
        os.system("clear")
    else :
        p("not_support")

p  = print 
i = 0

massage_screen = """
++++++++++++++++++++
+  Welcome IN ATM  +
+       v1.0       +
++++++++++++++++++++
"""
info_screen = """
+++++++++++++++++++++++++
   Welcome  
    Your have 
++++++++++++++++++++++++++

1. Withdraw
2. Deposit
3. Account Statement
4. Your Balance
5. Exit
"""

def opera_fun():
    clean_screen()
    p(info_screen)
    user_ch = input("Enter :> ")
    if user_ch == "1":
        yo = int(input("Enter your money to withdraw :> "))
        if yo > data[id_card]["balane"] :
            p("please try again you dont have this balance in you accont")
            yo = int(input("Enter your money to withdraw :> "))
        else :
            p("your operation is done sucess . ")
            data[id_card]["balane"] -= yo
            data[id_card]["action"].append(f"Withdraw :> -{yo} ({ti})")

            write_fun()
            p(f"Your account has now {data[id_card]['balane']}")
    elif user_ch == "2" :
        dep = input("Enter id of persone to deposit in her account :> ")
        if dep in data and data[dep] != data[id_card]:
            mo = int(input("Enter your money to deposit :> "))
            if mo > data[id_card]["balane"] :
                while mo > data[id_card]["balane"] :
                    p("please try again you dont have this balance in you accont")
                    mo = int(input("Enter your money to withdraw :> "))
            else :
                data[id_card]["balane"] -= mo
                data[id_card]["action"].append(f"Deposit :> -{mo} ({ti})")
                data[dep]["balane"] += mo
                data[dep]["action"].append(f"Deposit for {id_card} :> +{mo} ({ti})")
                write_fun()
                p(f'you now have {data[id_card]["balane"]} \nyour deposit is done sucess ..')

        elif dep == data[id_card]:
            p("you can't do deposit to you account")
        else:
            p("the id of persone is not correct , pleace try later")
    elif  user_ch == "3" :
        p(f"Your Account Statement:\n{data[id_card]['action']}")
    elif user_ch == "4" :
        p(f'you account has {data[id_card]["balane"]} $')
    elif user_ch == "5" :
        exit()
p(massage_screen)
id_card = str(input("Enter you id master Card :> "))
pa_card = str(input("Enter you password master Card :> "))

try :
    if id_card in data and pa_card == data[id_card]["passw"]  and data[id_card]["block"] == False:
            opera_fun()
    elif id_card in data and  pa_card != data[id_card]["passw"] :
        while i < 2 :
            p(">> your pass is ucorrect please try again")
            pa_card = str(input("Enter you password master Card :> "))
            if id_card in data and pa_card == data[id_card]["passw"] and data[id_card]["block"] == False :
                opera_fun()
                break
            elif i == 1 and   pa_card != data[id_card]["passw"] :
                p("your card id has band , please back to bank")
                data[id_card]["block"] = True
                write_fun()
            i += 1
    elif data[id_card]["block"] == True :
        p("your account has band , please back to bank")
    else: 
        p(" >> iam sorry , please try again you id or password is uncorrect")
except KeyError:
    print("you should make input intgers")
