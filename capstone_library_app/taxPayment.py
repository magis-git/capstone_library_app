from libraryDict import *
from manageBooks import *
from manageUsers import *
from manageTransactions import *

# Function to pay tax
def taxpayment(user,returns):
    showNotPayedLateReturns(returns)
    print("\n--------------------------------------------------\n")
    print("\nTax Payment Menu:")
    print("---Press 1 to choose user for payment\n---Press 0 to cancel payment")

    inputMenu=str(input("Enter number: "))

    while inputMenu != '0':
        if inputMenu =='1':
            showTaxUsers(user)
            print("\n--------------------------------------------------\n")
            print("Choose user for the tax payment by ID...")

            inputUserID=int(input("Input user ID: "))

            userName=user[inputUserID][0]
            userTax=user[inputUserID][4]
            
            if checkID(user,inputUserID) == True:
                    
                print(f"Name: {userName}\nTotal tax payment: {userTax}")
                print('\nIs this user u want to proceed?\n---Press 1 to continue payment\n---Press 0 to cancel')
                inputTaxMenu=str(input('Enter the number of the menu you want to run: '))

                while inputTaxMenu != '0':
                    if inputTaxMenu == '1':
                        print(f"Name: {userName}\nTotal tax payment: {userTax}")
                        print("Please input your amount of money...")
                        inputMoney=int(input('Input money: '))

                        if inputMoney>0 and type(inputMoney)!=str:
                            moneyDifference= abs(inputMoney-userTax)

                            if inputMoney < userTax:
                                print(f"Your money is {moneyDifference} less from the tax...")
                                continue
                            elif inputMoney > userTax:
                                print(f"Here is your change: {moneyDifference}")
                                user[inputUserID][4]=0
                                for ret in returns.keys():
                                    if returns[ret][2]==inputUserID:
                                        returns[ret][6]='payed'
                                    else:
                                        continue
                                
                                break
                            elif inputMoney == userTax:
                                print("Payment Complete...")
                                user[inputUserID][4]=0
                                for ret in returns.keys():
                                    if returns[ret][2]==inputUserID:
                                        returns[ret][6]='payed'
                                    else:
                                        continue

                                break
                            else:
                                print("Wrong Input")
                                break
                        else:
                            print("Wrong Input")
                            break
                    else:
                        pass

                    print(f"Name: {userName}\nTotal tax payment: {userTax}")
                    print('\nIs this user u want to proceed?\n---Press 1 to continue payment\n---Press 0 to cancel')
                    inputTaxMenu=str(input('Enter the number of the menu you want to run: '))
            else:
                print('No User Detected')
                break
        else:
            pass
        
        showNotPayedLateReturns(returns)
        print("\n--------------------------------------------------\n")
        print("\nTax Payment Menu:")
        print("---Press 1 to choose user for payment\n---Press 0 to cancel payment")

        inputMenu=str(input("Enter number: "))

