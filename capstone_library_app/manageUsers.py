from libraryDict import *

# Showing all user filter
def showAllUsers(user):
    print('\n\nUsers List :')
    print('ID' + '  | ' +'Name   '+ '  |'+'Status   '+ '  |'+'Handphone Number   '+ '  |'+'Address                 '+ '  |'+'Tax   '+ '  |')
    for i in user.keys():
        print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+user[i][0]+' ' *(len('Name   ')-len(user[i][0])) +'  |'+user[i][1]+' ' *(len('Status   ')-len(user[i][1])) +'  |'
              +user[i][2]+' ' *(len('Handphone Number   ')-len(user[i][2])) +'  |'+user[i][3]+' ' *(len('Address                 ')-len(user[i][3])) +'  |'
              +str(user[i][4])+' ' *(len('Tax   ')-len(str(user[i][4]))) +'  |')

# Showing user who have tax filter
def showTaxUsers(user):
    print('\n\nUsers List :')
    print('ID' + '  | ' +'Name   '+ '  |'+'Status   '+ '  |'+'Handphone Number   '+ '  |'+'Address                 '+ '  |'+'Tax   '+ '  |')
    for i in user.keys():
        if user[i][4] > 0:
            print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+user[i][0]+' ' *(len('Name   ')-len(user[i][0])) +'  |'+user[i][1]+' ' *(len('Status   ')-len(user[i][1])) +'  |'
              +user[i][2]+' ' *(len('Handphone Number   ')-len(user[i][2])) +'  |'+user[i][3]+' ' *(len('Address                 ')-len(user[i][3])) +'  |'
              +str(user[i][4])+' ' *(len('Tax   ')-len(str(user[i][4]))) +'  |')
        else:
            continue

# Showing user who dont have any tax filter
def showFreeTaxUsers(user):
    print('\n\nUsers List :')
    print('ID' + '  | ' +'Name   '+ '  |'+'Status   '+ '  |'+'Handphone Number   '+ '  |'+'Address                 '+ '  |'+'Tax   '+ '  |')
    for i in user.keys():
        if user[i][4] == 0:
            print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+user[i][0]+' ' *(len('Name   ')-len(user[i][0])) +'  |'+user[i][1]+' ' *(len('Status   ')-len(user[i][1])) +'  |'
              +user[i][2]+' ' *(len('Handphone Number   ')-len(user[i][2])) +'  |'+user[i][3]+' ' *(len('Address                 ')-len(user[i][3])) +'  |'
              +str(user[i][4])+' ' *(len('Tax   ')-len(str(user[i][4]))) +'  |')
        else:
            continue

# READ FUNCTION
# Displaying users list
def displayUsers(user):
    print("DISPLAY USERS")
    print("Display User Menu")
    displayMenu(userMenu)
    #input the menu
    userInput = int(input("Enter the number of the menu you want to run: "))

    while userInput !=4 :
        if userInput ==1 : # display all users 
            showAllUsers(user)
            print("\n--------------------------------------------------\n")
            
            print("Display User Menu")
            displayMenu(userMenu)
            #input the menu
            userInput = int(input("Enter the number of the menu you want to run: "))    
    
        elif userInput ==2: # display free tax users
            showFreeTaxUsers(user)
            print("\n--------------------------------------------------\n")

            print("Display User Menu")
            displayMenu(userMenu)
            #input the menu
            userInput = int(input("Enter the number of the menu you want to run: "))  
        elif userInput ==3: # display users with tax
            showTaxUsers(user)
            print("\n--------------------------------------------------\n")

            print("Display User Menu")
            displayMenu(userMenu)
            #input the menu
            userInput = int(input("Enter the number of the menu you want to run: "))  
        else :
            pass

        print("DISPLAY USERS")
        print("Display User Menu")
        displayMenu(userMenu)
        #input the menu
        userInput = int(input("Enter the number of the menu you want to run: "))

# Function to increment data
def increment(data):
    increment=1
    for i in data.keys():
        if increment == i:
            increment=i+1
            continue
        else:
            increment=i-1
            break
    return increment
 
