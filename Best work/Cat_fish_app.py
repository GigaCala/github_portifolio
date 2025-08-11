def main():
    print("Hello and welcome to the Giga Catfish Assistant. I am Giga Assist. Let's get started!")
    print(' ')
    print(' ')
    
    user_name = input("First, what's your name?: ")
    print(' ')
    print(f"Thank you, {user_name}, for using this app. We hope it helps you accurately calculate the amount you need to risk to start your fish farm.")
    print(' ')
    print(' ')
    
    budget = float(input("Please enter your budget (amount you're willing to risk on the fish farm). Note: This information will not be saved; it only helps to calculate whether starting a catfish farm with your available capital is advisable: "))
    print(' ')
    print(' ')
    
    num_fingerlings = int(input("How many fingerlings do you plan to start with?: "))
    print(' ')
    print(' ')
    
    pond_type = input("Which type of ponds do you plan to use? Options: Earth ponds, Tapoli ponds, or Water tanks: ").strip().lower()
    print(' ')
    print(' ')
    
    num_ponds = int(input("How many ponds do you plan to start with?: "))
    print(' ')
    print(' ')
    
    water_change_frequency = int(input("How often would you like to change the dirty water in a week?: "))
    print(' ')
    print(' ')
    
    labour_cost = 5000 
    print(' ')
    print(' ')
    
    cost_per_fingerling = 4
    cost_per_pond = {
        'earth ponds': 3000,
        'tapoli ponds': 2500,
        'water tanks': 5000
    }
    electricity_cost_per_day = water_change_frequency * 40

    total_fingerling_cost = num_fingerlings * cost_per_fingerling
    total_pond_cost = cost_per_pond.get(pond_type, 0) * num_ponds

    print(f"\nBased on your input:")
    print(' ')

    print(f"1. You will spend GHC {total_fingerling_cost} on fingerlings.")
    print(' ')
    
    print(f"2. You will spend approximately GHC {electricity_cost_per_day} on electricity to pump water inorder to change the dirty water of the fish, that is if you use borehole water.")
    print(' ')
    
    if pond_type in cost_per_pond:
        print(f"3. Using {num_ponds} {pond_type} will cost GHC {total_pond_cost}.")
        print(' ')
    else:
        print("3. Invalid pond type selected. Please choose from 'Earth ponds', 'Tapoli ponds', or 'Water tanks'.")
        print(' ')
        
    total_amount_to_spend = total_fingerling_cost + total_pond_cost + labour_cost + electricity_cost_per_day 
    print(f'Your budget is {budget} and your total cost plus labour cost if any, will be aproximately {total_amount_to_spend} per month, feed excluded(the cost will increase based on the feed you choose)')
    print(' ')

    if budget < total_amount_to_spend:
        print("\nWarning: Your budget may not be sufficient to cover the costs for starting the fish farm!.")
        print(' ')
    else:
        print("\nYour budget seems adequate for starting the fish farm. Best of luck with your venture!")
        print(' ')
if __name__ == "__main__":
    main()
