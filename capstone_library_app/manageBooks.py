from libraryDict import *

# Displaying Book Categories
def displayCategories(book):
    print('\n\nCategories List :')
    print('No.' + '  | ' +'Categories   '+ '  |')
    index=0
    for cat in book.keys():
        index+=1
        print(str(index)+' '*(len('No.')-len(str(index)))+'  | '+cat+' ' *(len('Categories   ')-len(cat)) +'  |')

# Showing all books
def showAllBooks(book,categoryInput):
    print(f'\n\n{categoryInput} Books List :')
    print('No.' + '  | ' +'ISBN'+ '           |'+'Title                         '+ '  |'+'Author            '+ '  |'+'Year'+ '  |'+'Category     '+ '  |'+'Status   '+ '  |')
    index=0
    for b in book[categoryInput].keys():
        index+=1
        print(str(index)+' '*(len('No.')-len(str(index)))+'  | '+b+' ' *(len('ISBN')-len(b)) +'  |'+book[categoryInput][b][0]+' ' *(len('Title                         ')-len(book[categoryInput][b][0])) +'  |'
                +book[categoryInput][b][1]+' ' *(len('Author            ')-len(book[categoryInput][b][1])) +'  |'+book[categoryInput][b][2]+' ' *(len('Year')-len(book[categoryInput][b][2])) +'  |'
                +categoryInput+' ' *(len('Category     ')-len(categoryInput)) +'  |'+book[categoryInput][b][3]+' ' *(len('Status   ')-len(book[categoryInput][b][3])) +'  |')

# Showing Books based on avalaibility status
def showAvalaibleBooks(book,categoryInput,status):
    print(f'\n\n{categoryInput} Books List :')
    print('No.' + '  | ' +'ISBN'+ '           |'+'Title                         '+ '  |'+'Author            '+ '  |'+'Year'+ '  |'+'Category     '+ '  |'+'Status   '+ '  |')
    index=0
    for b in book[categoryInput].keys():
        if book[categoryInput][b][3] == status:
           index+=1
           print(str(index)+' '*(len('No.')-len(str(index)))+'  | '+b+' ' *(len('ISBN')-len(b)) +'  |'+book[categoryInput][b][0]+' ' *(len('Title                         ')-len(book[categoryInput][b][0])) +'  |'
                +book[categoryInput][b][1]+' ' *(len('Author            ')-len(book[categoryInput][b][1])) +'  |'+book[categoryInput][b][2]+' ' *(len('Year')-len(book[categoryInput][b][2])) +'  |'
                +categoryInput+' ' *(len('Category     ')-len(categoryInput)) +'  |'+book[categoryInput][b][3]+' ' *(len('Status   ')-len(book[categoryInput][b][3])) +'  |')
        else:
            continue

# READ FUNCTION
# Displaying books
def displayBooks(book):
    # Pick categories
    print("\nDISPLAY BOOKS")
    displayCategories(book)
    print("\nType 'x' to cancel\n")
    categoryInput=(input("Enter the name of category you want to display: "))
    
    while categoryInput!='x':
        for cat in book.keys():
            if categoryInput == cat:
                # Filtering display
                print("\nDISPLAY BOOKS")
                displayMenu(avalaibleMenu)
                inputAvalaible= int(input('Enter the number of menu you want to select: '))
                while inputAvalaible != 4:
                    if inputAvalaible ==1 : # display all books 
                        print("\n--------------------------------------------------\n")
                        showAllBooks(book, categoryInput)
                        print("\n--------------------------------------------------\n")
                              
                    elif inputAvalaible ==2: # display avalaible books
                        print("\n--------------------------------------------------\n")
                        showAvalaibleBooks(book,categoryInput,'avalaible')
                        print("\n--------------------------------------------------\n")
                        
                    elif inputAvalaible ==3: # Display rented books
                        print("\n--------------------------------------------------\n")
                        showAvalaibleBooks(book,categoryInput,'rented')
                        print("\n--------------------------------------------------\n")
                    else:
                        pass
                    

                    displayMenu(avalaibleMenu)
                    inputAvalaible= int(input('Enter the number of menu you want to select: '))
            else:
                pass
            
            print("\nDISPLAY BOOKS")
            displayCategories(book)
            print("\nType 'x' to cancel\n")
            categoryInput=(input("Enter the name of category you want to display: "))

