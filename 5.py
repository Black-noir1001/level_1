import os
import platform
import time 

def clear():
    plat = platform.system()
    if plat == "Windows" :
        os.system("cls")
    elif plat == "Linux" :
        os.system("clear")
    else :
        p("not_support") 

p  = print
screen_main = """
*** Manger Tasks *** \n
1. Add tasks in list
2. veiw the list
3. mark task as complite
4. Clean the list
5. exit"""

def write_fun(ty):
    fil =  open("tasks.txt" ,  "a+")
    task = input("Add Task :> ")
    p("adding is success")
    fil.write(task + f"\t ({ty}) \n")
    fil.close()

def read_fun():
    fil =  open("tasks.txt" ,  "r")
    clear()
    p("Your Taskes : ")
    p(fil.read())
    fil.close()  

def edit_fun():
    ed = int(input("Enter the task number to edit: ")) 
    with open("tasks.txt", "r") as fil:
        l_t = fil.readlines()
    if 1 <= ed <= len(l_t):
        l = l_t[ed - 1].strip()
        l = l.replace("F", "T")
        l_t[ed - 1] = l + "\n"
        with open("tasks.txt", "w") as fil:
            fil.writelines(l_t)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def clean_fun():
    with open("tasks.txt" , "w") as lif :
        lif.write("")
        lif.close()
        p("yous list is now clean")

def re_fun():
    re = input("1.Contuine or 2.Exit :> ")
    if re == "Contuine" or re == "1":
        manger_list()
    elif re == "Exit" or re == "2" :
        manger_list()
    else:
        re_fun()

def manger_list():
    clear()
    p(screen_main)
    user = input("Enter :> ")
    if user== "1" :
        write_fun("F")
        re_fun()
    elif user == "2" :
        read_fun()
        re_fun()
    elif user == "3" :
        edit_fun()
        re_fun() 
    elif user == "4" :
        clean_fun()
        re_fun()
    elif user == "5" :
        exit()
    else :
        p("please try again you input is problem , after 3 secound")
        time.sleep(3)
        manger_list()

manger_list()