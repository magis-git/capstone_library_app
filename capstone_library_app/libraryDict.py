import datetime
from datetime import date

# Book Data
# category
# -> isbn (primary Key)-> title, author, year(released), avalaibility status
book={
    "fiction":{
        '9786022918172': ['Perawan Bukan Maria','Feby Indirani','2021','avalaible'],
        '9786024410209': ['Dunia Shopie', 'Jonstein Gardner', '2023','avalaible'],
        '9786024246945': ['Laut Bercerita', 'Leila S. Chudori', '2017', 'rented'],
        '9786020523316': ['Melangkah', 'JS Khairen', '2020','avalaible'],
        '9786020658049': ['Home sweet Loan', 'Almira Bastari', '2022','rented'],
        '9786235953403': ['Sincerpity', 'Almira Bastari', '2022','avalaible'],
        '9786235266312': ['Lofarsa', 'Rofeena', '2023','avalaible'],
        '9786022203018': ['Merebah Riuh', 'Sacessahi', '2019','avalaible'],
        '9786022506829': ['Sabariah', 'Buya Hamka', '2020','avalaible'],
        '9786025406003': ['The Black Shadow', 'Angel El Cherid', '2017','avalaible'],
    },
    "non fiction":{
        '9789799107503': ['Memorizing Like an Elephant', 'Yudi Lesmana', '2015', 'avalaible'],
        '9786020217444': ['WHY:Perang Dunia I dan II', 'Grimnamu','2010','rented'],
        '9786020667188': ['Atomic Habits', 'James Clear','2023','avalaible'],
        '9786020380407': ['Prinsip Pareto', 'Richard Cho','2020','avalaible'],
        '9786239989262': ['Rahasia Sukses Membangun Bisnis', 'Alvin Paradipratya','2023','avalaible'],
        '9786029992175': ['Mukjizat Kartu Kredit', 'Imam Wibowo','2016','avalaible'],
        '9786230404306': ['Bicara Itu Ada Seninya', 'Oh Su Hyang','2021','avalaible'],
        '9786232167995': ['Komunikasi itu ada seninya', 'Oh Su Hyang','2020','avalaible'],
        '9786232444652': ['Seni Berbahagia', 'Ardhina','2020','avalaible'],
        '9786230029257': ['Better Me', 'Anna Silvia','2021','rented'],
    },
}

# User Data
# user id(primary key) -> name, status, phone number, address, tax count
user={
    1:['gigi','member','0819837462902','beaver road', 0],
    2:['cici','member','0813928740912','automaton road', 10000],
    3:['raora','member','062813555161','beegcatto road', 0],
    4:['erb','member','0928734483123','blood road', 30000],
    5:['amelia','member','0828224093128','baker st', 0],
    6:['anya','member','0828114097188','little sword st', 0],
    7:['ollie','member','0813124777118','humanlesst st', 0],
    8:['ayunda','member','0828424022215','little javanese st', 0],
    9:['honda','member','0810217697216','little sword st', 0],
    10:['subaru','member','0826113495191','little javanese st', 0],
}

# Borrow Transaction Data
# transaction id (primary key) -> isbn, title, user id, user name, borrow date, expected return date, transaction status
borrowTransaction={
    1:['9786020217444','WHY:Perang Dunia I dan II',1,'gigi',datetime.date(2024,9,5),datetime.date(2024,9,8)],
    2:['9786024246945','Laut Bercerita',3,'raora',datetime.date(2024,9,11),datetime.date(2024,9,14)],
    3:['9786230029257','Better Me',5,'amelia',datetime.date(2024,9,16),datetime.date(2024,9,19)],
    4:['9786020658049','Home sweet Loan',10,'subaru',datetime.date(2024,9,20),datetime.date(2024,9,23)],
    5:['9786230404306','Bicara Itu Ada Seninya',7,'ollie',datetime.date(2024,9,21),datetime.date(2024,9,24)]
}

# Return Transaction Data
# transaction id (primary key) -> isbn, title, user id, user name, return date, transaction status, tax payment status
returnTransaction={
    1:['9789799107503','Memorizing Like an Elephant',2,'cici',datetime.date(2024,9,20),'late','not payed'],
    2:['9786020667188','Atomic Habits',4,'erb',datetime.date(2024,9,11),'late','not payed'],
    3:['9786024410209','Dunia Shopie',6,'anya',datetime.date(2024,9,19),'ontime','-'],
    4:['9786020380407','Prinsip Pareto',8,'ayunda',datetime.date(2024,9,10),'late','payed'],
    5:['9786232444652','Seni Berbahagia',9,'honda',datetime.date(2024,9,14),'late','payed'],
    6:['9786235953403','Sincerpity',7,'ollie',datetime.date(2024,9,21),'ontime','-'],
    7:['9786022203018','Merebah Riuh',10,'subaru',datetime.date(2024,9,20),'ontime','-']
}

# List Menu Option
mainMenu=['Display Library Data', 'Add Library Data', 'Update Library Data', 'Remove Library Data', 'Tax Payment', 'Exit Program']
displayOptionMenu=['Display Books', 'Display Users', 'Display Transaction', 'Return to Main Menu']
addOptionMenu=['Add New Books', 'Add New Users', 'Add New Transaction', 'Return to Main Menu']
editOptionMenu=['Edit Books', 'Edit Users', 'Edit Transaction', 'Return to Main Menu']
deleteOptionMenu=['Delete Books', 'Delete Users', 'Delete Transaction', 'Return to Main Menu']
taxOptionMenu=['Pay Tax', 'Return to Main Menu']

avalaibleMenu=['All Books','Avalaible Books', 'Rented Books', 'Back to Category Menu']
userMenu=['All User','User Free Tax','User with tax','Return to Main Menu']
transactionMenu=['Borrow Transaction','Return Transaction','Return to Main Menu']
returnMenu=['All Transaction', 'On Time Transaction', 'Late Transaction','Back to Transaction Menu']
lateReturnMenu=['All Late Transaction', 'Not Payed Transaction', 'Payed Transaction','Back to Return Transaction Menu']

# Displaying menu list function
def displayMenu(menu):
    print('\nMenu List: ')
    for i in range(0, len(menu)):
        print(f'{i+1}. {menu[i]} \n')