# Check Categories Function
# To check if there are categories in list
def checkCategory(book, inputCategory):
    status=False
    for cat in book.keys():
        if inputCategory == cat:
            status= True
        else:
            continue
    return status

# Check ISBN Function
# To check if there are isbn in list
def checkISBN(book, inputISBN, inputCategory):
    status= False
    for isbn in book[inputCategory].keys():
        if isbn == inputISBN:
            status= True
        else:
            continue
    return status

# CREATE FUNCTION
# Add A Book Function
def addBooks(book):
    print("\nADDING BOOKS")
    # Make sure want to continue add books
    print("\nAdd Books Menu")
    print("---Input 1 if you want to add books")
    print("---Input 0 if you want to cancel")

    inputAddBooks=int(input("Do you want to add Book?: "))

    while inputAddBooks !=0:
        if inputAddBooks == 1:
            # Choosing book's category
            displayCategories(book)
            inputCategory=str(input("Enter Book's Category: "))
            if inputCategory == '0':
                break
            if checkCategory(book,inputCategory) == True:
                print("Category Exist, You Can Proceed to Insert Book...")
            else:
                print("Category Not Exist")
                continue
            print(f'Saving Book into {inputCategory}...\n')

            # list for new book
            newBook=[]

            # Input ISBN
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
                   if checkISBN(book,inputISBN,inputCategory) == False:
                      print("There is no same book detected...")
                   else:
                      print("You can't add same Book")
                      continue
            print(f'ISBN: {inputISBN}')
            # Input Title
            inputTitle=str(input("Input Book's Title: "))
            if inputTitle=='0':
                break
            newBook.insert(0,inputTitle)
            print(f'Title: {inputTitle}')
            # Input Author
            inputAuthor=str(input("Input Book's Author: "))
            if inputAuthor=='0':
                break
            newBook.insert(1,inputAuthor)
            print(f'Author: {inputAuthor}')
            # input Year released
            inputYear=int(input("Input Book's Released Year: "))
            if inputYear==0:
                break
            if type(inputYear) != int:
                print('Your input is wrong')
            else:
                inputYear=str(inputYear)
                if len(inputYear) != 4:
                    print("Your input length is wrong")
                else:
                    newBook.insert(2,inputYear)
            print(f'Year: {inputYear} ')
            # Input default avalaibility status
            newBook.append('avalaible')

            # Make sure u want to save it
            print(f'\nThis is your book detail\nISBN: {inputISBN}\nTitle: {inputTitle}\nAuthor: {inputAuthor}\nYear: {inputYear}')
            print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
            inputSave=int(input('Choose your option: '))

            while inputSave != 0:
                if inputSave==1:
                    if checkCategory(book,inputCategory)==True and (inputTitle!='' and inputAuthor!=''):
                        # Saving the book to dictionary
                        book[inputCategory][inputISBN]=newBook
                        (f'{inputTitle} on {inputCategory} is Success')
                        
                        print("\n--------------------------------------------------\n")
                        showAllBooks(book, inputCategory)
                        print("\n--------------------------------------------------\n")
                        break
                    else:
                        print("Wrong Input Cancelled to Save")
                        break
                else:
                    pass
                print(f'\nThis is your book detail\nISBN: {inputISBN}\nTitle: {inputTitle}\nAuthor: {inputAuthor}\nYear: {inputYear}')
                print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                inputSave=int(input('Choose your option: '))

        else:
            pass
        
        print("\nADDING BOOKS")
        print("\nAdd Books Menu")
        print("---Input 1 if you want to add books")
        print("---Input 0 if you want to cancel")
        inputAddBooks=int(input("Do you want to add Book?: "))

