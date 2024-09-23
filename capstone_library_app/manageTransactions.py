from libraryDict import *
from manageBooks import *
from manageUsers import *

# Showing all borrow transaction
def showAllBorrows(borrow):
    print('\nBorrow List :')
    print('ID' + '  | '+'Title                          ' + '  | ' +'Name          '+ '  |'+'Borrow Date   '+ '  |'+'Expected to Return Date   '+ '  |')
    for i in borrow.keys():
        print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+borrow[i][1]+' ' *(len('Title                          ')-len(borrow[i][1])) +'  |'+borrow[i][3]+' ' *(len('Name           ')-len(borrow[i][3])) +'  |'
              +str(borrow[i][4])+' ' *(len('Borrow Date   ')-len(str(borrow[i][4]))) +'  |'+str(borrow[i][5])+' ' *(len('Expected to Return Date   ')-len(str(borrow[i][5]))) +'  |')

# Showing all return transaction
def showAllReturns(returns):
    # sorting returns transaction by return status
    returnsByStatus = {k: v for k, v in sorted(returns.items(), key=lambda x: x[1][5] == 'late')}
    print('\nReturn List :')
    print('ID' + '  | '+'Title                          ' + '  | ' +'Name          '+ '  |'+'Return Date   '+ '  |'+'Return Status   '+ '  |'+'Tax Payment Status   '+ '  |')
    for i in returnsByStatus.keys():
        print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+returnsByStatus[i][1]+' ' *(len('Title                          ')-len(returnsByStatus[i][1])) +'  |'+returnsByStatus[i][3]+' ' *(len('Name           ')-len(returnsByStatus[i][3])) +'  |'
              +str(returnsByStatus[i][4])+' ' *(len('Return Date   ')-len(str(returnsByStatus[i][4]))) +'  |'+str(returnsByStatus[i][5])+' ' *(len('Return Status   ')-len(str(returnsByStatus[i][5]))) +'  |'
              +str(returnsByStatus[i][6])+' ' *(len('Tax Payment Status   ')-len(str(returnsByStatus[i][6]))) +'  |')
        
# Showing all ontime transaction
def showOntimeReturns(returns):
    print('\nReturn List :')
    print('ID' + '  | '+'Title                          ' + '  | ' +'Name          '+ '  |'+'Return Date   '+ '  |'+'Return Status   '+ '  |'+'Tax Payment Status   '+ '  |')
    for i in returns.keys():
        if returns[i][5]=='ontime':
            print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+returns[i][1]+' ' *(len('Title                          ')-len(returns[i][1])) +'  |'+returns[i][3]+' ' *(len('Name           ')-len(returns[i][3])) +'  |'
                +str(returns[i][4])+' ' *(len('Return Date   ')-len(str(returns[i][4]))) +'  |'+str(returns[i][5])+' ' *(len('Return Status   ')-len(str(returns[i][5]))) +'  |'
                +str(returns[i][6])+' ' *(len('Tax Payment Status   ')-len(str(returns[i][6]))) +'  |')
        else:
            continue

# Showing all late transaction
def showAllLateReturns(returns):
    print('\nReturn List :')
    print('ID' + '  | '+'Title                          ' + '  | ' +'Name          '+ '  |'+'Return Date   '+ '  |'+'Return Status   '+ '  |'+'Tax Payment Status   '+ '  |')
    for i in returns.keys():
        if returns[i][5] == 'late':
            print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+returns[i][1]+' ' *(len('Title                          ')-len(returns[i][1])) +'  |'+returns[i][3]+' ' *(len('Name           ')-len(returns[i][3])) +'  |'
                +str(returns[i][4])+' ' *(len('Return Date   ')-len(str(returns[i][4]))) +'  |'+str(returns[i][5])+' ' *(len('Return Status   ')-len(str(returns[i][5]))) +'  |'
                +str(returns[i][6])+' ' *(len('Tax Payment Status   ')-len(str(returns[i][6]))) +'  |')
        else:
            continue

