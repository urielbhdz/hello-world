import random
import time

def choice():

    player_dice = random.randint(1,6)
    print('You rolled', str(player_dice))
    cp_dice = random.randint(1,6)
    time.sleep(2)
    print('I rolled a', str(cp_dice))

    if player_dice > cp_dice:
        print('You might have won')
    elif player_dice == cp_dice:
        print('I guess we both lost')
    else:
        print("Yeah, you lost")

    print("Want to keep playing? Yes or no")
    cont = input()

    if cont == "Yes" or cont == "yes":
        exit()
    elif cont == "No" or cont == "no":
        print('see you later!')
        pass
    else:
        print("Yes or no are the only responses.")
while True:
        print("Press return to roll you die.")

        roll = input()
        choice()

