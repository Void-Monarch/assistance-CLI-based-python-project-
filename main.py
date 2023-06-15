import datetime
import random
import subprocess
import time
import sys
import webbrowser

import MasterCmd
import pygame
import speech_recognition as sr
import pyttsx3
import re
import requests
import os
from rich import print as cprint


# Creating Voice engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 174)
engine.setProperty('voice', voices[0].id)

# voice engine setting complete


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #speak module

def masterCmd(query):
    print("in master cmd block")
    mcmd = MasterCmd.MasterCmd()
    if mcmd == "reset":
        exit(0)


def takeCommand():
    """
    To listen , and take input via voice
    :return:
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        cprint("[blue][+][/blue] [italic magenta]Listening...[/italic magenta]")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        cprint(f"[italic yellow]\tuser said[/italic yellow] [red]{query}[/red]")

        if query.lower() == "enter command mode":
            masterCmd(query.lower())

        return query.lower()
    except Exception as e:
        # print(e)
        cprint("[red][-] Say that again please ...[red] ")
        return "None"

def check_exit(query):
    if re.search("^exit$", query) or re.search("^quit$", query):
        speak("Terminating !!")
        cprint("\n[purple][+-] Terminating !![/purple]\n\n")
        exit(0)
    elif (len(query.split()) <= 2):
        cprint("[red][?][/red] Do you want to , [orange] close Me ? [/orange] ")
        speak("Do you want to , close Me ? ")
        confirm = takeCommand()
        if confirm == "yes" or confirm == "yep":
            exit()

def gandu(query):
    engine.setProperty('rate', 154)
    possible_response = ["abay, tu ho gaa gandu", "chal chal gandu", "tu Gandu , i am smart", "chal teri maa ki "]
    speak(random.choice(possible_response))
    engine.setProperty('rate', 174)

def repeat(query):
    speak(query.replace('repeat', " ", 1))

def wishHello(query):
    speak("hello, nice to meet you . I am your assistant, call me void !")

def play_music(query):
    pygame.mixer.init()
    try:
        print("[?] What would you like to play ?")
        speak("What would you like to play ?")
        mList = os.listdir()
        for i in mList:
            if "mp3" in i:
                print(i)
        x = takeCommand()
        cprint("[green][*] Playing Music[/green]")
        pygame.mixer.music.load(x+".mp3")
        pygame.mixer.music.play()

    except Exception as e:
        pass

def stop_music():
        pygame.mixer.music.stop()
        cprint("[red][*] Stoping music[/red]")


# Number game

class Difficulty:

    def __init__(self):
        cprint("\n[italic green][+] Select the Difficulty of the Game...[/italic green]\n1. Easy\n2. Medium\n3. High\n4. Hell\n")
        speak("select game difficulty")
    def level(self):
        # Level selector
        easy = 10
        medium = 30
        high = 50
        hell = 100
        i = 0
        while i == 0:
            try:
                print(">> ")
                x = takeCommand()
                if x == 'easy':
                    x=1
                if x == 'medium':
                    x = 2
                if x == 'hard':
                    x = 3
                if x == 'hell':
                    x = 4

                sel_level = int(x)
                i = 1
            except ValueError:
                cprint("[red][-] [/red][orange]wrong Input !! Invalid Operation!![/orange]")

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
        cprint("[+] A Number as per your difficulty has been chosen\n")
        return number
# Contains the different level for the game such as easy , medium , high

class User(Difficulty):

    def __init__(self):
        cprint("[aqua]Hello user !!\nThe game will now begin!!\n[/aqua]")

    def user(self):
        print("\rEnter user name >> ")
        speak("Enter user name ")
        username = str(takeCommand())
        return username

    def guess_count(self, diff):
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

    def __init__(self,count):
        cprint(f"[+] Total amount of turns[red] {count}[/red]\n")


    def start(self,number,count):
        count2 = count
        for _ in range(count):
            i = 0
            while i == 0:
                try:
                    print("\nEnter Guess >> ")
                    speak("Enter Guess")
                    guess = int(takeCommand())
                    i=1
                except ValueError:
                    cprint("[red][-] [/red][orange]wrong Input !! Invalid Operation!![/orange]")

            count2 = count2 - 1

            if number > guess:

                cprint("\n[yellow][+] Go Higher[/yellow]")
                speak("ho higher")
                if (number-guess <5):
                    print("just a bit ")
                    speak("just a bit higher")
                if (number-guess >= 5 and number-guess < 10):
                    print(" A little Higher")
                    speak("a little Higher")
                if (number-guess >= 10 and number-guess < 20):
                    print(" bit more higher")
                    speak("bit more higher")
                if (number-guess >= 20):
                    print("Much higher")
                    speak("way off, think big")

            if number < guess:
                print("\n[sky-blue][+] Go Lower[/sky-blue] ")
                speak("go lower")
                if (number-guess < -5):
                    print("just a bit ")
                    speak("just a bit")
                if (number-guess <= 5):
                    print(" Just a little Lower")
                    speak("a little more")
                if (number-guess <= 15 and number-guess > 5):
                    print(" more Lower")
                    speak("more lower")
                if (number-guess <= 20 and number-guess > 15):
                    print(" Much Lower")
                    speak("way off , think small")

            if guess == 69:
                print("[+]!!!AMAZING NUMBER !!! Hope you get some you VIRGIN ass")
                speak("[+]!!!AMAZING NUMBER !!! Hope you get some you VIRGIN ass")

            if number == guess:
                print("[+]!!! correct guess !!!")
                speak("correct guess, amazing")
                return count2


    def score(self, chances_used,username,diff):
        max_count = super().guess_count(diff)
        if max_count > 50:
            print("[+] Easy Mode score is not counted")
        else:
            points_obtained = max_count - chances_used
            cprint("[+] Guess Used ", points_obtained)
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

            cprint(f"{username} have scored |  {score}")
            speak(f"{username} have scored {score}")



class Game():

    def __init__(self):
        cprint("[bold magenta][+] [/bold magenta]Random Number guess game")

    def menu(self):
        cprint("[green][+][/green] Menu \n1> Start\3\n2> High Scores\n3> Exit\n")
        i = 0
        while i == 0:
            try:
                speak("choose a option")
                print(">> ")
                x = takeCommand()
                if x == 'start':
                    x = 1
                if x == 'score':
                    x = 2
                if x == 'exit':
                    x = 3
                option_choice = int(x)
                i = 1
            except ValueError:
                cprint("[red][-] [/red][orange]wrong Input !! Invalid Operation!![/orange]")

        return option_choice

    def ScoreCard(self):
        with open("score.txt", 'r') as out_file:
            for x in out_file:
                cprint("[red][+] [/red]" + x)
            print("\n-----------------------------x---------------------------------")


def numberGame():
    game = Game()
    counteri = 0
    while counteri == 0:
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
            gp = Game_play(count)
            chances_used = gp.start(number, count, )
            score = gp.score(chances_used, username,diff)
        if option == 2:
            game.ScoreCard()
        if option == 3:
            counteri = 1
            speak("Game has ended ")
            print('\n[+] Game has ended\n')


def openList(query,querys):
    if re.search("^open\sbrowser*", query):
        speak("opening Browser!")
        url = "www.google.com"
        try:
            if len(querys) <= 5:

                if "search" in query:
                    url = query.split()[4]
                    if "www" not in url:
                        url = "www." + url
                    if ".com" not in url:
                        url = url + ".com"
            else:
                pass
        except Exception as e:
            pass
        cprint("\t[italic green][+] Opening Browser [/italic green]")
        if len(querys) > 6:
            searchBrowser(query)
        else:
            webbrowser.open(url=url, new=1)

def searchBrowser(query):
    url = "www.google.com"
    x = query.find("search")
    z = len(query.split())
    s = query.split()
    y = "/search?q="
    for i in range(x+1, z):
        y = y + s[i]
    url = url+y
    cprint("\t[italic green][+] Opening Browser [/italic green]")
    speak(f"opening Browser! showing results ")

    webbrowser.open(url=url, new=1)

if __name__ == '__main__':

    while True:
        query = takeCommand()
        # Logic for Querys

        # Exit logic
        if 'exit' in query:
            check_exit(query)
        if 'quit' in query:
            check_exit(query)

# Hello mudule to pass a greeting
        if query == "hello":
            wishHello(query)

# Gandu Module
        if query == "gandu":
            gandu(query)

# Say module
        if query.startswith("repeat"):
            repeat(query)

# clear the terminal
        if query == "clear screen" or query == "clear" or query == "clear output":
            subprocess.call("cls", shell=True)

# Play Music and files
        if query == "play music":
            play_music(query)

        if query == "stop music":
            stop_music()

# play a number game
        if query == "play number game":
            numberGame()

#open browser

        querys = query.split()
        if "open" in querys[0]:
            openList(query,querys)

#search a word
        if querys[0] == "search":
            searchBrowser(query)
