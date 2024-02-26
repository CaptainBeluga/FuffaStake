import random
import time
import os
from basic_casino import *


def main():
    global max_decks

    def give_card(current_count):
        global max_decks

        index = random.randint(1,max_decks)

        card = decks[index]
        decks.pop(index)

        max_decks-=1

        #Jack, Queen, King
        if card > 10:
            card = 10

        #ace
        elif card == 1:
            if current_count+11 > 21:
                card = 1 
            else:
                card = 11

        return card


    while True:
        os.system("cls")

        #SHUFFLE
        decks = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
        max_decks = len(decks)-1

        bet = on_started()

        player_count = 0
        dealer_count = 0

        playerBust = False
        dealerBust = False

        doubleDown = False


        for y in range(3):
            if y%2 == 0:
                player_count+= give_card(player_count)
            
            else:
                dealer_count+= give_card(dealer_count)



        #player turn
        while True:   
            if(player_count <= 21):  
                print(f"\nPLAYER => {player_count}")
                print(f"DEALER => {dealer_count}\n")

                if player_count == 21:
                    break

                choose = str(input("s => stand | h => hit | d => double | ---> "))

                if choose == "h":
                    player_count+= give_card(player_count)
                    doubleDown = True
                

                elif choose == "d":
                    if doubleDown == False:

                        if balance(playerAddress) > bet:
                            #double bet
                            send(bet,playerAddress,bankAddress,playerPrivateKey)
                            bet*=2
                            player_count+= give_card(player_count)

                            break
                        
                        else:
                            print("\nINSUFFICIENT FOUNDS !")
                    
                    else:
                        print("\nNOT AVAILABLE ATM !")

                elif choose == "s":
                    break


            else:
                playerBust = True
                break
                
        if(player_count > 21):
            playerBust = True

        if(playerBust == False):

            dealer_count+= give_card(dealer_count)
            #dealer turn

            while True:
                if(dealer_count < 17):
                    dealer_count+= give_card(dealer_count)

                elif(dealer_count > 21):
                    dealerBust = True
                    break
                
                else:
                    break

            
            time.sleep(round(random.uniform(0.5,2),1))

            print(f"\nPLAYER => {player_count}")
            print(f"DEALER => {dealer_count}\n")

            if(dealerBust):
                print("\nDEALER BUST ! GG YOU WIN !\n\n")
                send(bet*2,bankAddress,playerAddress,bankPrivateKey)


            else:
                if(player_count > dealer_count):
                    print("\nGG YOU WIN !\n\n")
                    send(bet*2,bankAddress,playerAddress,bankPrivateKey)
                
                elif player_count == dealer_count:
                    print("\nPUSH\n")
                    send(bet,bankAddress,playerAddress,bankPrivateKey)
                
                else:
                    print("\nYOU LOSE BRO\n\n")
                    time.sleep(1.5)

        else:
            print(f"\nBUST {player_count} ! GAME ENDED !")
            time.sleep(1.5)