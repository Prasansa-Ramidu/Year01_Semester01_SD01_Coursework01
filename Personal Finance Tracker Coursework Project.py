#Import JSON module
import json
#Import re module
import re

#File path for JSON data
json_file_path = "Financial_Transactions.json"

#Global list to store transaction list
Transaction = []

#File handling functions:

#This Function used to load data from the JSON file
def load_data():
    #Open the JSON file in read mode
    try:
        with open(json_file_path, "r")as file:
            #Load the deserialized JSON data into the Transaction list   
            Transaction = json.load(file)
            return Transaction
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

#This Function used to save data to the JSON file    
def save_data():
    #Open the JSON file in write mode
    with open(json_file_path, "w")as file:
        #Write the serialized contents of the Transaction list to the file
        json.dump(Transaction, file)

#Core Features Implementation:

#This function used to check the date format
def check_date_format(date):
    valid_date = False
    match_found = False
    #Use regular expression to find a match for date pattern like YYYY-MM-DD
    match_check = re.findall(r'\b\d{4}-\d{2}-\d{2}\b',date)
    #Check if a match is found
    if match_check:
        match_found = True
        
    #If a match is found then proceed with checking date components
    if match_found:
        date_parts = date.split('-')
        #Check if a month and day components fall within valid ranges
        if ( 1 <= int(date_parts[1]) <= 12 ) and ( 1 <= int(date_parts[2]) <= 31 ):
            valid_date = True

    return valid_date

#This Function used to add a new transaction        
def add_transaction():
    try:
        global Transaction
        #Get the next available id for transaction
        id = len(Transaction) + 1
        #Prompt the user to input transaction details
        amount = float(input("Enter the amount: "))
        category = input("Enter the catagory: ")
        category = category.capitalize()
        type = input("Enter if this is a Income or Expense: ")
        if type == "Expense":
            amount = float("-"+str(amount))
        
        date = input("Enter the date according to this(YYYY-MM-DD)format: ")
        #Validate the date format in transaction
        if check_date_format(date):
            #Create a new transaction and add that in to the Transaction list
            transaction = [id, amount, category, type, date]
            Transaction.append(transaction)
            #Save the transaction data to the the JSON file
            save_data()
            print("Transaction added sucessfully")
        else:
            print("Invalid date format")
            
    except ValueError:
        print("Invalid input try again")

#This Function used to view the added transaction    
def view_transaction():
    global Transaction
    if not Transaction:
        print("Transaction not Found")      
    else:
        try:
            #Prompt the user to input transaction id 
            id = int(input("Enter the transaction id to view: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for transaction id")
        #Search the transaction with the specified id in the Transaction id
        count = 0
        for transaction in Transaction:
            if transaction[0] == id:
                print("Transaction Details: ")
                #Display the transaction details
                print(f"ID: {transaction[0]}")           
                print(f"Amount: {transaction[1]}")
                print(f"Catagory: {transaction[2]}")
                print(f"Type: {transaction[3]}")
                print(f"Date: {transaction[4]}")
                break
            else:
                count += 1
        if count == len(Transaction):
            print("Invaild id")

#This Function used to update the transaction that user added        
def update_transaction():
    global Transaction
    if not Transaction:
        print("No transactions found")
    else:
        try:
            #Prompt the user to input transaction id to update
            id = int(input("Enter the transaction id to update: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for transaction id")

        #Search for the transaction with the specified id in the Transaction list    
        id_found = True
        count = 0
        for index, transaction in enumerate(Transaction):
            if transaction[0] == id:
                #Prompt the user to input new transaction details
                amount = float(input("Enter the user new amount: "))
                category = input("Enter the new catagory: ")
                type = input("Enter if this is a Income or Expense: ")
                if type == "Expense":
                    amount = float("-"+str(amount))
                date = input("Enter the new date: ")
            
                Transaction[index] = [id, amount, category, type, date]
                #Save data to the JSON file
                save_data()
                print("Transaction updated successfully")
            else:
                count = count + 1
        if len(Transaction) == count:
            id_found = False
        if not id_found:
            print("No id found")
                
#This Function used to delete the transaction that user added            
def delete_transaction():
    global Transaction
    if not Transaction:
        print("No transactions found")
        
    else:    
        try:
            #Prompt the user to input transaction id to delete
            id = int(input("Enter the transaction id to delete: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for transaction id")
        #Search for the transaction with the specified id in Transaction id     
        for index, transaction in enumerate(Transaction):
            if transaction[0] == id:
                del Transaction[index]
            #Save data to the JSON file
            save_data()
            print("Transaction deleted successfully.")
            break

#This Function used to display summary of all transactions    
def display_summary():
    global Transaction
    if not Transaction:
        print("No transactions found")
        
    #Get the total balance from all transactions that has been made    
    total_balance = sum(transaction[1] for transaction in Transaction)
    print(f"The total balance is {total_balance}")

#This Function used to add transactions loaded from JSON to Transaction list
def add_transactions_to_list(returned_list):
    try:
        global Transaction
        #Add each transation from returned list to Transaction list
        for inner_list in returned_list:
            Transaction.append(inner_list)
            
    except ValueError:
        print("Invalid input try again")

#Main menu function
def menu():       
    #Main loop Programe(Main_menu)    
    while True:
        print("\nPersonal Finance Tracker Menu Choices: ")
        print("1.Add Transaction")
        print("2.View Transaction")
        print("3.Update Transaction")
        print("4.Delete Transaction")
        print("5.Display Summary")
        print("6.Exit\n")

        choice = input("Enter your Choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transaction()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Good Bye. Exiting from the Personal Finance Tracker")
            break
        else:
            print("Invalid Choice. Try again between 1 to 6 numbers")
            
#Load data from JSON file
returned_list = load_data()
#Add loaded transactions to the Transaction list
add_transactions_to_list(returned_list)      
#Run main menu loop  
menu()


#if you are paid to do this assignment please delete this line of comment.
    

   



   

        
       
        
    
    
    
