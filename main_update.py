import mysql.connector as sqlx
from datetime import date
from datetime import datetime
import pandas as pd


# start_mysql_if_stopped()
mydb = sqlx.connect(host = "localhost",user = "root",password = "passcode",database = "WalletX")


mycursor = mydb.cursor()

def Deposite(saving_balance,current_Balance,Amount,Spending_Balance,what_for,tnx_date,tnx_time):

    query = """
        INSERT INTO main(Saving_Balance,Current_Balance, Amount, Category, what_for, tnx_date, tnx_time) 
        VALUES (%s,%s ,%s,"Deposite", %s, %s, %s)
        """
    values = (saving_balance,current_Balance, Amount,Spending_Balance,"Deposite",what_for,tnx_date,tnx_time)
    mycursor.execute(query,values)



def Widhrawal(saving_balance,current_Balance,Amount,what_for,tnx_date,tnx_time):
    query = """
        INSERT INTO main(Saving_Balance,Current_Balance, Amount, Category, what_for, tnx_date, tnx_time) 
        VALUES (%s,%s ,%s,"Deposite", %s, %s, %s)
        """
    values = (saving_balance,current_Balance, Amount,"Widrawal",what_for,tnx_date,tnx_time)
    mycursor.execute(query,values)



while True:

    Saving_Balance001 = mycursor.fetchone()
    Saving_Balance = int(Saving_Balance001[0])



    Spending_Balance001 = mycursor.fetchone()
    Spending_Balance = int(Spending_Balance001[0])


    result2 = mycursor.execute("SELECT Current_Balance FROM WalletX.main WHERE Current_Balance IS NOT NULL ORDER BY tnx_id DESC LIMIT 1;")
    current_Balance001 = mycursor.fetchone()
    current_Balance = int(current_Balance001[0])


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1 Deposite Amount                      ",end="")
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
# Date Time Fetching Functions: 
    time_now = datetime.now().strftime("%H:%M:%S")
    print(time_now)

    t = date.today()


    match u1:
        case 1:
            print("Adding your Wallet Balance: ")
            print("Saving Balance: ", Saving_Balance,"Current Balance:",current_Balance,"Spending balance: ",Spending_Balance)
            print("1.Saving Wallet 2.Daily Wallet 3. Spending Balance ")
            u2 = int(input("Choose the Wallet:  "))
            a1 = int(input("Enter the amount to be added: "))
            a2 = input("Got Money from and for ")

            match u2:
                case 1:
                    print("Adding Value to your Saving Wallet: ")
                    print("New Amount for Saving Wallet")

                    new_Saving_Balance = Saving_Balance + a1

                    Deposite(new_Saving_Balance,current_Balance,a1,Spending_Balance,a2,t,time_now)

                case 2:
                    print("Adding Value to your Current Wallet: ")
                    print("New Amount for Saving Wallet")

                    new_current_Balance = current_Balance + a1
                    
                    Deposite(Saving_Balance,new_current_Balance,a1,a2,t,time_now)
                case 3:
                    print("Adding up value to Spending Wallet: ")

                    new_Spending_Balance = Spending_Balance + a1
                    
                    Deposite(Saving_Balance,current_Balance,a1,new_Spending_Balance,a2,t,time_now)
        case 2:
            print("Widhrawal in process: ")
            a1 = int(input("widhraw Amount: "))
            a2 = input("Reason for Widhrawal: ")
            print("1.Saving Wallet 2.Daily Wallet 3. Spending Wallet ")
            a3 = int(input("Choose the Wallet:  "))

            match a3:
                
                case 1:
                    new_Saving_Balance = Saving_Balance + a1

                    Deposite(new_Saving_Balance,current_Balance,a1,Spending_Balance,a2,t,time_now)
