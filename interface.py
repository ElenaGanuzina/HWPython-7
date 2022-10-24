import directory_write as w
import directory_search as s
import show_the_book as b

def choose_act():
    while True:
        print ("New entry: 1\n")
        print("Find entry: 2\n")
        print("Show everything: 3 \n")
        print("Exit: 4 \n")
        choice1 = int(input("You choose: "))

        if choice1 == 1:
            w.direct_write()
            next = input("Press Enter to continue...")
            choose_act()
        elif choice1 == 2:
            s.dir_search(s.get_key())
            next = input("Press Enter to continue...")
            choose_act()
        elif choice1 == 3:
            b.whole_book()
            next = input("Press Enter to continue...")
            choose_act()
        elif choice1 == 4:
            break
        else:
            print("Wrong number! Try again \n")
    return choice1




  

