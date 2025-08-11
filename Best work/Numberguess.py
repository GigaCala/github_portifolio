import random

top_of_range = input('Type a number that will give you a range for you to guess between it and 0(eg :10, then you will have to guess between 0 and 10): ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time:')
        quit()
    
else:
    print('Please type a number next time')
    quit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number between 0 and " + str(top_of_range) + ": ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
        if user_guess < 0:
            print('Please it has to be a number equal to or larger than 0 :')
            continue
    
    else:
        print('Please type a number next time')
        continue
        
    if user_guess == random_number:
        print('You aced it!!!')
        break
    elif user_guess < random_number:
        print('Your guess was too low')
    else:
        print('Your guess was too high')
        
        
print("You got it in ", guesses, " guesses") 