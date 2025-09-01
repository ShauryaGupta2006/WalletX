


import tkinter as tk
from tkinter import ttk, messagebox, filedialog 
import mysql.connector as sqlx
from datetime import date
from datetime import datetime
import pandas as pd

mydb = sqlx.connect(host = "localhost",user = "root",password = "passcode",database = "WalletX")


mycursor = mydb.cursor()

# print(wall_balance)
t = date.today()

def check_balance():
    print("Your Current Balance is :",wall_balance)
    print("                     ")


while(True):


    result = mycursor.execute("SELECT wall_balance FROM WalletX.main WHERE wall_balance IS NOT NULL ORDER BY tnx_id DESC LIMIT 1;")
    # result = mycursor.execute("SELECT wall_balance FROM WalletX.main WHERE tnx_id IS NOT NULL ORDER BY tnx_id DESC LIMIT 1;")
    # mycursor.execute("Select wall_balance FROM main ORDER BY tnx_id DESC Limit 1;")

    wall_balance001 = mycursor.fetchone()
    wall_balance = int(wall_balance001[0])

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

    print("7 to Exit ")
    u1 = int(input("Choice: "))

    time_now = datetime.now().strftime("%H:%M:%S")
    print(time_now)
    # // what for mai kisko or kis liye 
    #updated balance

    match u1:
        case 1:
            print("Increasing your Wallet Balance: ")
            a1 = int(input("Enter the amount to be added: "))
            a2 = input("Got Money from and for ")
            new_wall_balance = wall_balance+a1

            query = """
                INSERT INTO main(wall_balance, Amount, Category, what_for, tran_date, tnx_time) 
                VALUES (%s, %s,"Deposite", %s, %s, %s)
                """
            values = (new_wall_balance, a1, a2, t, time_now)

            mycursor.execute(query, values)
            print("Amount updated")
            wall_balance = new_wall_balance
            check_balance()
            mydb.commit()


        case 2:
            print("Widhrawal in process: ")
            a1 = int(input("widhraw Amount: "))
            a2 = input("Reason for Widhrawal: ")
            u2 = int(input('''1->Reimbursement
                           2-> Loses ''' ))
            
            if u2 == 1:
                new_wall_balance = wall_balance - a1
                query = """INSERT INTO main(wall_balance,Amount,Category,what_for,tran_date,tnx_time,Reimbursement_amount,Loses) Values(%s, %s, %s, %s, %s, %s, %s, %s) """
                values = (new_wall_balance,a1,"Widrawal",a2,t,time_now,a1,0)
                mycursor.execute(query,values)
                

            elif u2 == 2:
                new_wall_balance = wall_balance - a1
                query = """INSERT INTO main(wall_balance,Amount,Category,what_for,tran_date,tnx_time,Loses,Reimbursement_amount) Values(%s, %s, %s, %s, %s, %s, %s, %s) """
                values = (new_wall_balance,a1,"Widrawal",a2,t,time_now,a1,0)
                mycursor.execute(query,values)
            else:
                print("Entered Something Wrong:")  
            
                
            wall_balance = new_wall_balance
            print("Widhrawal Success")
            check_balance()
            mydb.commit()


        case 3:
            check_balance()
            
        
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
        

        case 6:
            print("Loading Wallet sheet:")
            query = "SELECT * FROM WalletX.main;"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            columns_name = [i[0] for i in mycursor.description] #Ye chiz nayi thi mere liye: It helps to make column name
            df = pd.DataFrame(rows,columns=columns_name)
            df.to_excel("WalletX.xlsx")
            print(df)
        case 7:
            print("Quiting this program BYE!!!")
            exit()

        case _:
            print("Oops something went wrong Please check and try back again: ")
            pass

