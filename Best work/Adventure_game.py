name = input('What is your name: ')
print('Welcome', name, 'to my adventure game! :)')
print('These are the rules:')
print("1.When answering a question, answer with the OPTIONS A/B")
print(' ')
print('2.Read the whole passage and think critically before answering each question')
print(' ')
print("3.When you see a message output 'invalid syntax' or 'You lose' then you have then you have to restart the program ")
print(' ')
print(' ')
print('With the rules stated ')
print('Let the fun begin ')
print(' ')
print(' ')



answer = input('You are walking in a jungle and you come across a dead end, you can go left or right which way do you go(A-left, B-right): ').lower()
print(' ')
print(' ')
if answer == 'b':
    answer = input('You end up walking through a  a valley with lots of skulks do you turn back or continue(A-back, B-continue): ').lower()
    if answer == 'a':
        print('You go back and step right into a quick sand you lose.')
        print(' ')
        print(' ')
    elif answer == 'b':
        print('It turns out that the valley is the hiding placa of a pack of lions you get eaten and you lose')
        print(' ')
        print(' ')

    else:
        print('Invalid syntax')
        print(' ')
        print(' ')

elif answer == 'a':
    answer == input('You reach a part of the forest that has lots of mosquito, do you wear your jacket and face the heat or get bitten by the mosquitos(A-wear jacket, B-get bitten: ').lower()
    print(' ')
    print(' ')
    if answer == 'a':
        answer = input('You wore the jacket and endured the heat. You later found water and food supplies in your backpack, do eat the us the provisions or save them for later(A-use them, B-save them): ').lower()
        print(' ')
        print(' ')
        if answer == 'a':
            print('You use all your supplies and later on you starve to death.You lose.')
            print(' ')
            print(' ')
        if answer == "b":
            answer = input("You saved them and later on used them when you really needed them. You come upon a village of babarians, do you ignore them and continue your walk or you speak to them(A-ignore them, B-speak to them): ").lower()
            print(' ')
            print(' ')
            if answer == 'a':
                print('You ignore them and walk into a trap. You lose: ')
                print(' ')
                print(' ')
            elif answer == 'b':
                print('You speak to them and become their friends, they warn you about the traps and how to avoid them, they also show you a destination which has a lot of treasure and leads you to your city')
                print(' ')
                print(' ')
            else:
                print('Invalid syntax:')
                print(' ')
                print(' ')
        else:
            print('Invalid syntax')
            print(' ')
            print(' ')
    elif answer == 'b':
        print('You get bitten and die of malaria :')
        print(' ')
        print(' ')
    else:
        print('Invalid syntax')
        print(' ')
        print(' ')
else:
    print("Invalid syntax")
    print(' ')

        