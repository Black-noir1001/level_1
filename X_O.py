import platform
import os
class x_o :
    _x_o_= """ 

    Welcome in game XO

        1. Start game
        2. Exit
    """
    def __init__(self , user1) :
        self.player1 = user1.lower()
        if self.player1 == "x" :
            self.player2 = "o"
        elif self.player1 == "o" :
            self.player2 = "x"
        else :
            ...

    def clean(self):
        self.cl = platform.system().lower()
        if self.cl == "windows" :
            os.system("cls")
        elif self.cl == "linux" :
            os.system("clear")
        else:
            print("not support")
    @staticmethod
    def main():
        game = x_o("X")
        game.clean()
        print(game._x_o_)
        pt = input(":> ")
        if pt == "1" :
            user1 = input("Enter Your X or O : ")
            game = x_o(user1)
            game.clean()
            for i in range(4):
                list = [1,2,3,4,5,6,7,8,9]
                sc = f"""
                    {list[0]} | {list[1]} | {list[2]}
                    ----------
                    {list[3]} | {list[4]} | {list[5]}
                    ----------
                    {list[6]} | {list[7]} | {list[8]}
                """
                play_one = int(input(f"player 1 {game.player1} :>> "))
                list[play_one-1] = game.player1
                play_two = int(input(f"player 2 {game.player2} :>> ")) 
                list[play_two-1] = game.player2
                game.clean()
                print(sc)

            if list[0] == list[1] == list[2]:
                print(f"{list[1]} is winer ")
            elif  list[3] == list[4] == list[5]:
                print(f"{list[4]} is winer ")
            elif list[6] == list[7] == list[8]:
                print(f"{list[7]} is winer ")            
            elif list[0] == list[3] == list[6] :
                print(f"{list[3]} is winer ")
            elif  list[1] == list[4] == list[7] :
                print(f"{list[4]} is winer ")
            elif  list[2] == list[5] == list[8] :
                print(f"{list[5]} is winer ")
            elif list[0] == list[4] == list[8] or list[2] == list[4] == list[6] :
                print(f"{list[4]} is winer ")
            else:
                con = input("no winer , 1 . player again 2. Exit :> ")
                if con == "1" :
                    game.main()
                elif con == "2" :
                    exit()
                else:
                    while con != "1" or con != "2" :
                        con = input("no winer , 1 . player again 2. Exit :> ")
                        if con == "1" :
                            game.main()
                        elif con == "2" :
                            exit()
        elif pt == "2":
            exit()
        else :
            while pt != "1" or pt != "2" :
                print("you input is hame mistake ! , please try again")
                pt = input(":> ")
                if pt == "1" :
                    game.main()
                elif pt == "2":
                    exit()

x_o("x").main()
