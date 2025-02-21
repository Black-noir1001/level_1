import json
import platform
import datetime
import os
p = print
class Bank():
    sc = """
    ________________________
    **** Bank Mangement ****
    ------------------------
    1. Veiw info accounts
    2. Mange accounts
    3. Add new account
    4. Exit
    """
    sc_2 = """
    ________________________
    **** Bank Mangement ****
    ------------------------
    1. Veiw all  id
    2. Veiw all  names of accounts
    3. Veiw all  numbers  of accounts
    4. veiw spical account
    5. Exit
    """

    def  __init__(self):

        self.name = 50

    def read(self , info):
        self.info = info
        list_id = []
        with open("user_data.json" , "r+") as rd :
            j_r = json.load(rd)
            for keys in j_r.keys():
                list_id.append(keys)
            if info == "name" :
                for i in range(len(list_id)):
                    p(f"{i+1} : { j_r[list_id[i]]['name'] }")
            elif info == "id" :
                for i in range(len(list_id)):
                    p(f"{i+1} : { j_r[list_id[i]]['id'] }") 
            elif info == "accout" :
                for i in range(len(list_id)):
                    p(f"{i+1} : { list_id[i] }")
            elif info == "sp_id" :
                yo_se = input("Enter you number to git info :> ")
                p(f">> { j_r[yo_se]}")
            else :
                exit()        
            rd.close()
            
    def clear_screen():
        plat = platform.system().lower()
        if plat == "windows" :
            os.system("cls")
        elif plat == "linux" :
            os.system("clear")
        else:
            p("not support !!")
    
    @staticmethod
    def add_accout():
        list = ["name","id","passw","balane","block"]
        num = input("Enter number of account :> ")
        data = {num:{}}
        for i in list :
            data[num][i] = input(f"Enter {i} :> ")
        data[num]["opened"] = datetime.datetime.now().strftime("%H:%M:%S")
        data[num]["action"] = []
        Bank.clear_screen()
        keys_list = []
        val_list = []
        for keys in data[num].keys() :
            keys_list.append(keys)
        for val in data[num].values():
            val_list.append(val)
        for v in range(len(keys_list)):
            p(f"{keys_list[v]} : {val_list[v]}")
        con = input("Are Sure to add this new account in system 1.yes 2.no :>")
        if con == "1" :
            ...
        elif con == "2" :
            ...
    
    @staticmethod
    def main():
        Bank.clear_screen()
        p(Bank.sc)
        in_us = input("::> ")
        if in_us == "1" :
            Bank.clear_screen()
            p(Bank.sc_2)
            in_ve = input("::>> ")
            if in_ve == "1" :
                Bank.clear_screen()
                Bank().read("id")
            elif in_ve == "2" :
                Bank.clear_screen()
                Bank().read("name")
            elif in_ve == "3" :
                Bank.clear_screen()
                Bank().read("accout")
            elif in_ve == "4" :
                sr_in = input("Enter to scresh 1.id 2.name 3.number_account 4.Exit :> ")
                if sr_in == "1" :
                    Bank().read("sp_id")
            elif in_ve == "5" :
                exit()
        elif in_us == "2" :
            ...
        elif in_us == "3" :
            Bank.add_accout()
        elif in_us == "4" :
            exit()
        else:
            p("you make a mistake in you input , please try again !!")
                


Bank().main()