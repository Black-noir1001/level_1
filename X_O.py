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
                list_range = [1,2,3,4,5,6,7,8,9]
                sc = f"""
                    {list_range[0]} | {list_range[1]} | {list_range[2]}
                    ----------
                    {list_range[3]} | {list_range[4]} | {list_range[5]}
                    ----------
                    {list_range[6]} | {list_range[7]} | {list_range[8]}
                """
                play_one = int(input(f"player 1 {game.player1} :>> "))
                list_range[play_one-1] = game.player1
                play_two = int(input(f"player 2 {game.player2} :>> ")) 
                list_range[play_two-1] = game.player2
                game.clean()
                print(sc)
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