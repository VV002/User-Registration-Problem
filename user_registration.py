import os
import re
import logging

#setting up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#handlers
stream_Handler = logging.StreamHandler()

#setting format
format = logging.Formatter("%(levelname)s : %(message)s")

#setting formats to handlers
stream_Handler.setFormatter(format)

#level specification
stream_Handler.setLevel(logging.INFO)

#adding handlers to logger
logger.addHandler(stream_Handler)

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
    ls =[]
    i=1
    while i<6:
        match i:
            case 1:
                first_name = input("Enter your first name: ")
                if first_name_validation(first_name): #validating first name
                    ls.append(first_name)
                    i+=1
                else:
                    logger.error("Invalid First name, Try again.!!!")
                    logger.error("Fist Name should start with capital letter and should have minimum 3 characters.")
            case 2:
                last_name = input("Enter your last name: ")
                if last_name_validation(last_name): #validating last name
                    ls.append(last_name)
                    i+=1
                else:
                    logger.error("Invalid Last name, Try again.!!!")
                    logger.error("Last Name should start with capital letter and should have minimum 3 characters.")
            case 3:
                email = input("Enter your email: ")
                if validate_email(email): #validating email
                    ls.append(email)
                    i+=1
                else:
                    logger.error("Email Invalid, Try again.!!!")
                    logger.error("Email should be in proper format.")
            case 4:
                mobile_number = input("Enter your mobile number: ")
                if validate_mobile_number(mobile_number): #validating mobile number
                    ls.append(mobile_number)
                    i+=1
                else:
                    logger.error("Mobile Number Invalid, Try again.!!!")
                    logger.error("Mobile Number should have 10 digits.")
            case 5:
                password = input("Enter your password: ")
                if validate_password(password): #validating password
                    ls.append(password)
                    i+=1
                else:
                    logger.error("Password Invalid, Try again.!!!")
                    logger.error("Password should have minimum 8 characters and Must contain atleast 1 uppercase letter & Special Character .")
    return ls

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
    pattern = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[~`!@#$%^&*()_+\-={}\[\]:;"\'<>,.?/]).{8,}$'
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
    logger.info("-----------------User Details-----------------".center(width))
    logger.info(f"Name : {ls[0]} {ls[1]}")
    logger.info(f"Email : {ls[2]}")
    logger.info(f"Mobile Number : {ls[3]}")
    logger.info(f"Password : {len(ls[4]) * '*'}")
    

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