# CREATE FUNCTION
# ADD a User Function
def addUsers(user):
    print("ADD USERS")
    print("Add Users Menu")
    print("---Input 1 if you want to add users")
    print("---Input 0 if you want to cancel")

    inputAddUsers=int(input("Do you want to add new user?: "))

    while inputAddUsers !=0:
        if inputAddUsers == 1:
            print("\n--------------------------------------------------\n")
            showAllUsers(user)
            print("\n--------------------------------------------------\n")
            print("Start to input user data you want to add")
            
            # create new user
            newUser=[]
            # input name
            inputName=str(input("Input Name: "))
            if inputName=='0':
                break
            newUser.insert(0,inputName)
            print(f'Name: {inputName}')
            # input phone number
            inputPhone=str(input("Input Phone Number: "))
            if inputPhone=='0':
                break
            if len(inputPhone) == 12 or len(inputPhone) == 13: # check length of phone number is valid (12 or 13)
                newUser.insert(2,str(inputPhone))
                print(f'Phone Number: {inputPhone}')
            else:
                print(f'Your input length is wrong, your length input is {len(inputPhone)}')
                continue
            # input address
            inputAddress=str(input("Input Address: "))
            if inputAddress==0:
                break
            newUser.insert(3,inputAddress)
            print(f'Address: {inputAddress} ')
            # input default status and tax
            newUser.insert(1,'member')
            newUser.insert(4,int(0))

            print("\n--------------------------------------------------\n")
            print(f'This is your new user detail\nName: {inputName}\nPhone Number: {inputPhone}\nAddress: {inputAddress}')
            print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
            inputSave=int(input('Choose your option: '))

            while inputSave != 0:
                if inputSave==1:
                    inputUserID=increment(user) # Input ID with increment function
                    if (inputName!='' and inputAddress!='') and (type(inputName)==str and type(inputAddress==str and type(inputPhone)==str)):
                        user[inputUserID]=newUser
                        (f'{inputName} is Success')
                        print("\n--------------------------------------------------\n")
                        showAllUsers(user)
                        print("\n--------------------------------------------------\n")
                        break
                    else:
                        print("Wrong Input Cancelled to Save")
                        break
                else:
                    pass
                print("\n--------------------------------------------------\n")
                print(f'This is your new user detail\nName: {inputName}\nPhone Number: {inputPhone}\nAddress: {inputAddress}')
                print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                inputSave=int(input('Choose your option: '))

        else:
            pass
        
        print("ADD USERS")
        print("Add Users Menu")
        print("---Input 1 if you want to add users")
        print("---Input 0 if you want to cancel")

        inputAddUsers=int(input("Do you want to add new user?: "))

# Function for check if ID exist in the list
def checkID(data,inputData):
    status= False
    for i in range(1, len(data)+1):
        if i == inputData:
            status = True
        else:
            continue
    return status