# UPDATE FUNCTION
# Edit A Book Function
def editBooks(book):
    print("\nEDIT BOOKS")
    # Make sure want to continue edit books
    print("\nEdit Books Menu")
    print("---Input 1 if you want to edit books")
    print("---Input 0 if you want to cancel")

    inputEditBooks=int(input("Do you want to edit Book?: "))

    while inputEditBooks !=0:
        if inputEditBooks == 1:
            # Choose book Categories
            showAllBooks(book,'fiction')
            showAllBooks(book,'non fiction')
            print("\n--------------------------------------------------\n")

            print("Choose book's category")
            displayCategories(book)
            inputCategory=str(input("Enter Book's Category: "))
            if inputCategory == '0':
                break
            if checkCategory(book,inputCategory) == True:
                print("Category Exist, You Can Proceed to Edit Book...")
            else:
                print("Category Not Exist")
                continue
            
            # create list for new book
            newBook=[]

            print(f'Choose avalaible book from {inputCategory} list here you want to edit...')
            print("\n--------------------------------------------------\n")
            showAvalaibleBooks(book,inputCategory,'avalaible')
            print("\n--------------------------------------------------\n")
            print("Choose your book with input book's ISBN")

            # Input ISBN
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
                      print("Book detected")
                   else:
                      print("There is no book detected")
                      continue
            print(f'ISBN: {inputISBN}')
            # Input Title
            inputTitle=str(input("Input Book's Title: "))
            if inputTitle=='0':
                break
            newBook.insert(0,inputTitle)
            print(f'Title: {inputTitle}')
            # Input Author
            inputAuthor=str(input("Input Book's Author: "))
            if inputAuthor=='0':
                break
            newBook.insert(1,inputAuthor)
            print(f'Author: {inputAuthor}')
            # Input Year
            inputYear=int(input("Input Book's Released Year: "))
            if inputYear==0:
                break
            if type(inputYear) != int:
                print('Your input is wrong')
            else:
                inputYear=str(inputYear)
                if len(inputYear) != 4:
                    print("Your input length is wrong")
                else:
                    newBook.insert(2,inputYear)
            print(f'Year: {inputYear} ')
            # Set default avalaibility status
            newBook.append('avalaible')

            print("\n--------------------------------------------------\n")
            print(f'This is your current book detail\nISBN: {inputISBN}\nTitle: {book[inputCategory][inputISBN][0]}\nAuthor: {book[inputCategory][inputISBN][1]}\nYear: {book[inputCategory][inputISBN][2]}')
            print("\n---------------------------------------\n")
            print(f'This is your new book detail\nISBN: {inputISBN}\nTitle: {inputTitle}\nAuthor: {inputAuthor}\nYear: {inputYear}')
            print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
            inputSave=int(input('Choose your option: '))

            while inputSave != 0:
                if inputSave==1:
                    # Check if book still avalaible or not
                    # if still rented cannot edit the book
                    if book[inputCategory][inputISBN][3]=='avalaible':
                        if checkCategory(book,inputCategory)==True and (inputTitle!='' and inputAuthor!=''):
                            book[inputCategory][inputISBN]=newBook
                            (f'{inputTitle} on {inputCategory} is Success')
                            print("\n--------------------------------------------------\n")
                            showAllBooks(book, inputCategory)
                            print("\n--------------------------------------------------\n")
                            break
                        else:
                            print("Wrong Input Cancelled to Save")
                            break
                    else:
                        print('Your book still rented, cannot edit...')
                        break
                else:
                    pass
                print("\n--------------------------------------------------\n")
                print(f'This is your current book detail\nISBN: {inputISBN}\nTitle: {book[inputCategory][inputISBN][0]}\nAuthor: {book[inputCategory][inputISBN][1]}\nYear: {book[inputCategory][inputISBN][2]}')
                print("\n---------------------------------------\n")
                print(f'This is your new book detail\nISBN: {inputISBN}\nTitle: {inputTitle}\nAuthor: {inputAuthor}\nYear: {inputYear}')
                print('Do you want to save?\n---Press 1 to save\n---Press 0 to cancel')
                inputSave=int(input('Choose your option: '))

        else:
            pass
        
        print("\nEDIT BOOKS")
        # Make sure want to continue edit books
        print("\nEdit Books Menu")
        print("---Input 1 if you want to edit books")
        print("---Input 0 if you want to cancel")

        inputEditBooks=int(input("Do you want to edit Book?: "))

