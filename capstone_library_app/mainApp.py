from taxPayment import *
from manageTransactions import *
from manageUsers import *
from manageBooks import *
from libraryDict import *

#display the menu list
print("Welcome to Magis'Library")
displayMenu(mainMenu)
#input the menu
menu = int(input("Enter the number of the menu you want to run: "))


while menu != 6:
    if menu == 1 : #display data
        print("\n--------------------------------------------------\n")
        displayMenu(displayOptionMenu)
        inputDisplay= int(input("Enter the number of the menu you want to run: "))

        while inputDisplay !=4 :
            if inputDisplay == 1:
                displayBooks(book)
            elif inputDisplay == 2:
                displayUsers(user)
            elif inputDisplay == 3:
                displayTransactions(borrowTransaction,returnTransaction)
            else:
                pass
            print("\n--------------------------------------------------\n")
            displayMenu(displayOptionMenu)
            inputDisplay= int(input("Enter the number of the menu you want to run: "))  
            
    elif menu == 2: # add data
        print("\n--------------------------------------------------\n")
        displayMenu(addOptionMenu)
        inputDisplay= int(input("Enter the number of the menu you want to run: "))
        while inputDisplay !=4:
            if inputDisplay == 1:
                addBooks(book)
            elif inputDisplay == 2:
                addUsers(user)
            elif inputDisplay == 3:
                addTransactions(borrowTransaction,returnTransaction,user,book)
            else:
                pass
            print("\n--------------------------------------------------\n")
            displayMenu(addOptionMenu)
            inputDisplay= int(input("Enter the number of the menu you want to run: "))
    elif menu == 3: # edit data
        print("\n--------------------------------------------------\n")
        displayMenu(editOptionMenu)
        inputDisplay= int(input("Enter the number of the menu you want to run: "))
        while inputDisplay !=4 :
            if inputDisplay == 1:
                editBooks(book)
            elif inputDisplay == 2:
                editUsers(user)
            elif inputDisplay == 3:
                editTransactions(borrowTransaction,returnTransaction,user,book)
            else:
                pass
            print("\n--------------------------------------------------\n")
            displayMenu(editOptionMenu)
            inputDisplay= int(input("Enter the number of the menu you want to run: "))

    elif menu == 4: # delete data
        print("\n--------------------------------------------------\n")
        displayMenu(deleteOptionMenu)
        inputDisplay= int(input("Enter the number of the menu you want to run: "))
        while inputDisplay !=4 :
            if inputDisplay == 1:
                deleteBooks(book)
            elif inputDisplay == 2:
                deleteUsers(user)
            elif inputDisplay == 3:
                deleteTransactions(borrowTransaction,returnTransaction)
            else:
                pass
            print("\n--------------------------------------------------\n")
            displayMenu(deleteOptionMenu)
            inputDisplay= int(input("Enter the number of the menu you want to run: "))
    elif menu == 5: # tax payment
        print("\n--------------------------------------------------\n")
        displayMenu(taxOptionMenu)
        inputDisplay= int(input("Enter the number of the menu you want to run: "))
        while inputDisplay != 2:
            if inputDisplay == 1:
                taxpayment(user,returnTransaction)
            else:
                pass
            print("\n--------------------------------------------------\n")
            displayMenu(taxOptionMenu)
            inputDisplay= int(input("Enter the number of the menu you want to run: "))
    else :
        pass
    print("\n--------------------------------------------------\n")
    displayMenu(mainMenu)
    menu = int(input("Enter the number of the menu you want to run: "))
        
print('\n\nHave a Good Day!') 
