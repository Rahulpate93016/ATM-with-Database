from unittest import result

from BankExceptions4 import insufficient_Balance_Error,ValuesErrors,InvaildPin






def accountopen():
    import random
    try:
        import mysql.connector
        con = mysql.connector.connect(host="127.0.0.1", user="root", password="9999", database="SBI_BANK")
        cur = con.cursor()
        while True:
            print("-"*50)
            Name = input("Enter Account Holder Name:")
            Account = random.randint(1000000000, 9999999999)
            Phone = input("Enter costumer phone number:")
            Branch = input("Enter Branch Name:")
            Balance = int(input("Enter Balance:"))
            pins = random.randint(1001, 9999)
            bnk="""insert into mp_sbi (Name,Account_Number,Phone_number,Branch,Balance,pin)
                values(%s,%s,%s,%s,%s,%s)"""
            cur.execute(bnk, (Name, Account, Phone, Branch, Balance, pins))
            print("-"*50)
            print("New Account is open successfully")
            print("-" * 50)

            con.commit()
            ch = input("Would you like to open new Account?(y/n)")

            if ch != "y":
                break
    except mysql.connector.Error as err:
        print(err)
    except ValueError as err:
        print("Wrong input check it..")




from oracledb import DatabaseError


def deposit():
    try:
        import mysql.connector
        con = mysql.connector.connect(host="127.0.0.1", user="root", password="9999", database="SBI_BANK")
        cur = con.cursor()
        while True:
            print("-"*50)
            Accounts = int(input("Enter Account Number:"))
            pinss = int(input("Enter Pin number:"))
            bnk = """select Account_Number, pin from mp_sbi where Account_Number=%s AND pin=%s
                    """
            cur.execute(bnk, (Accounts, pinss))
            result = cur.fetchone()
            if result is None:
                print("Invalid Account Number or Pin plz try again...")
            else:
                try:
                    dep = int(input("Enter deposit amount:"))
                except ValueError:
                    print("Don't enter input str and special charcter..")
                    break
                if dep < 0:
                    print("Don't Enter Zero...")
                else:
                    query2 = """update mp_sbi set Balance=Balance +%s where Account_Number=%s
                        """
                    cur.execute(query2, (dep, Accounts))

                    print("-"*50)
                    print("The Account Number {} is {} deposit successfully...".format(Accounts, dep))
                    print("-" * 50)

            con.commit()
            ch = input("Do you want to deposite?(y/n)....:")

            if ch != "y":
                break
    except mysql.connector.Error as err:
        print(err)
    except ValueError as err:
        print("Wrong input check it..")




def withdraw():
    try:
        import mysql.connector
        con = mysql.connector.connect(host="localhost", user="root", password="9999", database="sbi_bank")
        cur = con.cursor()
        while True:
            print("_"*50)
            Ac_no = int(input("Enter the account number: "))
            pins = int(input("Enter the amount of pin number: "))
            print("_" * 50)
            bnk = ("""select account_number, pin from mp_sbi where Account_number=%s AND pin=%s""")
            cur.execute(bnk, (Ac_no, pins))
            result = cur.fetchone()
            if result is None:

                raise ValuesErrors("Wrong account number or pin. try again...")
            blns = ("""select Balance from mp_sbi where Account_number=%s""")
            cur.execute(blns, (Ac_no,))
            blns1 = cur.fetchone()[0]
            print("_" * 50)

            withdr = int(input("Enter the ammount for withdraw= "))

            print("Don't Enter str and special charcter..")
            if withdr <= 0:
                raise ValuesErrors("Withdraw amount must be greater than 0")

            elif withdr > blns1:
                raise insufficient_Balance_Error("insufficient balance")
            else:
                blns2 = ("""update mp_sbi set Balance=Balance- %s where Account_number=%s""")
                cur.execute(blns2, (withdr, Ac_no))
                con.commit()
                print("Your account no. {} has been withdred {} rupees chech it..".format(Ac_no, withdr))
                print("Thank you visit again.....")
                print("_" * 50)
                ans = input("You want to continue..(y/n)")
            if ans != 'y':
                print("Thank you for using this application....")
                break
    except mysql.connector.Error as err:
        print(err)
    except ValuesErrors as err:
        print(err)
    except insufficient_Balance_Error as err:
        print(err)




def pinchange():
    try:
        import mysql.connector
        con = mysql.connector.connect(host="localhost", user="root", password="9999", database="sbi_bank")
        cur = con.cursor()
        while True:
            print("-"*50)
            acc_no = input("Enter Account Number: ")
            print("-" * 50)
            pins = input("Enter Pin Number: ")
            print("-" * 50)
            res1 = ("""select Account_number, Pin from mp_sbi where Account_number=%s and Pin=%s""")
            cur.execute(res1, (acc_no, pins))
            result2 = cur.fetchone()
            if result2 is None:
                raise InvaildPin("Invaild Account Number or Pin try again..")
            else:
                try:
                    pins2 = int(input("Enter the new Pin Number: "))
                except ValuesErrors:
                    print("Don't enter str and special charcter..")
                res = ("""update mp_sbi set Pin =%s where Account_number=%s""")
                cur.execute(res, (pins2, acc_no))
                con.commit()
                print("Account Pin Changed Successfully")
                print("-" * 50)
                ans = input("Do you wish to continue? (y/n)")
            if ans != "y":
                print("Thank you visit again.......")
                break
    except mysql.connector.Error as err:
        print(err)
    except InvaildPin as err:
        print(err)




def balance():
    try:
        import mysql.connector
        con=mysql.connector.connect(host="localhost",user="root",password="9999",database="sbi_bank")
        cur=con.cursor()
        while True:
            Ac_no=int(input("Enter account number: "))
            pins=int(input("Enter Pin number: "))
            res1=("""select Account_number ,pin from mp_sbi where Account_Number=%s And Pin=%s""")
            cur.execute(res1,(Ac_no,pins))
            result=cur.fetchone()
            if result is None:
                raise InvaildPin("Invaild Account Number or Pin try again.....")
            else:
                blns=("""select Balance from mp_sbi where Account_Number=%s""")
                cur.execute(blns,(Ac_no,))
                result2=cur.fetchone()[0]
                print("Your Balance is: ",result2)


            ans=input("Do you wish to continue? (y/n)=")
            if ans!="y":
                print("Thank you visit again.............")
                break


    except InvaildPin as e:
        print(e)
    except mysql.connector.Error as e:
        print(e)