# Showing all payed late transaction
def showPayedLateReturns(returns):
    print('\nReturn List :')
    print('ID' + '  | '+'Title                          ' + '  | ' +'Name          '+ '  |'+'Return Date   '+ '  |'+'Return Status   '+ '  |'+'Tax Payment Status   '+ '  |')
    for i in returns.keys():
        if returns[i][5] == 'late' and returns[i][6]=='payed':
            print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+returns[i][1]+' ' *(len('Title                          ')-len(returns[i][1])) +'  |'+returns[i][3]+' ' *(len('Name           ')-len(returns[i][3])) +'  |'
                +str(returns[i][4])+' ' *(len('Return Date   ')-len(str(returns[i][4]))) +'  |'+str(returns[i][5])+' ' *(len('Return Status   ')-len(str(returns[i][5]))) +'  |'
                +str(returns[i][6])+' ' *(len('Tax Payment Status   ')-len(str(returns[i][6]))) +'  |')
        else:
            continue
        
# Showing all not payed late transaction
def showNotPayedLateReturns(returns):
    print('\nReturn List :')
    print('ID' + '  | '+'Title                          ' + '  | ' +'Name          '+ '  |'+'Return Date   '+ '  |'+'Return Status   '+ '  |'+'Tax Payment Status   '+ '  |')
    for i in returns.keys():
        if returns[i][5] == 'late' and returns[i][6]=='not payed':
            print(str(i)+' '*(len('ID')-len(str(i)))+'  | '+returns[i][1]+' ' *(len('Title                          ')-len(returns[i][1])) +'  |'+returns[i][3]+' ' *(len('Name           ')-len(returns[i][3])) +'  |'
                +str(returns[i][4])+' ' *(len('Return Date   ')-len(str(returns[i][4]))) +'  |'+str(returns[i][5])+' ' *(len('Return Status   ')-len(str(returns[i][5]))) +'  |'
                +str(returns[i][6])+' ' *(len('Tax Payment Status   ')-len(str(returns[i][6]))) +'  |')
        else:
            continue

# READ FUNCTION
# Displaying Transaction
def displayTransactions(borrow,returns):
    print("\nDISPLAY TRANSACTION")
    print("Transaction Menu:")
    displayMenu(transactionMenu)
    #input the menu
    transactionInput = str(input("Enter the number of the menu you want to run: "))

    while transactionInput !='3' :
        if transactionInput =='1' : # display borrow transaction list
            print("\n--------------------------------------------------\n")
            showAllBorrows(borrow)
            print("\n--------------------------------------------------\n")
            
            print("Transaction Menu:")
            displayMenu(transactionMenu)
            #input the menu
            transactionInput = str(input("Enter the number of the menu you want to run: "))
        elif transactionInput =='2': # display return transaction list
            print("\nDISPLAY RETURN TRANSACTION")
            print("Return Transaction Menu:")
            displayMenu(returnMenu)
            #input the menu
            returnInput = str(input("Enter the number of the menu you want to run: "))

            while returnInput !='4' :
                    if returnInput =='1' : # display all return transaction list
                        print("\n--------------------------------------------------\n")
                        showAllReturns(returns) 
                        print("\n--------------------------------------------------\n")
                
                    elif returnInput =='2': # display On Time return transaction list
                        print("\n--------------------------------------------------\n")
                        showOntimeReturns(returns)
                        print("\n--------------------------------------------------\n")

                    elif returnInput =='3': # display late return transaction list
                        print("Late Return Transaction Menu:")
                        displayMenu(lateReturnMenu)
                        #input the menu
                        lateReturnInput = str(input("Enter the number of the menu you want to run: "))

                        while lateReturnInput != '4':
                            if lateReturnInput =='1' : # display all return transaction list
                                print("\n--------------------------------------------------\n")
                                showAllLateReturns(returns)
                                print("\n--------------------------------------------------\n") 
                        
                            elif lateReturnInput =='2': # display On Time return transaction list
                                print("\n--------------------------------------------------\n")
                                showNotPayedLateReturns(returns)
                                print("\n--------------------------------------------------\n")

                            elif lateReturnInput=='3':
                                print("\n--------------------------------------------------\n")
                                showPayedLateReturns(returns)
                                print("\n--------------------------------------------------\n")

                            else:
                                pass
                            
                            print("Late Return Transaction Menu:")
                            displayMenu(lateReturnMenu)
                            #input the menu
                            lateReturnInput = str(input("Enter the number of the menu you want to run: "))

                    else :
                        pass
                    
                    print("Borrow Transaction Menu:")
                    displayMenu(returnMenu)
                    #input the menu
                    returnInput = str(input("Enter the number of the menu you want to run: "))

        else :
           pass
    
        print("\nDISPLAY TRANSACTION")
        print("Transaction Menu:")
        displayMenu(transactionMenu)
        #input the menu
        transactionInput = str(input("Enter the number of the menu you want to run: ")) 

