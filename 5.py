import os
import platform
import json
import datetime
import time

ti = datetime.datetime.now().strftime("%H:%M:%S")
da = datetime.datetime.now().strftime("%Y/%m/%d")

f = open("user_data.json", "r+")
data = json.load(f)


def re_fun():
    ch = input("1.contiune or 2.Exit :> ")
    if ch == "1":
        opera_fun()
    elif ch == "2":
        exit()
    else:
        re_fun()
    while ch != "1" or ch != "2":
        p("you input is has mastake please enter 1 or 2 ")
        ch = input("1.contiune or 2.Exit :> ")
        if ch == "1":
            opera_fun()
        elif ch == "2":
            exit()


def write_fun():
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)


def clean_screen():
    plat = platform.system()
    if plat == "Windows":
        os.system("cls")
    elif plat == "Linux":
        os.system("clear")
    else:
        p("not_support")


p = print
i = 0

massage_screen = """
++++++++++++++++++++
+  Welcome IN ATM  +
+       v1.0       +
++++++++++++++++++++
"""


def main(user_ch):
    if user_ch == "1":
        yo = int(input("Enter your money to withdraw :> "))
        while yo > data[id_card]["balane"]:
            p("please try again you dont have this balance in you accont")
            yo = int(input("Enter your money to withdraw :> "))
        p("your operation is done sucess . ")
        data[id_card]["balane"] -= yo
        data[id_card]["action"].append(f"Withdraw :> -{yo} ({ti})  ({da})")
        write_fun()
        p(f"Your account has now {data[id_card]['balane']} $")
        re_fun()

    elif user_ch == "2":
        dep = input("Enter id of persone to deposit in her account :> ")
        if dep in data and data[dep] != data[id_card] and data[dep]["block"] != True:
            mo = int(input("Enter your money to deposit :> "))
            while mo > data[id_card]["balane"]:
                p("please try again you dont have this balance in you accont")
                mo = int(input("Enter your money to withdraw :> "))
            data[id_card]["balane"] -= mo
            data[id_card]["action"].append(f"Deposit :> -{mo} ({ti}  ({da}))")
            data[dep]["balane"] += mo
            data[dep]["action"].append(f"Deposit for {id_card} :> +{mo} ({ti})  ({da})")
            write_fun()
            p(
                f'you now have {data[id_card]["balane"]} $\nyour deposit is done sucess ..'
            )
            re_fun()

        elif dep not in data:
            p("this id is uncorrect please try again")
            re_fun()

        elif data[dep]["block"] == True:
            p("you can't make Deposit to account has band , please return to bank")
            re_fun()

        elif data[dep]["id"] == data[id_card]["id"]:
            p("you can't do deposit to you account")
            re_fun()

    elif user_ch == "3":
        for i in range(len(data[id_card]["action"])):
            p(f"Your Account Statement {i+1}:\n{(data[id_card]['action'][i])}\n")
        re_fun()

    elif user_ch == "4":
        p(f'you account has {data[id_card]["balane"]} $')
        re_fun()

    elif user_ch == "5":
        exit()


def opera_fun():
    clean_screen()
    p(info_screen)
    user_ch = input("Enter :> ")
    main(user_ch)
    while user_ch not in range(1, 6):
        p("you input is uncorrect pleace : 1 , 2, 3, 4, 5")
        user_ch = input("Enter :> ")
        main(user_ch)


p(massage_screen)
id_card = str(input("Enter you id master Card :> "))
pa_card = str(input("Enter you password master Card :> "))

info_screen = f"""
+++++++++++++++++++++++++
   Welcome  {data[id_card]['name']}
    Your have {data[id_card]['balane']} $
++++++++++++++++++++++++++

1. Withdraw
2. Deposit
3. Account Statement
4. Your Balance
5. Exit
"""

if (
    id_card in data
    and pa_card == data[id_card]["passw"]
    and data[id_card]["block"] == False
):
    opera_fun()
elif (
    id_card in data
    and pa_card != data[id_card]["passw"]
    and not data[id_card]["block"] == True
):
    while i < 2:
        p(">> your pass is ucorrect please try again")
        pa_card = str(input("Enter you password master Card :> "))
        if (
            id_card in data
            and pa_card == data[id_card]["passw"]
            and data[id_card]["block"] == False
        ):
            opera_fun()
            break
        elif i == 1 and pa_card != data[id_card]["passw"]:
            p("your card id has band , please back to bank")
            data[id_card]["block"] = True
            write_fun()
        i += 1

elif id_card not in data:
    p(" >> iam sorry , please try again you id or password is uncorrect")

elif data[id_card]["block"] == True:
    p("your account has band , please back to bank")
    time.sleep(2)
