import random

com_score = 0
use_score = 0

opt = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break
        
    if user_input not in opt:
        pritn(":( sorry but that option is not available") 
        continue
        
    random_num = random.randint(0, 2)
    computer_pick = opt[random_num]
    
    print('Computer picked', computer_pick + ".")
    
    if user_input == 'rock' and computer_pick == "scissors":
        print("You won")
        use_score += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won")
        use_score += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won')
        use_score += 1
    else:
        print("You lost")
        com_score += 1
        
        
print('The computer got', com_score, 'and you got', str(use_score) + '.') 

while True:
    if com_score > 1 and  com_score == use_score:
        print("It was a tie")
        break
    elif com_score > use_score:
        print('The computer overall won! :(')
        break
    else:
        print('Overall, won!!! :)')
        break

print('Good bye :(')

    
    
    
    
    
    
    
    
    