# CREATE FUNCTION
# ADD A Transactions
def addTransactions(borrow,returns,user,book):
    print("\nADD TRANSACTIONS")
    print("Transaction Menu:")
    displayMenu(transactionMenu)
    #input the menu
    transactionInput = str(input("Enter the number of the menu you want to run: "))

    while transactionInput !='3' :
        if transactionInput =='1' : # display borrow transaction list
            print("\nADD BORROW TRANSACTIONS")
            print("\n--------------------------------------------------\n")
            showAllBorrows(borrow)
            print("\n--------------------------------------------------\n")
            # Make sure to continue add borrow transaction
            print("\nAdd Borrow Transaction Menu")
            print("---Input 1 if you want to add borrow transaction")
            print("---Input 0 if you want to cancel\n")

            inputAddBorrows=str(input("Do you want to add new transaction?: "))

            while inputAddBorrows !='0':
                if inputAddBorrows == '1':
                    # new borrow list
                    newBorrow=[]
                    # display categories
                    print("\n--------------------------------------------------\n")
                    displayCategories(book)
                    print("\n--------------------------------------------------\n")
                    print("Choose book's category...")
                    inputCategory=str(input("Type your book's category: "))
                    if inputCategory=='0':
                        break
                    if checkCategory(book,inputCategory) == False:
                        print('\nNo Category Detected, please type the category correctly...')
                        break
                    # display books
                    print("\n--------------------------------------------------\n")
                    showAvalaibleBooks(book,inputCategory,'avalaible')
                    print("\n--------------------------------------------------\n")
                    print('Choose book you want to insert by the ISBN...')                  
                    # input isbn
                    inputISBN=int(input("Input Book's ISBN: "))
                    if inputISBN==0:
                        break
                    if type(inputISBN) != int:
                        print('Your input is wrong')
                        continue
                    else:
                        inputISBN=str(inputISBN)
                        if len(inputISBN) != 13:
                            print(f"Your input length is wrong, your input length is {len(inputISBN)}")
                            continue
                        else:
                            if checkISBN(book,inputISBN,inputCategory) == True:
                                print("There is no book detected...")
                            else:
                                print("Book detected...")
                                continue
                    # input title based on isbn
                    inputTitle=''
                    for b in book[inputCategory].keys():
                        if b == inputISBN:
                            inputTitle=book[inputCategory][inputISBN][0]
                        else:
                            continue
                    print(f'Title: {inputTitle}')
                    # save isbn and title to new list
                    newBorrow.insert(0,inputISBN)
                    newBorrow.insert(1,inputTitle)

                    # display user
                    print("\n--------------------------------------------------\n")
                    showAllUsers(user)
                    print("\n--------------------------------------------------\n")
                    print('Choose user you want to insert by the ID...')
                    # Input user id
                    inputUserID=int(input("Input User's ID: "))
                    if inputUserID==0:
                        break
                    # input name based on user id
                    inputName=''
                    for u in user.keys():
                        if u == inputUserID:
                            inputName=user[u][0]
                        else:
                            continue
                    print(f'Name: {inputName}')
                    # save id and name to new list
                    newBorrow.insert(2,inputUserID)
                    newBorrow.insert(3,inputName)
                    # input today's date for borrow date
                    inputBorrowDateTransaction=date.today()
                    if inputBorrowDateTransaction==0:
                        break
                    newBorrow.insert(4,inputBorrowDateTransaction)

                    inputExpectedReturn=inputBorrowDateTransaction+datetime.timedelta(days=3)
                    newBorrow.insert(5,inputExpectedReturn)

                    print("\n--------------------------------------------------\n")                    
                    print(f'\n\nThis is your new transaction detail\nBook Title: {inputTitle}\nName: {inputName}\nBorrow Date: {inputBorrowDateTransaction}\nExpected Return on: {inputExpectedReturn}')
                    print("\n--------------------------------------------------\n")

                    print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                    inputSave=str(input('Choose your option: '))

                    while inputSave != '0':
                        if inputSave=='1':
                            if user[inputUserID][4]==0:
                                inputBorrowID=increment(borrow)
                                if (inputISBN !='' and inputUserID !='' and inputBorrowDateTransaction !=''):
                                    borrow[inputBorrowID]=newBorrow
                                    (f'{inputName} borrowing {inputTitle} is Success...')
                                    book[inputCategory][inputISBN][3]='rented'
                                    print(f"{book[inputCategory][inputISBN][0]} status set to {book[inputCategory][inputISBN][3]}")

                                    print("\n--------------------------------------------------\n")
                                    showAllBorrows(borrow)
                                    print("\n--------------------------------------------------\n")
                                    break
                                else:
                                    print("Wrong Input Cancelled to Save")
                                    break
                            elif user[inputUserID][4]>0:
                                print("User must pay tax to borrow another book...")
                                break
                            else:
                                print("Wrong input")
                                break
                        else:
                            pass

                        print("\n--------------------------------------------------\n")                    
                        print(f'\n\nThis is your new transaction detail\nBook Title: {inputTitle}\nName: {inputName}\nBorrow Date: {inputBorrowDateTransaction}\nExpected Return on: {inputExpectedReturn}')
                        print("\n--------------------------------------------------\n")

                        print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                        inputSave=str(input('Choose your option: '))

                else:
                    pass
                
                print("\nAdd Borrow Transaction Menu")
                print("Input 1 if you want to add borrow transaction\n")
                print("Input 0 if you want to cancel\n")

                inputAddBorrows=str(input("Do you want to add new transaction?: "))
            
        elif transactionInput =='2': # display return transaction list
            # show borrow list
            print("\n--------------------------------------------------\n")
            showAllBorrows(borrow)
            print("\n--------------------------------------------------\n")

            print("\nAdd Return Transaction Menu")
            print("---Input 1 if you want to add return transaction")
            print("---Input 0 if you want to cancel")

            inputAddReturns=str(input("Do you want to add new transaction?: "))

            while inputAddReturns !='0':
                if inputAddReturns == '1':
                    # new return list
                    newReturn=[]

                    # input category
                    print("\n--------------------------------------------------\n")
                    displayCategories(book)
                    print("\n--------------------------------------------------\n")
                    inputCategory=str(input("Type your book's category: "))
                    if inputCategory=='0':
                        break
                    if checkCategory(book,inputCategory) == False:
                        print('\nNo Category Detected, please type the category correctly...')
                        break
                    # Input borrow id
                    print("\n--------------------------------------------------\n")
                    showAllBorrows(borrow)
                    showAvalaibleBooks(book,inputCategory,'rented')
                    print("\n--------------------------------------------------\n")

                    print("Choose borrow transaction")
                    inputBorrowID=int(input("Input Borrow ID: "))
                   
                    # input isbn
                    inputISBN=borrow[inputBorrowID][0]
                    print(f"ISBN: {inputISBN}")
                    newReturn.insert(0,inputISBN)
                    # input title
                    inputTitle=borrow[inputBorrowID][1]
                    print(f"Title: {inputTitle}")
                    newReturn.insert(1,inputTitle)
                    # input user id
                    inputUserID=borrow[inputBorrowID][2]
                    print(f"User ID: {inputUserID}")
                    newReturn.insert(2,inputUserID)
                    # input name
                    inputName=borrow[inputBorrowID][3]
                    print(f"Name: {inputName}")
                    newReturn.insert(3,inputName)
                    # input expected date
                    expectedDate=borrow[inputBorrowID][5]     

                    # input date
                    inputDateTransaction=date.today()
                    if inputDateTransaction==0:
                        break
                    diffDate=abs(expectedDate-inputDateTransaction).days
                    # Check late or ontime return transaction
                    if diffDate > 3:
                        inputStatus='late'
                        inputTaxStatus='not payed'
                        print(f'Expected return on: {expectedDate}\nReturn Date: {inputDateTransaction}\nReturn Status: {inputStatus} and {inputTaxStatus}')
                        newReturn.insert(4,inputDateTransaction)
                    else:
                        inputStatus='ontime'
                        inputTaxStatus='-'
                        print(f'Expected return on: {expectedDate}\nReturn Date: {inputDateTransaction}\nReturn Status: {inputStatus}')
                        newReturn.insert(4,inputDateTransaction)
                    # input status
                    newReturn.insert(5,inputStatus)
                    newReturn.insert(6,inputTaxStatus)

                    print("\n--------------------------------------------------\n")
                    print(f'\nThis is your new transaction detail\nBook Title: {inputTitle}\nName: {inputName}\nDate: {inputDateTransaction}\nReturn Status: {inputStatus}')
                    print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                    inputSave=str(input('Choose your option: '))

                    while inputSave != '0':
                        if inputSave=='1':
                            inputReturnID=increment(returns)
                            if (inputISBN !='' and inputUserID !='' and inputDateTransaction !=''):
                                returns[inputReturnID]=newReturn
                                (f'{inputName} borrowing {inputTitle} is Success...')
                                # change book status to avalaible
                                book[inputCategory][inputISBN][3]='avalaible'
                                print(f"{book[inputCategory][inputISBN][0]} status set to {book[inputCategory][inputISBN][3]}")
                                # adding tax to user who have late status
                                if inputStatus=='late':
                                    inputTax=(diffDate//3)*10000
                                    user[inputUserID][4]+=inputTax
                                    print(f"{inputName} tax now is: {user[inputUserID][4]}")
                                else:
                                    print(f"No tax...")
                                # Removing borrow transaction cause its done
                                print(f"{borrow[inputBorrowID]} borrow transactions is removed...")
                                del borrow[inputBorrowID]

                                print("\n--------------------------------------------------\n")
                                showAllReturns(returns)
                                print("\n--------------------------------------------------\n")
                                break
                            else:
                                print("Wrong Input Cancelled to Save")
                                break
                        else:
                            pass

                        print("\n--------------------------------------------------\n")
                        print(f'\nThis is your new transaction detail\nBook Title: {inputTitle}\nName: {inputName}\nDate: {inputDateTransaction}\nReturn Status: {inputStatus}')
                        print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                        inputSave=str(input('Choose your option: '))

                else:
                    pass
                # show borrow list
                print("\n--------------------------------------------------\n")
                showAllBorrows(borrow)
                print("\n--------------------------------------------------\n")
                print("\nAdd Return Transaction Menu")
                print("Input 1 if you want to add return transaction\n")
                print("Input 0 if you want to cancel\n")

                inputAddReturns=str(input("Do you want to add new transaction?: "))

        else :
            pass
        
        print("\nADD TRANSACTIONS")
        print("Transaction Menu:")
        displayMenu(transactionMenu)
        #input the menu
        transactionInput = str(input("Enter the number of the menu you want to run: "))

# UPDATE FUNCTION
# Edit Borrow Transaction
def editTransactions(borrow,user,book):
    print("\nEDIT BORROW TRANSACTIONS")
    print("\n--------------------------------------------------\n")
    showAllBorrows(borrow)
    print("\n--------------------------------------------------\n")
    # Make sure to continue add borrow transaction
    print("\nEdit Borrow Transaction Menu")
    print("---Input 1 if you want to edit borrow transaction")
    print("---Input 0 if you want to cancel\n")

    inputAddBorrows=str(input("Do you want to add new transaction?: "))

    while inputAddBorrows !='0':
        if inputAddBorrows == '1':
            
            # input borrow id
            print("\n--------------------------------------------------\n")
            showAllBorrows(borrow)
            print("\n--------------------------------------------------\n")
            inputBorrowID=int(input("Input transaction ID: "))

            if checkID(borrow,inputBorrowID) == True:

                # new borrow list
                newBorrow=[]
                # display categories
                print("\n--------------------------------------------------\n")    
                showAvalaibleBooks(book,'fiction','rented')
                showAvalaibleBooks(book,'non fiction','rented')
                print("\n--------------------------------------------------\n")  
                print("Choose book's category...")
                inputCategory=str(input("Type your book's category: "))
                if inputCategory=='0':
                    break
                if checkCategory(book,inputCategory) == False:
                    print('\nNo Category Detected, please type the category correctly...')
                    break
                # set current borrowed book status to avalaible first
                currentISBN=borrow[inputBorrowID][0]
                if checkISBN(book,currentISBN,inputCategory) == False:
                    print("Wrong input...")
                    break
                book[inputCategory][currentISBN][3]='avalaible'

                # display books
                print("\n--------------------------------------------------\n")
                showAvalaibleBooks(book,inputCategory,'avalaible')
                print("\n--------------------------------------------------\n")
                print('Choose book you want to insert by the ISBN...')                  
                # input isbn
                inputISBN=int(input("Input Book's ISBN: "))
                if inputISBN==0:
                    break
                if type(inputISBN) != int:
                    print('Your input is wrong')
                    continue
                else:
                    inputISBN=str(inputISBN)
                    if len(inputISBN) != 13:
                        print(f"Your input length is wrong, your input length is {len(inputISBN)}")
                        continue
                    else:
                        if checkISBN(book,inputISBN,inputCategory) == True:
                            print("You can proceed...")
                        else:
                            print("Book detected...")
                            continue
                        # input title based on isbn
                    inputTitle=''
                    for b in book[inputCategory].keys():
                        if b == inputISBN:
                            inputTitle=book[inputCategory][inputISBN][0]
                        else:
                            continue
                    print(f'Title: {inputTitle}')
                    # save isbn and title to new list
                    newBorrow.insert(0,inputISBN)
                    newBorrow.insert(1,inputTitle)

                    # display user
                    print("\n--------------------------------------------------\n")
                    showAllUsers(user)
                    print("\n--------------------------------------------------\n")
                    print('Choose user you want to insert by the ID...')
                    # Input user id
                    inputUserID=int(input("Input User's ID: "))
                    if inputUserID==0:
                        break
                    # input name based on user id
                    inputName=''
                    for u in user.keys():
                        if u == inputUserID:
                            inputName=user[u][0]
                        else:
                            continue
                    print(f'Name: {inputName}')
                    # save id and name to new list
                    newBorrow.insert(2,inputUserID)
                    newBorrow.insert(3,inputName)
                    # input today's date for borrow date
                    inputBorrowDateTransaction=borrow[inputBorrowID][4]
                    if inputBorrowDateTransaction==0:
                        break
                    newBorrow.insert(4,inputBorrowDateTransaction)

                    inputExpectedReturn=inputBorrowDateTransaction+datetime.timedelta(days=3)
                    newBorrow.insert(5,inputExpectedReturn)

                    print("\n--------------------------------------------------\n")                    
                    print(f'\n\nThis is your current transaction detail\nBook Title: {borrow[inputBorrowID][1]}\nName: {borrow[inputBorrowID][3]}\nBorrow Date: {borrow[inputBorrowID][4]}\nExpected Return on: {borrow[inputBorrowID][5]}')
                    print("\n--------------------------------------------------\n")                    
                    print(f'\n\nThis is your new transaction detail\nBook Title: {inputTitle}\nName: {inputName}\nBorrow Date: {inputBorrowDateTransaction}\nExpected Return on: {inputExpectedReturn}')
                    print("\n--------------------------------------------------\n")

                    print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                    inputSave=str(input('Choose your option: '))

                    while inputSave != '0':
                        if inputSave=='1':
                            if user[inputUserID][4]==0:
                                
                                if (inputISBN !='' and inputUserID !='' and inputBorrowDateTransaction !=''):
                                    borrow[inputBorrowID]=newBorrow
                                    (f'{inputName} borrowing {inputTitle} is Success...')
                                    book[inputCategory][inputISBN][3]='rented'
                                    print(f"{book[inputCategory][inputISBN][0]} status set to {book[inputCategory][inputISBN][3]}")

                                    print("\n--------------------------------------------------\n")
                                    showAllBorrows(borrow)
                                    print("\n--------------------------------------------------\n")
                                    break
                                else:
                                    print("Wrong Input Cancelled to Save")
                                    break
                            elif user[inputUserID][4]>0:
                                print("User must pay tax to borrow another book...")
                                break
                            else:
                                print("Wrong input")
                                break
                        else:
                            pass

                        print("\n--------------------------------------------------\n")                    
                        print(f'\n\nThis is your current transaction detail\nBook Title: {borrow[inputBorrowID][1]}\nName: {borrow[inputBorrowID][3]}\nBorrow Date: {borrow[inputBorrowID][4]}\nExpected Return on: {borrow[inputBorrowID][5]}')                    
                        print("\n--------------------------------------------------\n")                    
                        print(f'\n\nThis is your new transaction detail\nBook Title: {inputTitle}\nName: {inputName}\nBorrow Date: {inputBorrowDateTransaction}\nExpected Return on: {inputExpectedReturn}')
                        print("\n--------------------------------------------------\n")

                        print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                        inputSave=str(input('Choose your option: '))


            else:
                print("No Transaction Detected...")
                break
        else:
            pass
                
        print("\nEDIT BORROW TRANSACTIONS")
        print("\n--------------------------------------------------\n")
        showAllBorrows(borrow)
        print("\n--------------------------------------------------\n")
        # Make sure to continue add borrow transaction
        print("\nEdit Borrow Transaction Menu")
        print("---Input 1 if you want to edit borrow transaction")
        print("---Input 0 if you want to cancel\n")

        inputAddBorrows=str(input("Do you want to add new transaction?: "))

def deleteTransactions(borrow,returns,user,book):
    print("\nDELETE TRANSACTION")
    print("Transaction Menu:")
    displayMenu(transactionMenu)
    #input the menu
    transactionInput = str(input("Enter the number of the menu you want to run: "))

    while transactionInput !='3' :
        if transactionInput =='1' : # display borrow transaction list
            print("\n--------------------------------------------------\n")
            showAllBorrows(borrow)
            print("\n--------------------------------------------------\n")         

            print("\nDelete Borrow Transaction Menu")
            print("---Input 1 if you want to delete borrow transaction")
            print("---Input 0 if you want to cancel")

            inputDeleteBorrows=str(input("Do you want to delete transaction?: "))

            while inputDeleteBorrows !='0':
                if inputDeleteBorrows == '1':
                    print("\n--------------------------------------------------\n")  
                    showAllBorrows(borrow)
                    print("\n--------------------------------------------------\n")  
                    print("Choose transaction...")
                    inputBorrowID=int(input("Input transaction ID: "))
                    
                    if checkID(borrow,inputBorrowID) == True:
                        
                        print("\n--------------------------------------------------\n")    
                        showAvalaibleBooks(book,'fiction','rented')
                        showAvalaibleBooks(book,'non fiction','rented')
                        print("\n--------------------------------------------------\n")    
                        print("Choose book's category...")
                        inputCategory=str(input("Type your book's category: "))
                        if inputCategory=='0':
                            break
                        if checkCategory(book,inputCategory) == False:
                            print('\nNo Category Detected, please type the category correctly...')
                            break
                        # set current book status to avalaible
                        currentBookISBN=borrow[inputBorrowID][0]
                        if checkISBN(book,currentBookISBN,inputCategory) == False:
                            print('\nNo ISBN Detected, please type the category correctly...')
                            break
                        book[inputCategory][currentBookISBN][3]='avalaible'

                        print("\n--------------------------------------------------\n")
                        print(f'\nThis is your transaction detail\nBook Title: {borrow[inputBorrowID][1]}\nName: {borrow[inputBorrowID][3]}\nBorrow Date: {borrow[inputBorrowID][4]}')
                        print('Do you want to delete?\n---Press 1 to delete\n---Press 0 to cancel')
                        inputDelete=str(input('Choose your option: '))

                        while inputDelete != '0':
                            if inputDelete=='1':
                                if (inputBorrowID !=''):
                                    (f'{borrow[inputBorrowID][3]} borrowing {borrow[inputBorrowID][1]} is deleted...')
                                    del borrow[inputBorrowID]

                                    print(f"{book[inputCategory][currentBookISBN][0]} status set to {book[inputCategory][currentBookISBN][3]}")
                                    print("\n--------------------------------------------------\n") 
                                    showAllBorrows(borrow)
                                    print("\n--------------------------------------------------\n") 
                                    break
                                else:
                                    print("Wrong Input Cancelled to Save")
                                    break
                            else:
                                pass

                            print("\n--------------------------------------------------\n")
                            print(f'\nThis is your transaction detail\nBook Title: {borrow[inputBorrowID][1]}\nName: {borrow[inputBorrowID][3]}\nBorrow Date: {borrow[inputBorrowID][4]}')
                            print('Do you want to delete?\n---Press 1 to delete\n---Press 0 to cancel')
                            inputDelete=str(input('Choose your option: '))
                    else:
                        print('No transaction detected...')
                        break

                else:
                    pass
                
            print("\nDelete Borrow Transaction Menu")
            print("---Input 1 if you want to delete borrow transaction\n")
            print("---Input 0 if you want to cancel\n")

            inputDeleteBorrows=str(input("Do you want to delete transaction?: "))
            
        elif transactionInput =='2': # display return transaction list
            
            print("\n--------------------------------------------------\n")
            showAllReturns(returns)
            print("\n--------------------------------------------------\n")
            print("\nDelete Return Transaction Menu")
            print("---Input 1 if you want to Delete return transaction")
            print("---Input 0 if you want to cancel")

            inputDeleteReturns=str(input("Do you want to delete transaction?: "))

            while inputDeleteReturns !='0':
                if inputDeleteReturns == '1':
                    print("\n--------------------------------------------------\n")
                    showAllReturns(returns)
                    print("\n--------------------------------------------------\n")
                    inputReturnID=int(input("Input Transaction ID: "))

                    if checkID(returns, inputReturnID)==True and returns[inputReturnID][6]!='not payed':
                        
                        print("\n--------------------------------------------------\n")    
                        showAvalaibleBooks(book,'fiction','avalaible')
                        showAvalaibleBooks(book,'non fiction','avalaible')
                        print("\n--------------------------------------------------\n")
                        print("Choose book's category...")
                        inputCategory=str(input("Type your book's category: "))
                        if inputCategory=='0':
                            break
                        if checkCategory(book,inputCategory) == False:
                            print('\nNo Category Detected, please type the category correctly...')
                            break
                        # set current book status to avalaible
                        currentBookISBN=returns[inputReturnID][0]
                        if checkISBN(book,currentBookISBN,inputCategory) == False:
                            print('\nNo ISBN Detected, please type the category correctly...')
                            break
                        book[inputCategory][currentBookISBN][3]='rented'
                        
                        print("\n--------------------------------------------------\n")
                        print(f'\n\nThis is your transaction detail\nBook Title: {returns[inputReturnID][1]}\nName: {returns[inputReturnID][3]}\nDate: {returns[inputReturnID][4]}')
                        print('Do you want to delete?\n---Press 1 to delete\n---Press 0 to cancel')
                        inputDelete=str(input('Choose your option: '))

                        while inputDelete != '0':
                            if inputDelete=='1':
                                if (inputReturnID!=''):
                                    print(f'{returns[inputReturnID][3]} borrowing {returns[inputReturnID][1]} is Success...')
                                    del returns[inputReturnID]
                                    print("\n--------------------------------------------------\n")
                                    showAllReturns(returns)
                                    print("\n--------------------------------------------------\n")
                                    break
                                else:
                                    print("Wrong Input Cancelled to Save")
                                    break
                            else:
                                pass
                            print(f'\n\nThis is your transaction detail\nBook Title: {returns[inputReturnID][1]}\nName: {returns[inputReturnID][3]}\nDate: {returns[inputReturnID][4]}')
                            print('Do you want to delete?\n---Press 1 to delete\n---Press 0 to cancel')
                            inputDelete=str(input('Choose your option: '))

                    elif returns[inputReturnID][6]=='not payed':
                        print('Transaction is still not payed...')
                        break
                    else:
                        print('No transaction detected...')
                        break
                   
                else:
                    pass
                
                print("\n--------------------------------------------------\n")
                showAllReturns(returns)
                print("\n--------------------------------------------------\n")
                print("\nDelete Return Transaction Menu")
                print("---Input 1 if you want to Delete return transaction")
                print("---Input 0 if you want to cancel")

                inputDeleteReturns=str(input("Do you want to delete transaction?: "))

        else :
            pass
    
        print("\nDELETE TRANSACTION")
        print("Transaction Menu:")
        displayMenu(transactionMenu)
        #input the menu
        transactionInput = str(input("Enter the number of the menu you want to run: "))

