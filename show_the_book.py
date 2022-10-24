def whole_book():
    with open('phone_dir.csv', "r+") as f:
        book = f.read() 
        if len(book) == 0: 
            print( "There is no contact in the phonebook.") 
        else: 
            print(book) 
        
