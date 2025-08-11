# Initialize variables for player hands and choices
coke = ""
fanta = ""
moringa = ""

# Initial state of the hands
user_hand1 = "O"
user_hand2 = "O"

# Function to update hand states based on choice
def update_hands(choice, hand1, hand2):
    if choice.lower() == "coke":
        print('Cocacola')
        if hand1 == "O":
            hand1 = "|||||"
        elif hand1 == "|||||":
            hand1 = "||||"
        elif hand1 == "||||":
            hand1 = "|||"
        elif hand1 == "|||":
            hand1 = "||"
        elif hand1 == "||":
            hand1 = "|"
        elif hand1 == "|":
            hand1 = "0"
    elif choice.lower() == "fanta":
        print('Fantastic')
        if hand2 == "O":
            hand2 = "|||||"
        elif hand2 == "|||||":
            hand2 = "||||"
        elif hand2 == "||||":
            hand2 = "|||"
        elif hand2 == "|||":
            hand2 = "||"
        elif hand2 == "||":
            hand2 = "|"
        elif hand2 == "|":
            hand2 = "0"
    elif choice.lower() == "moringa":
        print('Moringa ginger gips')
        if hand1 == "O":
            hand1 = "|||||"
        elif hand1 == "|||||":
            hand1 = "||||"
        elif hand1 == "||||":
            hand1 = "|||"
        elif hand1 == "|||":
            hand1 = "||"
        elif hand1 == "||":
            hand1 = "|"
        elif hand1 == "|":
            hand1 = "0"
    return hand1, hand2

# Game loop
while user_hand1 != "0" and user_hand2 != "0":
    print(f"Current hands: Hand1: {user_hand1}, Hand2: {user_hand2}")
    user_One = input("Coke and fanta which one do you like? : ")
    
    user_hand1, user_hand2 = update_hands(user_One, user_hand1, user_hand2)

    if user_hand1 == "0" or user_hand2 == "0":
        print("Player 1 wins!")
        break

    print(f"Current hands: Hand1: {user_hand1}, Hand2: {user_hand2}")
    user_Two = input("Coke and fanta which one do you like? : ")

    user_hand1, user_hand2 = update_hands(user_Two, user_hand1, user_hand2)
    
    if user_hand1 == "0" or user_hand2 == "0":
        print("Player 2 wins!")
        break

print(f"Final hands: Hand1: {user_hand1}, Hand2: {user_hand2}")
