import json
import platform
import datetime
import os
import time

p = print

class Bank():
    sc = """
    ________________________
    **** Bank Mangement ****
    ------------------------
    1. Veiw info accounts and Mangemint
    2. Add new account
    3. Exit
    """

    sc_2 = """
    ________________________
    **** Bank Mangement ****
    ------------------------
    1. Veiw all id and users name
    2. Add and remove ban
    3. Reteurn
    4. Exit
    """

    def  __init__(self):

        self.name = 50
    
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
        con = input("Are Sure to add this new account in system 1.yes 2.no 3.Return 4.Exit :>")
        if con == "1" :
            fi =  open("user_data.json" , "r+")
            json.dump(data[num],fi,indent=4) # Edit
        elif con == "2" :
            Bank.clear_screen()
            p("try again ... ")
            time.sleep(2)
            Bank.add_accout()
        elif con == "3" :
            Bank.main()
        elif con == "4" :
            exit()

    @staticmethod
    def main():
        Bank.clear_screen()
        p(Bank.sc)
        in_us = input("::> ")
        if in_us == "1" :
            Bank.clear_screen()
            p(Bank.sc_2)
            in_ve = input("::>> ")
            if in_ve == "1"  :
                def sc2():
                    nums_list = []
                    name_list= []
                    id_list = []
                    Bank.clear_screen()
                    file3 = open("user_data.json" , "r+")
                    rd = json.load(file3)
                    for nums in rd.keys():
                        nums_list.append(nums)
                        for names in rd[nums]["name"] :
                            name_list.append(rd[nums]["name"])
                            break
                        for ids in rd[nums]["id"] :
                            id_list.append(rd[nums]["id"])
                            break
                    for na , nu , i in zip(name_list , nums_list , id_list) :
                        p("_"*50+f"""\n{na}\t:|:\t{nu}\t:|:\t{i}""")
                    con2 = input("\nEnter 1.Return 2.Exit :> ")
                    if con2 == "1" :
                        Bank.main()  # edit again 
                    elif con2 == "2" :
                        exit()
                    else:
                        while con2 not in [1,2] :
                            con2 = input("Enter 1.Return 2.Exit :> ")
                            if con2 == "1" :
                                Bank.main()
                            elif con2 == "2" :
                                exit()    
                sc2()                    
            elif in_ve == "2" :
                Bank.clear_screen()
                file = open("user_data.json" , "+r")
                da = json.load(file)
                acc_ba = input("Enter number of accont to has ban or remove :> ")
                if da[acc_ba]['block'] == False :
                    p("this account is not has ban")
                else:
                    p("this account has ban")
                acc_fu = input("ban or unban :> ")
                if acc_fu == "ban" :
                    da[acc_ba]["block"] = True
                    with open("user_data.json" , "w+") as file2 :
                        json.dump(da , file2 , indent=4)
                    file.close()
                    r_v = input("1.Return 2.Exit :> ")
                    if r_v == "1" :
                        Bank.main()
                    elif r_v == "2" :
                        exit()
                    else :
                        while r_v not in range (1,3):
                            p("you input is erro")
                            r_v = input("1.Return 2.Exit :> ")
                            if r_v == "1" :
                                Bank.main()
                            elif r_v == "2" :
                                exit()
                elif acc_fu == "unban" :
                    da[acc_ba]['block'] = False
                    with open("user_data.json" , "w+") as file2 :
                        json.dump(da , file2 , indent=4)
                    file.close()
                    r_v = input("1.Return 2.Exit :> ")
                    if r_v == "1" :
                        Bank.main()
                    elif r_v == "2" :
                        exit()
                    else :
                        p("you input is erro")
                        while r_v not in range(1,3):
                            r_v = input("1.Return 2.Exit :> ")
                            if r_v == "1" :
                                Bank.main()
                            elif r_v == "2" :
                                exit()              
                else:
                    p("you input in mistake , try again")
                    time.sleep(1)
                    Bank.main()
            elif in_ve == "3" :
                Bank.main()

            elif in_ve == "4" :
                exit()
            
            else :
                while in_ve not in [1,2,3,4] :
                    p("you input is erro , please try agains!!")
                    in_ve = input("::>> ")
                    if in_ve == "1"  :
                        def sc2():
                            nums_list = []
                            name_list= []
                            id_list = []
                            Bank.clear_screen()
                            file3 = open("user_data.json" , "r+")
                            rd = json.load(file3)
                            for nums in rd.keys():
                                nums_list.append(nums)
                                for names in rd[nums]["name"] :
                                    name_list.append(rd[nums]["name"])
                                    break
                                for ids in rd[nums]["id"] :
                                    id_list.append(rd[nums]["id"])
                                    break
                            for na , nu , i in zip(name_list , nums_list , id_list) :
                                p("_"*50+f"""\n{na}\t:|:\t{nu}\t:|:\t{i}""")
                            con2 = input("\nEnter 1.Return 2.Exit :> ")
                            if con2 == "1" :
                                Bank.main()  # edit again 
                            elif con2 == "2" :
                                exit()
                            else:
                                while con2 not in [1,2] :
                                    con2 = input("Enter 1.Return 2.Exit :> ")
                                    if con2 == "1" :
                                        Bank.main()
                                    elif con2 == "2" :
                                        exit()    
                        sc2()                    
                    elif in_ve == "2" :
                        Bank.clear_screen()
                        file = open("user_data.json" , "+r")
                        da = json.load(file)
                        acc_ba = input("Enter number of accont to has ban or remove :> ")
                        if da[acc_ba]['block'] == False :
                            p("this account is not has ban")
                        else:
                            p("this account has ban")
                        acc_fu = input("ban or unban :> ")
                        if acc_fu == "ban" :
                            da[acc_ba]["block"] = True
                            with open("user_data.json" , "w+") as file2 :
                                json.dump(da , file2 , indent=4)
                            file.close()
                            r_v = input("1.Return 2.Exit :> ")
                            if r_v == "1" :
                                Bank.main()
                            elif r_v == "2" :
                                exit()
                            else :
                                p("you input is erro")
                                exit()
                        elif acc_fu == "unban" :
                            da[acc_ba]['block'] = False
                            with open("user_data.json" , "w+") as file2 :
                                json.dump(da , file2 , indent=4)
                            file.close()
                            r_v = input("1.Return 2.Exit :> ")
                            if r_v == "1" :
                                Bank.main()
                            elif r_v == "2" :
                                exit()
                            else :
                                p("you input is erro")
                                exit()
                        else:
                            p("you input in mistake , try again")
                            time.sleep(1)
                            Bank.main()
                    elif in_ve == "3" :
                        Bank.main()

                    elif in_ve == "4" :
                        exit()

        elif in_us == "2" :
            Bank.add_accout()
        elif in_us == "3" :
            exit()
        else:
            while in_us not in [1,2,3] :
                p("you make a mistake in you input , please try again !!")
                time.sleep(2)
                Bank.main()


Bank().main()