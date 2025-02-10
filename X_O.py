import platform
import os
class x_o :
    list = [1,2,3,4,5,6,7,8,9]
    sc = f"""
    {list[0]} | {list[1]} | {list[2]}
    ----------
    {list[3]} | {list[4]} | {list[5]}
    ----------
    {list[6]} | {list[7]} | {list[8]}
    """
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

    def xc(self):

        return self.player1 , self.player2

i = 0
game = x_o("X")
game.clean()
print(game._x_o_)
pt = input(":> ")
if pt == "1" :
    user1 = input("Enter Your X or O : ")
    game = x_o(user1)
    game.clean()
    print(game.sc)
    # while i <= 9 :
    play_one = int(input(f"{game.player1} :>> "))
    game.list[play_one-1] = game.player1
    play_two = int(input(f"{game.player2} :>> ")) 
    game.list[play_two-1] = game.player2
    game.clean()
    print(game.sc)
    i += 1
elif pt == "2":
    exit()
else :
    while pt != "1" or pt != "2" :
        pt = input(":> ")
        if pt == "1" :
            user1 = input("Enter Your X or O : ")
            game = x_o(user1)
            game.clean()
            print(game.sc)
        elif pt == "2":
            exit()