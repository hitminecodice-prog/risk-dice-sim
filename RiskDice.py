import random 
#Asking for input here
num_red = int(input("Attacker (Red) - With how many troops you attack (1-3)?"))
num_blue = int(input("Defender (Blue) - With how many troops you defend (1-3)?"))
#Dices Randomizer sorted
red_dices = sorted([random.randint(1,6) for _ in range(num_red)], reverse= True)
blue_dices =  sorted([random.randint(1,6) for _ in range(num_blue)], reverse = True)
#Print functions
print(f"Red: {red_dices}")
print(f"Blue: {blue_dices}")
#Losses
red_losses= 0
blue_losses = 0
#Zip loop with losses
for red, blue in zip(red_dices, blue_dices):
    if red > blue:
        blue_losses += 1
        print(f"Red {red} wins vs Blue {blue}")
    else:
        red_losses += 1
        print(f"Blue {blue} wins/ties vs Red {red}")

print(f"\nFinal Result: Red Lost {red_losses}, Blue lost {blue_losses}")
#Battle Result
if blue_losses > red_losses:
    print("--- ATTACKER (RED) WINS AGAINST THE DEFENSE! ---")
elif red_losses > blue_losses:
    print("--- DEFENDER (BLUE) WINS AGAINST THE ATTACKER! ---")
else:
    print("--- ITS A STALEMATE/TIE! ---")
