import threading
import concurrent.futures
import multiprocessing
import time
import random
from rich import print


class Difficulty:

    def __init__(self):
        print("\n[italic green][+] Select the Difficulty of the Game...[/italic green]\n1. Easy\n2. Medium\n3. High\n4. Hell\n")

    def level(self):
        # Level selector
        easy = 10
        medium = 30
        high = 50
        hell = 100
        i = 0
        while i == 0:
            try:
                sel_level = int(input(">> "))
                i = 1
            except ValueError:
                print("[red][-] [/red][orange]wrong Input !! Invalid Operation!![/orange]")


        if sel_level == 1:
            return easy
        elif sel_level == 2:
            return medium
        elif sel_level == 3:
            return high
        elif sel_level == 4:
            return hell
        else:
            print("[-] Invalid output")
            return 0

    def generator(self, diff):
        # Random number generator as per level
        number = random.randint(0, diff)
        print("[+] A Number as per your difficulty has been chosen\n")
        return number
# Contains the different level for the game such as easy , medium , high

class User(Difficulty):

    def __init__(self):
        print("[aqua]Hello user !!\nThe game will now begin!!\n[/aqua]")

    def user(self):
        username = str(input("\rEnter user name >> "))
        return username

    def guess_count(self,diff):
        if diff == 10:
            count = 100
        elif diff == 30:
            count = 10
        elif diff == 50:
            count = 10
        elif diff == 100:
            count = 10
        return count

class Game_play(User):

    def __init__(self,):
        print(f"[+] Total amount of turns[red] {count}[/red]\n")


    def start(self,number,count):
        count2 = count
        for _ in range(count):
            i = 0
            while i == 0:
                try:
                    guess = int(input("\nEnter Guess >> "))
                    i=1
                except ValueError:
                    print("[red][-] [/red][orange]wrong Input !! Invalid Operation!![/orange]")

            count2 = count2 - 1

            if number > guess:

                print("\n[yellow][+] Go Higher[/yellow]")
                if (number-guess <5):
                    print("just a little bit ")
                if (number-guess >= 5 and number-guess < 10):
                    print(" Just a little Higher")
                if (number-guess >= 10 and number-guess < 20):
                    print(" bit more higher")
                if (number-guess >= 20):
                    print("Much higher")

            if number < guess :
                print("\n[sky-blue][+] Go Lower[/sky-blue] ")
                if (number-guess < -5):
                    print("just a little bit ")
                if (number-guess <= 5):
                    print(" Just a little Lower")
                if (number-guess <= 15 and number-guess > 5):
                    print(" bit more Lower")
                if (number-guess <= 20 and number-guess > 15):
                    print(" Much Lower")

            if guess == 69:
                print("{++} Amazing number , gigtty  but try again !!!")

            if number == guess:
                print("[+]!!! correct guess !!!")
                return count2


    def score(self, chances_used,username):
        max_count = super().guess_count(diff)
        if max_count > 50:
            print("[+] Easy Mode score is not counted")
        else:
            points_obtained = max_count - chances_used
            print("[+] Guess Used ", points_obtained)
            score = diff * max_count - points_obtained

            if diff == 10:
                dx = "easy"
            if diff == 30:
                dx = "Medium"
            if diff == 50:
                dx = "High"
            if diff == 100:
                dx = "Hell"

            with open("score.txt", 'a') as out_file:
                out_file.write(f"\n" + f"{username} | Score {score} | Difficulty {dx} ")
                out_file.close()

            print(f"{username} have scored |  {score}")



class Game():

    def __init__(self):
        print("[bold magenta][+] [/bold magenta]Random Number guess game")

    def menu(self):
        print("[green][+][/green] Menu \n1> Start\3\n2> High Scores\n3> Exit\n")
        i = 0
        while i == 0:
            try:
                option_choice = int(input(">> "))
                i = 1
            except ValueError:
                print("[red][-] [/red][orange]wrong Input !! Invalid Operation!![/orange]")

        return option_choice

    def ScoreCard(self):
        with open("score.txt", 'r') as out_file:
            for x in out_file:
                print("[red][+] [/red]" + x)
            print("\n-----------------------------x---------------------------------")




if __name__ == '__main__':
    game = Game()
    while True:
        option = game.menu()
        if option == 1:
            # Start of the game
            u = User()
            username = u.user()
            d = Difficulty()
            diff = d.level()
            number = d.generator(diff)
            count = u.guess_count(diff)
            print(number)
            gp = Game_play()
            chances_used = gp.start(number, count, )
            score = gp.score(chances_used, username)
        if option == 2:
            game.ScoreCard()
        if option == 3:
            exit(0)
