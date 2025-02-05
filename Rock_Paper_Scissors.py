import random
import time
import platform
import os

def clean_screen():
    plat = platform.system()
    if plat == "Windows":
        os.system("cls")
    elif plat == "Linux":
        os.system("clear")
    else:
        print("not_support")

def re_fun():
    inp = input("1.try agian or 2.Exit :> ")
    if inp == "1" :
        main()
    elif inp == "2" :
        exit()
    else:
        re_fun()

def main():
    score = 0
    win = 10
    lose = 10
    list_ch = ["paper" , "scissors" , "rock"]
    list_ic = ["🪨" , "📄", "✂️"]
    p = print
    i = 1
    clean_screen()

    screen = (f"""Welcome in :\n
    {list_ic[0]}   or   {list_ic[1]}   or   {list_ic[2]}
    """)
    p(screen)
    while i <= 3 :
        p(f"---------- Round {i} ----------\n")
        user_ch = input("you :> ")
        compl_ch = random.choice(list_ch)
        time.sleep(0.5)
        p(f"comp:> {compl_ch}\n")
        if user_ch == compl_ch :
            p("Equality")
        elif user_ch == "rock" and compl_ch == "paper" :
            p("you lost -10 ")
            score -= 10
            lose -= 1
        elif user_ch == "rock" and compl_ch == "scissors" :
            p("you win +10 ")
            score += 10
            win += 1
        elif user_ch == "paper" and compl_ch == "scissors" :
            p("you lost -10 ")
            score -= 10
            lose -= 1
        elif user_ch == "paper" and compl_ch == "rock" :
            p("you win +10 ")
            score += 10
            win += 1
        elif user_ch == "scissors" and compl_ch == "rock" :
            p("you lost -10 ")
            score -= 10
            lose -= 1
        elif user_ch == "scissors" and compl_ch == "paper" :
            p("you win +10 ")
            score += 10
            win += 1
        else :
            p("(:> you input is uncorrect")
            re_fun()
        i += 1
    clean_screen()

    if win > lose :
        p(f"you win in game 🏆 \nyour score({score})")
    elif win == lose :
        p(f"you Equality ️🤝\nyour score({score})")
    else:
        p(f"you lose in game 😞\nyour score({score})")
main()