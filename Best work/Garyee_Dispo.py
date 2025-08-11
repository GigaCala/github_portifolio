items_store = ["rubber-1", "stationaries-2", "foil-3", "toothpick-4", 
               "kebab sticks-5", "shoe polish-6", "cloth pegs-7",  "disposables-8"]
               
oneToEight = ['1', '2', '3', '4', '5', '6', '7', '8']

rubber_items = {
    'Big take away rubber-1': 'GHC 9',                    
    'Medium take away rubber-2': 'GHC 5',                   
    'Small take away rubber-3': 'GHC 2p',                   
    'Koko rubber-4': 'GHC 4',                   
    'Sugar & Gari rubber-5': 'GHC 2',                   
    'Ice water rubber-6': 'GHC 2.50p',
    'Olonka rubber-7': 'GHC 4',
    'Half olonka rubber-8': 'GHC 2.50p',
    'Magirin rubber-9': 'GHC 2'
}

stationary_items = {
    'Pens-1': 'GHC 2',                    
    'Exercise books big-2': 'GHC 4.50p',
    'Exercise books small-3' : 'GHC 2',
    'Singing notebook-4': 'GHC 4',                   
    'Orange small tape-5': 'GHC 2',                   
    'White small tape-6': 'GHC 1.50p'
}


foil_items = {
    'Aluminum foil-1': 'GHC 22',
    'Rubber foil-2': 'GHC 22',
}

toothpick_items = {
    'Wooden toothpick-1': 'GHC 4p',
    'Pastic toothpick-2': 'GHC 7'
}

kebab_sticks_items = {
    'Gentle morning bamboo skewer large-1': 'GHC 5',
    'Gentle morning bamboo skewer medium-2': 'GHC 4',
    'Gentle morning bamboo skewer small-3': 'GHC 3'
}

shoe_polish_items = {
    'Miki polish-1': 'GHC 10',
    'Palc shoe polish-2': 'GHC 15',
    'Biki quick shine-3': 'GHC 8',
    'Lude polish-4': 'GHC 8'
}

cloth_pegs_items = {
    'Plastic cloth spin-1': 'GHC 10',
    'Yes pegs-2': 'GHC 10'
}

disposable_items = {
    'disposable_cup_items-1': {
        'Everpack party time coffee cup-1': 'GHC 12',
        'Small five-star cups-2': 'GHC 7', 
        'Anchor round cup big-3': 'GHC 12'
    },
    'cutlery_items-2': {
        'Disposable silver cutlery-1': 'GHC 25',        
        'Cut crystal spoon-2': 'GHC 16',
        'Space pack Ghana LTD forks-3': 'GHC 15',
        'Disposable plate-4': 'GHC 40',
        'Smile cutlery spoon-5': 'GHC 15'
    },
    'takeaway_items-3': {
        'take away pack(unit = full)': 'GHC 44',
        'take away plate(unit = full)': 'GHC 40',
    }
}


shop_keeper = input('Shop keeper input your name: ').upper()
starter_talk = input('How much money is in the bag already:GHC ') 
how_much_at_end = 0
customer_per = 1

if '.' in starter_talk:
    starter_money = float(starter_talk)
elif '.' not in starter_talk:
    starter_money = int(starter_talk)



print('Welcome to Garyee Dispo online shopping app, I am Giga Bot.')

