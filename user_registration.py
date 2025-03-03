import os
import re
width = os.get_terminal_size().columns
print("--------------------WELCOME TO USER REGISTRATION SYSTEM--------------------".center(width))

def get_user_input():
    """
    Description:
        This function is used to get the user input.
    Parameter:
        None
    Return:
        list : User input
    """
    #loop to get the valid user input
    while True:
        ls = [] #list to store user details
        first_name = input("Enter your first name: ")        
        if first_name_validation(first_name): #validating first name
            ls.append(first_name)
            last_name = input("Enter your last name: ")
            if last_name_validation(last_name): #validating last name
                ls.append(last_name)
                email = input("Enter your email: ")
                if validate_email(email): #validating email
                    ls.append(email)
                    mobile_number = input("Enter your mobile number: ")
                    if validate_mobile_number(mobile_number): #validating mobile number
                        ls.append(mobile_number)
                        password = input("Enter your password: ")
                        if validate_password(password): #validating password
                            ls.append(password)
                            print("Valid Input.")
                            return ls
                            break
                        else:
                            print("\nPassword Invalid, Try again.!!!")
                            print("Hint: Password should have minimum 8 characters.\n")
                    else:
                        print("\nMobile Number Invalid, Try again.!!!")
                        print("Hint: Mobile number should be 10 digits number.\n")
                else:
                    print("\nEmail Invalid, Try again.!!!")
                    print("Hint: Email should be in proper format.\n")
            else:
                print("\nLast name Invalid, Try again.!!!")
                print("Hint: Last Name should start with capital letter and should have minimum 3 characters.\n")
        else:
            print("\nFirst name Try again.!!!")
            print("Hint: Fist Name should start with capital letter and should have minimum 3 characters.\n")

def first_name_validation(first_name):
    """
    Description:
        This function is used to validate the first name of the user.
    Parameter:
        first_name (str) : First name of the user.
    Return:
        True : If the first name is valid.
        False : If the first name is invalid.
    """
    if re.match("^[A-Z][a-z]{2,}$", first_name): #pattern matching for first name
            return True
    else:
            return False

def last_name_validation(last_name):
    """
    Description:
        This function is used to validate the last name of the user.
    Parameter:
        last_name (str) : Last name of the user.
    Return:
        True : If the last name is valid.
        False : If the last name is invalid.
    """
    if re.match("^[A-Z][a-z]{2,}$", last_name): #pattern matching for last name
            return True
    else:
            return False
    
def validate_email(email):
    """
    Description:
        This function is used to validate the email of the user.
    Parameter:
        email (str) : Email of the user.
    Return:
        True : If the email is valid.
        False : If the email is invalid.
    """
    #pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+&#-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
    
def validate_mobile_number(mobile_number):
    """
    Description:
        This function is used to validate the mobile number of the user.
    Parameter:
        mobile_number (str) : Mobile number of the user.
    Return:
        True : If the mobile number is valid.
        False : If the mobile number is invalid.
    """
    #pattern for mobile number validation
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, mobile_number))

def validate_password(password):
    """
    Description:
        This function is used to validate the password of the user.
    Parameter:
        password (str) : Password of the user.
    Return:
        True : If the password is valid.
        False : If the password is invalid.
    """
    #pattern for password validation
    pattern = r'(?=.[A-Z]).{8,}'
    return bool(re.match(pattern, password))
     
def print_result(ls):
    """
    Description:
        This function is used to print the user details.
    Parameter:
        first_name (str) : First name of the user.
        last_name (str) : Last name
    Return:
        None
    """
    print("\n")
    print("-----------------User Details-----------------".center(width))
    print(f"Name : {ls[0]} {ls[1]}")
    print(f"Email : {ls[2]}")
    print(f"Mobile Number : {ls[3]}")
    print(f"Password : {len(ls[4]) * '*'}")
    

def main():
    """
    Description:
        This is a main function.
    Parameter:
        None
    Return:
        None
    """
    ls = get_user_input()
    print_result(ls)


if __name__ == '__main__':
    main()