import random
import platform
import os

with open("your_pass.txt" , "a") as info :
    def clean_screen():
        plat = platform.system()
        if plat == "Windows" :
            os.system("cls")
        elif plat == "Linux" :
            os.system("clear")
        else :
            print("not_support")

    clean_screen()

    print("""
        Welcome In Key Creator
    *****************************
        1.Password Pc
        2.Password Wifi
        3.Password ATM
        4.Password Accont
        
        5.Exit""")

    def show(c_p_s):
        rp = (f"""
            Your Password for {c_p_s}
        *****************************
            """)
        print(rp)

    c_p = int(input("::> "))

    if c_p == 1 :
        clean_screen()
        show("pc")
        fl = input("Enter your first name :> ")
        o = "".join(random.choices("1234567890!@#$%^&*()",k=4 ))
        print(f"your pass :> {fl+o}")
        info.write(f"your pass for pc : {fl+o} \n")
    elif c_p == 2:
        clean_screen()
        show("WiFi")
        l_n = int(input("Enter Your limit of pass :> "))
        o = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()",k=l_n ))
        print(f"you pass :> {o}")
        info.write(f"your pass for Wifi : {o} \n")
    elif c_p == 3:
        clean_screen()
        show("ATM")
        o= "".join(random.choices("1234567890",k=4))
        print (f" Your Password :> {o}" , end="")
        info.write(f"your pass for ATM : {o} \n")
    elif c_p == 4:
        clean_screen()
        show("accont")
        fl = input("Enter your first name :> ")
        o = "".join(random.choices("1234567890!@#$%^&*()",k=6 ))
        print(f"your pass :> {fl+o}")
        info.write(f"your pass for Accont : {fl+o} \n")
    elif c_p == 5:
        exit()