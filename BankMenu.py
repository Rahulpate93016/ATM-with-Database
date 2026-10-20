

from BankOperation import accountopen,deposit,withdraw,pinchange,balance
from BankExceptions4 import insufficient_Balance_Error,ValuesErrors,InvaildPin
from CaseStudy_BANK import userinterface


def menu():
    while True:

        userinterface()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:

                accountopen()
            case 2:
                deposit()
            case 3:

                    withdraw()


            case 4:
                pinchange()
            case 5:
                balance()
            case 6:
                print("Thank you for using our application..............")
                break

            case _:
                print("Oops wrong choice......try again")

menu()
