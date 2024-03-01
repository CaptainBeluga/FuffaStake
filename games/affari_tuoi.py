import secrets
import time
from basic_casino import *

def main():
    #multipliers
    GENERAL_SCHEME = [1.1,1.5,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,46,50]
    bets = [1.1,1.5,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,46,50] 

    DIVIDER = bets[10-1]

    opens = {}
    packets = {}

    red = 0
    blue = 0 

    numbers = []

    min_bet = 3
    count_bet = 0

    finish = False

    bet = on_started()

    def ask_packet(msg):
        
        choose = int(input(f"\n{msg}"))

        if((choose >= 1 and choose <= 19) and choose not in numbers):
            return choose
        

        else:
            return False


    def packet_change(msg):
        global player

        choose = input(str(f"\n{msg}")).lower()

        if(choose == "y"):
            #packet change
            while True:
                choose = ask_packet("PACKAGE TO CHANGE => ")

                if choose != False:
                    c = packets[choose] #choosen
                    packets[choose] = bets[0]
                    player = c
                    break

                else:
                    print("\nPACKAGE NUMBER NOT CORRET !")

    for x in range(len(bets)-1):
        choice = secrets.choice(bets)

        packets[x+1] = choice
        bets.remove(choice)

    player = bets[0]
    print(player)
    
    print(packets)
    time.sleep(1.5)

    while len(packets) != 0:
        if count_bet == min_bet and len(packets) != 1:
            min_bet+= 1
            count_bet = 0

            if(blue <= red):
                choose = input(str("\nOFFERT => TOO MANY BLUE PACKETS MISSING, YOU'LL PROBABLY LOOSE | SURREND ? (WIN 0.5X)  | (y: yes ; n: no) => ")).lower()

                if(choose == "y"):
                    print("\nGAME ENDED | you win YOU BET * 0.5")
                    finish = False
                    break

            
            else:
                packet_change("OFFERT => TOO MANY RED PACKETS MISSING, YOU'LL PROBABLY CHOOSE A RED IN A WHILE | CHANGE YOUR PACKAGE WITH ANOTHER ? | (y: yes ; n: no) => ")

        else:
            if len(packets) == 1:
                packet_change("OFFERT => LAST CHANGE | CHANGE YOUR PACKAGE WITH ANOTHER ? | (y: yes ; n: no) => ")

            print("\nPACKETS AVAILABLE: \n\n")
            for x in packets:
                print(f"PACKAGE => {x}")

            print("\nGENERAL BETS: \n")

            for x in range(len(GENERAL_SCHEME)):
                print(f"{GENERAL_SCHEME[x]}x {'--- X ---' if GENERAL_SCHEME[x] in opens.values() else ''}")

                if GENERAL_SCHEME[x] == DIVIDER:
                    print("")


            
            print(f"\nRED => {red}/10 | BLUE => {blue}/10\n")

            
            choose = ask_packet("PACKAGE TO OPEN => ")

            if choose != False:
                print(f"\n\n[!] PACKAGE {choose} => {packets[choose]} X")

                time.sleep(0.8)

                if(packets[choose] > DIVIDER):
                    red+=1
                else:
                    blue+=1

                count_bet +=1

                opens[choose] = packets[choose]
                packets.pop(choose)
                numbers.append(choose)

            
                finish = True

            else:
                print("\nPACKAGE NUMBER NOT CORRET !\n")


    if finish:
        print(f"YOU WON {player}X !")
        send(bet*player,bankAddress,playerAddress,bankPrivateKey)


    else:
        send(bet*0.5,bankAddress,playerAddress,bankPrivateKey)