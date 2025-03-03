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
            print("First name is valid.")
            break
        else:
            print("First name is invalid. Try again.!!! \nHint: Name should start with capital letter and should have minimum 3 characters.")
    print("\n")
    print("-----------------User Details-----------------".center(width))
    print(f"Name : {first_name}")


if __name__ == '__main__':
    main()