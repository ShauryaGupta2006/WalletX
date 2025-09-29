import tkinter as tk
from tkinter import ttk, messagebox, filedialog 
import mysql.connector as sqlx
from db_init import start_mysql_if_stopped
from datetime import date
from datetime import datetime
import pandas as pd

#command to update changes in dmg:

    #hdiutil create -volname "WalletX" -srcfolder /Applications/WalletX.app -ov -format UDZO WalletX.dmg

#dmg file icon:

# hdiutil create -volname "WalletX" -srcfolder /Users/Shaurya/Desktop/Code/Home_directory/projects/WalletX/wallet_1543590.icns -ov -format UDZO WalletX.dmg



start_mysql_if_stopped()
mydb = sqlx.connect(host = "localhost",user = "root",password = "passcode",database = "WalletX")


mycursor = mydb.cursor()
# starter = "sudo /usr/local/mysql/support-files/mysql.server start"
# mycursor.execute(starter)

# print(Saving_Balance)
t = date.today()

def check_save_balance():
    print("Your Current Balance is :",Saving_Balance)
    print("                     ")


def check_current_balance():
    print("Your Current Balance is :",current_Balance)
    print("                     ")

def check_Spending_Balance():
    print("Your Current Balance is :",Spending_Balance)
    print("                     ")