# UPDATE FUNCTION
# Edit a User Function
def editUsers(user):

    print("\nEDIT USERS")
    
    showAllUsers(user)
    print("\n--------------------------------------------------\n")

    print("Edit Users Menu")
    print("---Input 1 if you want to edit users")
    print("---Input 0 if you want to cancel")

    inputEditUsers=int(input("Do you want to edit user?: "))

    while inputEditUsers !=0:
        if inputEditUsers == 1:
            print("\n--------------------------------------------------\n")
            showAllUsers(user)
            print("\n--------------------------------------------------\n")
            print("Choose user to edit...")
            inputUserID=int(input("Input User ID you want to edit: "))
            # Checking ID is exist
            if checkID(user,inputUserID) == True: # if detected can continue to edit
                print(f"User {user[inputUserID][0]} detected...")
                # new user list
                newUser=[]
                # input name
                inputName=str(input("Input Name: "))
                if inputName=='0':
                    break
                newUser.insert(0,inputName)
                print(f'Name: {inputName}')
                # input phone number
                inputPhone=str(input("Input Phone Number: "))
                if inputPhone=='0':
                    break
                if len(inputPhone) == 12 or len(inputPhone) == 13:
                    newUser.insert(2,str(inputPhone))
                    print(f'Phone Number: {inputPhone}')
                else:
                    print(f'Your input length is wrong, your length input is {len(inputPhone)}')
                    continue
                # input address
                inputAddress=str(input("Input Address: "))
                if inputAddress==0:
                    break
                newUser.insert(3,inputAddress)
                print(f'Address: {inputAddress} ')
                # input default status
                newUser.insert(1,'member')
                # input current user's tax
                inputTax=user[inputUserID][4]
                newUser.insert(4,inputTax)

                # Preview the edit result
                print("\n--------------------------------------------------\n")
                print(f'This is your current user detail\nName: {user[inputUserID][0]}\nPhone Number: {user[inputUserID][2]}\nAddress: {user[inputUserID][3]}')
                print("\n--------------------------------------------------\n")
                print(f'This is your new user detail\nName: {inputName}\nPhone Number: {inputPhone}\nAddress: {inputAddress}')
                print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                inputSave=int(input('Choose your option: '))

                while inputSave != 0:
                    if inputSave==1:
                        if (inputName!='' and inputAddress!='') and (type(inputName)==str and type(inputAddress==str and type(inputPhone)==str)):
                            user[inputUserID]=newUser
                            (f'{inputName} is Success')
                            print("\n--------------------------------------------------\n")
                            showAllUsers(user)
                            print("\n--------------------------------------------------\n")
                            break
                        else:
                            print("Wrong Input Cancelled to Save")
                            break
                    else:
                        pass

                    print("\n--------------------------------------------------\n")
                    print(f'This is your current user detail\nName: {user[inputUserID][0]}\nPhone Number: {user[inputUserID][2]}\nAddress: {user[inputUserID][3]}')
                    print("\n--------------------------------------------------\n")
                    print(f'This is your new user detail\nName: {inputName}\nPhone Number: {inputPhone}\nAddress: {inputAddress}')
                    print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                    inputSave=int(input('Choose your option: '))
                
            else:
                print("No user detected...")
                break
        else:
            pass

        print("\nEDIT USERS")
        print("Edit Users Menu")
        print("---Input 1 if you want to edit users")
        print("---Input 0 if you want to cancel")

        inputEditUsers=int(input("Do you want to edit user?: "))

# DELETE FUNCTION
# Delete A User Function
def deleteUsers(user):
    print("\nDELETE USERS")
    showAllUsers(user)
    print("\n--------------------------------------------------\n")

    print("Delete Users Menu")
    print("---Input 1 if you want to delete users")
    print("---Input 0 if you want to cancel")

    inputDeleteUsers=int(input("Do you want to delete user?: "))

    while inputDeleteUsers !=0:
        if inputDeleteUsers == 1:
            print("\n--------------------------------------------------\n")
            showAllUsers(user)
            print("\n--------------------------------------------------\n")
            print("Choose user to delete...")
            inputUserID=int(input("Input User ID you want to edit: "))
            # Check if ID exist
            if checkID(user,inputUserID) == True:
                print("User detected...")
                if user[inputUserID][4] == 0:
                    print("\n--------------------------------------------------\n")
                    print(f'This is your new user detail\nName: {user[inputUserID][0]}\nPhone Number: {user[inputUserID][2]}\nAddress: {user[inputUserID][3]}')
                    print('Do you want to delete?\n---Press 1 to delete\n---Press 0 to cancel')
                    inputDelete=int(input('Choose your option: '))

                    while inputDelete != 0:
                        if inputDelete==1:
                            if inputUserID != '':
                                (f'{user[inputUserID][0]} is Deleted')
                                del user[inputUserID]

                                showAllUsers(user)
                                break
                            else:
                                print("Wrong Input Cancelled to Save")
                                break
                        else:
                            pass

                        print("\n--------------------------------------------------\n")
                        print(f'This is your user detail\nName: {user[inputUserID][0]}\nPhone Number: {user[inputUserID][2]}\nAddress: {user[inputUserID][3]}')
                        print('Do you want to delete?\n---Press 1 to save\n---Press 0 to cancel')
                        inputDelete=int(input('Choose your option: '))
                else:
                    print("Can't delete user because user still have a tax to pay...")
                    break
            else:
                print("No user detected...")
                break
        else:
            pass

        print("\nDELETE USERS")
        showAllUsers(user)
        print("\n--------------------------------------------------\n")

        print("Delete Users Menu")
        print("---Input 1 if you want to delete users")
        print("---Input 0 if you want to cancel")

        inputDeleteUsers=int(input("Do you want to delete user?: "))
