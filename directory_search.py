# Поиск по фамилии

def get_key():
    key = input("Enter surname: ")
    return key
    

def dir_search(key):
    with open('phone_dir.csv', 'r') as f:    
        i = False
        for line in f.readlines():
            data = line.split("; ")        
            if data[0] == key:
                print(* data, sep=" ") 
                i = True
        if i == False:
            print("There is no such person in the directory")
    

