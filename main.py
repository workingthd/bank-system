from pymongo import MongoClient  # DataBase Connected Section
client = MongoClient("mongodb://localhost:27017/")
mydb = client['bank']
mycol = mydb["customers"]
while True:  # Menu
 print("This is a Bank system..")
 print("1 for new account open")
 print("2 for deposit money")
 print("3 for withdraw money")
 print("4 for view account details")
 print("5 for delete account")


 options=int(input())

 if options==1:    # create account

    name=input("Enter your name ?")
    age=input("enter your age ?")
    amount = int(input("enter deposit Amount ?"))
    account_no=int(input("enter account number ?"))
    dict = {"name": name,"agr":age,"amount":amount,"account_no":account_no}  # collect data for database
    data_insert = mycol.insert_one(dict) # insert all data in database
 elif options==2:      # deposit money section
    account_no=int(input("enter account number ?"))
    new = {"account_no":account_no} # account number
    mydoc = mycol.find_one(new) # find data with account number
    print(mydoc)
    current_amount = mydoc["amount"] # amount index find and load his value
    amount = int(input("Enter Deposit Amount ?"))
    addition_amount=current_amount+amount # here addition new money and calculations
    update_myquery = {"$set": {"amount":addition_amount}} # update the money in database
    mydocs = mycol.update_many(new, update_myquery) # here two arguments and one is specific account find and second update data query and data updated
    update_account_details=mycol.find_one(new) # here find again account
    print(update_account_details)
    print("Your Amount Deposit successfully.....")
    # same logics worked here
 elif options==3:  # Withdraw money section
    account_no=int(input("enter account number ?"))
    new = {"account_no":account_no}
    mydoc = mycol.find_one(new)
    print(mydoc)
    current_amount=mydoc["amount"]
    amount = int(input("Enter withdraw Amount ?"))
    dedect_amount=current_amount-amount
    update_myquery = {"$set": {"amount":dedect_amount}}
    mydocs = mycol.update_many(new, update_myquery)
    update_account_details=mycol.find_one(new)
    print(update_account_details)
    print("Your Amount withdraw successfully.....")
 elif options==4: # find account details
    account_no=int(input("enter account number ?"))
    new = {"account_no":account_no}
    mydoc = mycol.find_one(new) # details find a specific account in which account number is given
    print(mydoc)
 elif options==5:  # delete account section
    account_no=int(input("enter account number ?"))
    new = {"account_no":account_no}
    mydoc = mycol.find_one(new) # find a specific account in which account number is given
    print(mydoc)
    mydoc = mycol.delete_one(new) # here delete record query run
    print("your account deleted !")
 else:  # if not condition True
    print("You Chose Wrong Option! ")
