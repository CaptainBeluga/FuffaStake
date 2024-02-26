import random
import time
import os
from dotenv import dotenv_values
from web3 import Web3


games = {}
game_counter = 0

for f in os.listdir("games"):
    if f.endswith(".py"):
        game_counter += 1
        games[game_counter] = f.replace(".py","")


while True:
    try:

        print("\n\nCASINO GAMES\n")
        
        for game in games:
            print(f"[ {game} ] -> {games[game]}\n")

        gameToLoad = int(input("\n\nGAME TO PLAY => "))


        if(gameToLoad > 0 and gameToLoad <= len(games)):

            getattr(__import__(f"games.{games[gameToLoad]}", fromlist=[""]),"main")()

    except Exception as e:
        trigger = True
        e = str(e).lower()

        errors = {
            #finance
            "already known-replacement transaction underpriced" : "TRANSACTION STILL IN PROGRESS !",
            "insufficient funds for gas" : "INSUFFICIENT BALANCE !",
            "address has an invalid" : "PLAYER ADDRESS WRONG !",

            #generic
            "invalid literal for int() with base 10:" : "TYPE ONLY NUMBERS !",
            "keyerror" : "GAME NOT AVAILABLE !"

        }

        for err in errors:

            errA = err.split("-")
            for er in errA:
                if er in e:
                    print(f"\n{errors[err]}\n")
                    trigger = False
                    break
        

        if trigger:
            print("\nGENERIC ERROR !\n")

        

    except KeyboardInterrupt:
        exit()