# DELETE FUNCTION
# Delete a book function
def deleteBooks(book):
    print("\nDELETE BOOKS")
    print("\nDelete Books Menu")
    print("---Input 1 if you want to delete books")
    print("---Input 0 if you want to cancel")

    inputDeleteBooks=int(input("Do you want to delete Book?: "))

    while inputDeleteBooks !=0:
        if inputDeleteBooks == 1:
            # Choose book Categories
            showAllBooks(book,'fiction')
            showAllBooks(book,'non fiction')
            print("\n--------------------------------------------------\n")

            print("Choose book's category")
            # Input book's category
            displayCategories(book)
            inputCategory=str(input("Enter Book's Category: "))
            if inputCategory == '0':
                break
            if checkCategory(book,inputCategory) == True:
                print("Category Exist, You Can Proceed to Edit Book...")
            else:
                print("Category Not Exist")
                continue

            print(f'Choose avalaible book from {inputCategory} list here you want to edit...')
            print("\n--------------------------------------------------\n")
            showAvalaibleBooks(book,inputCategory,'avalaible')
            print("\n--------------------------------------------------\n")
            print("Choose your book with input book's ISBN")
            # input ISBN
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
                      print("Book detected")
                   else:
                      print("There is no book detected")
                      continue
            print(f'ISBN: {inputISBN}')

            # Make sure to want delete the book
            print("\n--------------------------------------------------\n")
            print(f'This is your book detail\nISBN: {inputISBN}\nTitle: {book[inputCategory][inputISBN][0]}\nAuthor: {book[inputCategory][inputISBN][1]}\nYear: {book[inputCategory][inputISBN][2]}')
            print('Do you want to delete?\n---Press 1 to delete\n---Press 0 to cancel')
            inputDelete=int(input('Choose your option: '))

            while inputDelete != 0:
                if inputDelete==1:
                    # Check if book to delete still avalaible or not
                    # If still rented, it cant delete the book
                    if book[inputCategory][inputISBN][3]=='avalaible':
                        if checkCategory(book,inputCategory)==True:
                            del book[inputCategory][inputISBN]
                            print("\n--------------------------------------------------\n")
                            showAllBooks(book, inputCategory)
                            print("\n--------------------------------------------------\n")
                            break
                        else:
                            print("Wrong Input Cancelled to Save")
                            break
                    else:
                        print('Your book still rented, cannot delete...')
                        break
                else:
                    pass
                print("\n--------------------------------------------------\n")
                print(f'This is your book detail\nISBN: {inputISBN}\nTitle: {book[inputCategory][inputISBN][0]}\nAuthor: {book[inputCategory][inputISBN][1]}\nYear: {book[inputCategory][inputISBN][2]}')
                print('Do you want to delete?\n---Press 1 to delete\n---Press 0 to cancel')
                inputDelete=int(input('Choose your option: '))

        else:
            pass
        
        print("\nDELETE BOOKS")
        print("\nDelete Books Menu")
        print("---Input 1 if you want to delete books")
        print("---Input 0 if you want to cancel")

        inputDeleteBooks=int(input("Do you want to delete Book?: "))
