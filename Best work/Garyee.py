# Welcome Page
print('                                              Welcome To Garyee Online Shopping App                                                                      ')

# List to store details of all users
users_list_seller = []
users_list_buyer = []

while True:
    # Register form
    userOne = input("Are you a Buyer/Seller (or type 'Bid' to see all bidders when you are done and you are a seller also 'exit' if you are done with everything.): ").strip()
    
    user_details_sell = {}
    user_details_buy = {}
    
    if userOne.lower() == 'seller':
        userTwo = input("First Name: ").strip()
        userSeven = input("Last Name: ").strip()
        userEight = input("Email: ").strip()
        
        # Email validation
        if not userEight.lower().endswith('@gmail.com'):
            print("Email must end with '@gmail.com'.")
        else:
            userThree = input("Product: ").strip()
            user_details_sell = {
                "Role": "Seller",
                "First Name": userTwo,
                "Last Name": userSeven,
                "Email": userEight,
                "Product": userThree,
                "Bid": None  
            }
            users_list_seller.append(user_details_sell)
            print(f"Thank you {userTwo} {userSeven} for registering as a Seller.")

    elif userOne.lower() == 'buyer':
        userFive = input("First Name: ").strip()
        userNine = input("Last Name: ").strip()
        userSix = input("Email: ").strip()
        
        # Email validation
        if not userSix.lower().endswith('@gmail.com'):
            print("Email must end with '@gmail.com'.")
        else:
            user_details_buy = {
                "Role": "Buyer",
                "First Name": userFive,
                "Last Name": userNine,
                "Email": userSix
            }
            users_list_buyer.append(user_details_buy)
            print(f"Thank you {userFive} {userNine} for registering as a Buyer.")
    
    elif userOne.lower() == 'bid':
        # Display saved user details for sellers
        if users_list_seller:
            print("\n --- Bidding Details ---")
            for index, user in enumerate(users_list_seller, start=1):
                print(f"\nSeller {index}:")
                for key, value in user.items():
                    print(f"{key}: {value}")
                if user["Bid"] is None:  
                    user["Bid"] = input("Bid: ").strip()
                    print(f"Bid placed: {user['Bid']}")
        else:
            print("No sellers registered yet.")
            
    elif userOne.lower() == 'exit':
        break
        
    else:
        print("Please input 'Buyer', 'Seller', 'Bid', or 'Exit'.")

