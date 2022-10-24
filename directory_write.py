# Внесение новой записи в справочник 

def direct_write():       
    f = {'Surname', 'Name', 'Phone', 'Description'}
    
    with open ('phone_dir.csv', 'a') as data:
        while True:
            surn = input("Surname: ")
            if surn.isalpha() and len(surn) >= 2: 
                data.write(f'{surn}; ')
                break
            else:
                print("It's not surname! Try again.")

        while True: 
            name = input("Name: ")
            if name.isalpha() and len(name) >= 2: 
                data.write(f'{name}; ')
                break
            else: 
                print("It's not name! Try again.")

        while True:
            phone = input("Phone number: ")
            if phone.isdigit() and 2 < len(phone) < 16: 
                data.write(f'{phone}; ')
                break
            else: 
                print("It's not a phone number! Try again.")
            
        descr = input("Description: ")
        data.write(f'{descr} \n')                    
    
    

      


       
            
