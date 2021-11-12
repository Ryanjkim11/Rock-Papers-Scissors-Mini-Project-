import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissors or Q for quit: ").lower()
    if user_input == 'q':
        break 
    
    if user_input not in options: 
        continue
    
    random_number = random.randint(0, 2) # Rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")
    
    
    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
        
    
    elif user_input == "paper" and computer_pick == "rock": #I deleted the continue because we know they're true, instead of "continue", I used the elif conditional statement to have it run to the next line of code on its own. 
        print("you won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("you Won!")
        user_wins += 1
        
    else:
        print("You lost! ")
        computer_wins += 1
        
        """
        I just needed to make sure that the 3 Win conditions above were true
        which was the if, and two elif's. If any one of those were not true,
        it means the computer won th game, and us the users playing lost.
        So if I lost, I would print "You Lost!", and below add "computer_wins += 1". 
        """
        
print("You won", user_wins, "times.")
print("the computer won", computer_wins, "times.") 
print("Goodbye! ")    