while True:
    print("\n". join(items_store))
    wert = input("What would customer %s want to purchase?(type exit to quit/name(to change the name of the store keeper)):\n" % (customer_per)).lower()
    
    if wert == '1':
        print('These are our rubbers') 
        print("\n". join(rubber_items))
        inputer1 = input('Which one would you like to purchase?:\n')

    elif wert == '2':
        print('These are our statinaries')
        print("\n". join(stationary_items))
        inputer1 = input('Which one would you like to purchase?:\n').lower()

    elif wert == '3':
        print("\n". join(foil_items))
        inputer1 = input('Which one would you like to purchase?:\n')

    elif wert == '4':
        print("\n". join(toothpick_items))
        inputer1 = input('Which one would you like to purchase?:\n')

    elif wert == '5':
        print("\n". join(kebab_sticks_items))
        inputer1 = input('Which one would you like to purchase?:\n')

    elif wert == '6':
        print("\n". join(shoe_polish_items))
        inputer1 = input('Which one would you like to purchase?:\n')

    elif wert == '7':
        print("\n". join(cloth_pegs_items))
        inputer1 = input('Which one would you like to purchase?:\n')

    elif wert == '8':
        print("\n". join(disposable_items))
        inputer1 = input('Which one would you like to purchase?:\n')
        
    elif wert == 'name':
        new_shoppy = input('Input your name replacement shop keeper: ')
        shop_keeper = new_shoppy 
        continue
        
    elif wert == 'exit':
        print("%s GHC %s is suppose to be in the bag, count the money to be sure!!!" % (shop_keeper, how_much_at_end + starter_money))
        print('Thank you :)!')
        how_u = str(how_much_at_end)
        money_in_formum = open('c:\\test.txt', 'w')
        money_in_formum.write(how_u)
        money_in_formum.close()
        quit()
    
    elif wert not in oneToEight:
        print('We might not sell the product you want, or there might be a spelling mistake.')
        print('These are the items available at our store:')
        print(items_store)
        continue 

     
    
    while wert == '1':
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 9
            how_much_at_end += wert
            
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '2':
            how_many1 = int(input('how many do you want:\n'))
            wert = how_many * 4.5
            how_much_at_end += wert
        
            # mone_cus = input("Input your money: GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '3':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 1.80
            how_much_at_end += wert
            
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '4':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 4
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '5':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 1.50
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '6':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 2
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '7':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 3.50
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '8':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 2
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '9':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 1.80
            how_much_at_end += wert
            
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))

        elif inputer1.lower() not in rubber_items:
            print('We may not sell this type of rubber')
            print('These are the rubbers we sell:')
            print(rubber_items)
            continue



    while wert == '2':
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 1.50
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '2':
            how_many= int(input('how many do you want:\n'))
            wert = how_many * 4
            how_much_at_end += wert
        
            # mone_cus = input("Input your money: GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '3':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 2
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
        
        elif inputer1.lower() == '4':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 3
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '5':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 1.50
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() == '6':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 2
            how_much_at_end += wert
        
            # mone_cus = input("Input your money:GHC ")
            # change = int(mone_cus) - how_much_at_end
            # print("Your change is %s" % (change))
    
        elif inputer1.lower() not in stationary_items:
            print('We may not sell this stationary')
            print('These are the stationaries we sell:')
            print(stationary_items)
            continue
       
            
            
            
    
    while wert == '3': 
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 22
            how_much_at_end += wert
            
        if inputer1.lower() == '2':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 22
            how_much_at_end += wert        
            
    
        elif inputer1.lower() not in foil_items:
            print('We may not sell this foil')
            print('These are the foils we sell:')
            print(foil_items)
            continue      

    while wert == '4': 
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 4
            how_much_at_end += wert
            
        elif inputer1.lower() == '2':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 7
            how_much_at_end += wert        
            
    
        elif inputer1.lower() not in toothpick_items:
            print('We may not sell this toothpick')
            print('These are the toothpicks we sell:')
            print(toothpick_items)
            continue
        

    while wert == '5': 
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 5
            how_much_at_end += wert
            
        elif inputer1.lower() == '2':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 4
            how_much_at_end += wert
            
        elif inputer1.lower() == '3':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 3
            how_much_at_end += wert
        
    
        elif inputer1.lower() not in kebab_sticks_items:
            print('We may not sell this Khebab stick')
            print('These are the Khebab sticks we sell:')
            print(kebab_sticks_items)
            continue  
        
   
   

    while wert == '6': 
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 10
            how_much_at_end += wert
            
        elif inputer1.lower() == '2':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 15
            how_much_at_end += wert        
            
        elif inputer1.lower() == '3':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 8
            how_much_at_end += wert        

        elif inputer1.lower() == '4':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 8
            how_much_at_end += wert        
            
    
        elif inputer1.lower() not in shoe_polish_items:
            print('We may not sell this shoe polish')
            print('These are the shoe polish we sell:')
            print(shoe_polish_items)
            continue
        
        
        

    while wert == '7': 
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 3.50
            how_much_at_end += wert
            
        elif inputer1.lower() == '2':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 3.50
            how_much_at_end += wert        
            
    
        elif inputer1.lower() not in toothpick_items:
            print('We may not sell this toothpick')
            print('These are the toothpicks we sell:')
            print(toothpick_items)
            continue
             
        
    while wert == '8': 
        if inputer1.lower() == '1':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 3.50
            how_much_at_end += wert
            
        elif inputer1.lower() == '2':
            how_many = int(input('how many do you want:\n'))
            wert = how_many * 3.50
            how_much_at_end += wert        
            
    
        elif inputer1.lower() not in toothpick_items:
            print('We may not sell this toothpick')
            print('These are the toothpicks we sell:')
            print(toothpick_items)
            continue  
        
        
        
        
        
        
        
        
        
        
    exi_disco = input('Is that all you need? (yes or no):\n').lower()
    how_much = wert
    
    if exi_disco == 'yes':
        print('The items are GHC %s' % (how_much))
        mone_cus = input("Input your money:GHC ")
        change = int(mone_cus) - how_much
        change_for_real = round(change, 2)
        print("Your change is GHC %s" % (change_for_real))
        print('Thank you for shopping with us!')
        customer_per += 1
        continue
    elif exi_disco == 'no':
        continue
        
        
    