while(True):


    result = mycursor.execute("SELECT Saving_Balance FROM WalletX.main WHERE Saving_Balance IS NOT NULL ORDER BY tnx_id DESC LIMIT 1;")
    # result = mycursor.execute("SELECT Saving_Balance FROM WalletX.main WHERE tnx_id IS NOT NULL ORDER BY tnx_id DESC LIMIT 1;")
    # mycursor.execute("Select Saving_Balance FROM main ORDER BY tnx_id DESC Limit 1;")
    Saving_Balance001 = mycursor.fetchone()
    Saving_Balance = int(Saving_Balance001[0])



    Spending_Balance001 = mycursor.fetchone()
    Spending_Balance = int(Spending_Balance001[0])


    result2 = mycursor.execute("SELECT Current_Balance FROM WalletX.main WHERE Current_Balance IS NOT NULL ORDER BY tnx_id DESC LIMIT 1;")
    current_Balance001 = mycursor.fetchone()
    current_Balance = int(current_Balance001[0])

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1 Insert Amount                      ",end="")
    print("2 Widhraw Amount")
    print("")
    print("3 Check the current balance          ",end="")
    print("4 Check Reimbursment Amount:")
    print("")
    print("5 Check Loses.                       ",end="")
    print("6 to show Wallet Sheet",)
    print("")
    print("7 for Spending amount")

    print("8 to Exit ")
    u1 = int(input("Choice: "))

    time_now = datetime.now().strftime("%H:%M:%S")
    print(time_now)
    # // what for mai kisko or kis liye 
    #updated balance
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Adding up new value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    match u1:
        case 1:
            print(current_Balance)
            print("Adding your Wallet Balance: ")
            print("Saving Balance: ", Saving_Balance,"Current Balance:",current_Balance,"Spending balance: ",Spending_Balance)
            print("1.Saving Wallet 2.Daily Wallet 3. Spending Balance ")
            a3 = int(input("Choose the Wallet:  "))
            a1 = int(input("Enter the amount to be added: "))
            a2 = input("Got Money from and for ")

            match a3:
                case 1:
                    print("New Amount for Saving Wallet")

                    new_Saving_Balance = Saving_Balance+a1

                    query = """
                        INSERT INTO main(Saving_Balance,Current_Balance, Amount, Category, what_for, tnx_date, tnx_time) 
                        VALUES (%s,%s ,%s,"Deposite", %s, %s, %s)
                        """
                    values = (new_Saving_Balance,current_Balance, a1, a2, t, time_now)

                    mycursor.execute(query, values)
                    print("Amount updated")
                    Saving_Balance = new_Saving_Balance
                    check_save_balance()
                    mydb.commit()
                case 2:
                    print("UNew Amount for Daily Wallet")

                    new_current_Balance = current_Balance+a1

                    query = """
                        INSERT INTO main(Saving_Balance,Current_Balance, Amount, Category, what_for, tnx_date, tnx_time) 
                        VALUES (%s,%s ,%s,"Deposite", %s, %s, %s)
                        """
                    values = (Saving_Balance,new_current_Balance, a1, a2, t, time_now)

                    mycursor.execute(query, values)
                    print("Amount updated")
                    current_Balance = new_current_Balance
                    check_current_balance()
                    mydb.commit()
                case 3:
                    print("New Amount for Spending Wallet")
                    New_Spending_Balance = Spending_Balance+a1
                    query = """
                        INSERT INTO main(Saving_Balance,Current_Balance, Amount,Spending_Balance, Category, what_for, tnx_date, tnx_time) 
                        VALUES (%s,%s ,%s,%s,"Deposite", %s, %s, %s)
                        """
                    values = (Saving_Balance,new_current_Balance,New_Spending_Balance, a1, a2, t, time_now)

                    mycursor.execute(query, values)
                    print("Amount updated")
                    Spending_Balance = New_Spending_Balance
                    check_Spending_Balance()
                    mydb.commit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Widhrawing value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

        case 2:
            print("Widhrawal in process: ")
            a1 = int(input("widhraw Amount: "))
            a2 = input("Reason for Widhrawal: ")
            print("1.Saving Wallet 2.Daily Wallet 3. Spending Wallet ")
            a3 = int(input("Choose the Wallet:  "))

            if a3 == 3:
                pass
            elif a3 == 1 || a3 == 2:
                pass
            else:
                continue()
            print("1-> Reimbursement")
            u2 = int(input("2-> Loses \n"))
            

            match a3:

            # This is my Saving Wallet
                case 1:
                    if u2 == 1:
                        new_Saving_Balance = Saving_Balance - a1
                        query = """INSERT INTO main(Saving_Balance,Current_Balance,Amount,Category,what_for,tnx_date,tnx_time,Reimbursement_amount,Loses) Values(%s,%s, %s, %s, %s, %s, %s, %s, %s) """
                        values = (new_Saving_Balance,current_Balance,a1,"Widrawal",a2,t,time_now,a1,0)
                        mycursor.execute(query,values)


                    elif u2 == 2:
                        new_Saving_Balance = Saving_Balance - a1
                        query = """INSERT INTO main(Saving_Balance,Current_Balance,Amount,Category,what_for,tnx_date,tnx_time,Loses,Reimbursement_amount) Values(%s,%s, %s, %s, %s, %s, %s, %s, %s) """
                        values = (new_Saving_Balance,current_Balance,a1,"Widrawal",a2,t,time_now,a1,0)
                        mycursor.execute(query,values)
                    else:
                        print("Entered Something Wrong:")
                    Saving_Balance = new_Saving_Balance
                    print("Widhrawal Success")
                    check_save_balance()
                    mydb.commit()

            #Daily wallet
                case 2:
                    #reimbursment 
                    if u2 == 1:
                        new_current_Balance = current_Balance - a1
                        query = """INSERT INTO main(Saving_Balance,Current_Balance,Amount,Category,what_for,tnx_date,tnx_time,Reimbursement_amount,Loses) Values(%s,%s, %s, %s, %s, %s, %s, %s, %s) """
                        values = (Saving_Balance,new_current_Balance,a1,"Widrawal",a2,t,time_now,a1,0)
                        mycursor.execute(query,values)

        #Losses
                    elif u2 == 2:
                        new_current_Balance = current_Balance - a1
                        query = """INSERT INTO main(Saving_Balance,Current_Balance,Amount,Category,what_for,tnx_date,tnx_time,Loses,Reimbursement_amount) Values(%s,%s, %s, %s, %s, %s, %s, %s, %s) """
                        values = (Saving_Balance,new_current_Balance,a1,"Widrawal",a2,t,time_now,a1,0)
                        mycursor.execute(query,values)
                    else:
                        print("Entered Something Wrong:")

                    current_Balance = new_current_Balance
                    print("Widhrawal Success")
                    check_current_balance()
                    mydb.commit()
        #Spending Wallet
                case 3:
                    print("Widhrawing from Spending Wallet")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Amount checkerr  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

        case 3:
            check_save_balance()
            
        
        case 4:
            print("Checking for reimbursment amount:")
            query = "SELECT SUM(Reimbursement_amount)FROM WalletX.main;"
            mycursor.execute(query);
            reimbursement = mycursor.fetchone()

            print(reimbursement[0])
        case 5:
            print("Checking for loses: ")
            query = "SELECT sum(Loses) FROM WalletX.main"
            mycursor.execute(query);
            loses = mycursor.fetchone()

            print(loses[0])
        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Showing up the whole sheet ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

        case 6:
            print("Loading Wallet sheet:")
            query = "SELECT * FROM WalletX.main;"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            columns_name = [i[0] for i in mycursor.description] #Ye chiz nayi thi mere liye: It helps to make column name
            df = pd.DataFrame(rows,columns=columns_name)
            df.to_excel("WalletX.xlsx")
            print(df)
        
#Spending Branch
        case 7:
            print("Opeing a Spending Branch ")
            u1 = int(input("Enter "))
            
#Exit portion
        case 8:
            print("Quiting this program BYE!!!")
            exit()

        case _:
            print("Oops something went wrong Please check and try back again: ")
            pass
