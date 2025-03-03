import os
import re
width = os.get_terminal_size().columns
print("--------------------WELCOME TO USER REGISTRATION SYSTEM--------------------".center(width))

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
    if re.match("^[A-Z][a-z]{2,}$", first_name):
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
    if re.match("^[A-Z][a-z]{2,}$", last_name):
            return True
    else:
            return False
    
def print_result(first_name, last_name):
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
    print(f"Name : {first_name} {last_name}")

def main():
    """
    Description:
        This is a main function that triggers the validators.
    Parameter:
        None
    Return:
        None
    """
    while True:
        first_name = input("Enter your first name: ")
        if first_name_validation(first_name):
            while True:
                last_name = input("Enter your last name: ")
                if last_name_validation(last_name):
                    print("First & last name is valid.")
                    break
                else:
                    print("Last name is invalid. Try again.!!! \nHint: Name should start with capital letter and should have minimum 3 characters.")
            print_result(first_name, last_name)
            break
        else:
            print("First name is invalid. Try again.!!! \nHint: Name should start with capital letter and should have minimum 3 characters.")


if __name__ == '__main__':
    main()