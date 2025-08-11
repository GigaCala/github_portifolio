print("Hi this is my Giga quiz.")
user = input("Do you want to play? ").lower()

if user != "yes":
    print(":(")
    quit()
elif user == 'yes':
    print('Okay lets play :)!')

score = 0

user_answer = input("What is the full meaning of ROM?: ").lower()
if  user_answer == 'read only memory':
    print('Yes!')
    score += 1
else:
    print('Sorry its incorrect')

user_answer = input("What is the full meaning of  CPU?: ").lower()
if  user_answer == 'central processing unit':
    print('Correcto!')
    score += 1 
else:
    print("Not quite correct")
   
user_answer = input('What is the full meaning of RAM')    
if  user_answer == 'random access memory':
    print('Ace!')
    score += 1
else:
    print("Wrong answer")    

user_answer = input("What is the full meaning of GPU? ").lower()
if  user_answer == 'graphic processing unit':
    print('Thumbs up!')
    score += 1
else:
    print("Nope!")
    
user_answer = input("What is the full meaning of PSU? ").lower()
if  user_answer == 'power supply':
    print('Right!')
    score += 1
else:
    print('No!')
    
    
user_answer = input("What is the full meaning of GIGO? ").lower()
if  user_answer == 'garbage in garbage out':
    print('Yeah!')
    score += 1
else:
    print('Naaa!')
    

print('You got ' + str(score) + ' correct!!!')
print('You got ' + str((score / 5) * 100) + '%')

 