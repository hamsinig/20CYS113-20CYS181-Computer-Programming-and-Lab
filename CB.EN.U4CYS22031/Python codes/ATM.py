# Creating an atm model that asks user for function to be used.
print("Welcome to the atm")
print("Please enter your name.")
name = input()
print("please enter your account number")
acct = int(input())
print("please enter your account balance")
balance = float(input())
print("please enter your secret pin")
pin = input()
min = 500

# User details collection complete
if len(pin) == 4:
    
    # Pin verification
    # function menu to be displayed to user
    print(" which function would you like to use.")
    print("1 ---> WIthdraw money")
    print("2 ---> deposit money")
    print("3 ---> view account balance")
    print("4 ---> change pin")
    fn = int(input())
    if fn == 1:
        
        # withdrawal programme
        print("please enter amount to be withdrawn.")
        amt = float(input())
        if balance >= min:
            print("please enter your pin")
            secret = input()
            if secret == pin:
                if balance - amt > 0:
                    print("transaction successful. Updated account balance is " + str(balance - amt))
                    if balance - amt < min:
                        print("current balance is " + str(balance - amt) + " Please deposit money to maintain minimum balance Rs. " + str(min) + "otherwise you may attract penalties.")
                else:
                    print("transaction unsuccessful due to insufficient funds. please run again and enter amount to be withdrawn lower than " + str(balance))
            else:
                print("Invalid pin. Please run again and enter correct pin.")
        else:
            if balance < 0:
                print("balance cannot be negative. please run again and enter correct balance.")
            else:
                print("Minimum balance for withdrawal is 500. Due to insufficient funds this transcation can't be processed. ")
    else:
        if fn == 2:
            
            # deposit programme
            print("please enter amount you would like to deposit.")
            amt = float(input())
            print("please enter your pin")
            secretpin = input()
            if pin == secretpin:
                print("deposit successful.")
                print("current account balance is " + str(balance + amt))
            else:
                print("Invalid pin. Transaction unsuccessful.")
        else:
            if fn == 3:
                
                # Account balance programme
                print("please enter your pin.")
                secpin = input()
                if pin == secpin:
                    print("current account balance is " + str(balance))
                else:
                    print("invalid pin")
            else:
                if fn == 4:
                    
                    # Pin change algorithm
                    print("please enter your current pin.")
                    sec = input()
                    if pin == sec:
                        print("Enter new pin.")
                        new = input()
                        if len(new) == 4:
                            print("reenter new pin for confirmation.")
                            new2 = input()
                            if new == new2:
                                print("Successful. Pin has been changed to " + new)
                            else:
                                print("pins dont match. operation unsuccessful.")
                        else:
                            print("pin must be of four digits.")
                    else:
                        print("invalid pin.")
                else:
                    
                    # only 4 functions are available
                    print("Invalid input.")
else:
    print("Invalid pin. Pin must be of four digits.")
print("Thank you for using this atm.")
