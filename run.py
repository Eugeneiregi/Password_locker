import os
from credentials import Credentials
import pyperclip
from time import time


def generate_password():
    '''

     generate password
    '''

    return os.urandom(8)


print("Hello! Welcome to Password app where passwords are found")
print("****** Use Yes or No as shortcodes to navigate******")
print("Kindly enter your name for continuation")
user_name = input()
print("Thank you please wait...")
time.sleep(2)

print("You have successfully created an account kindlyy proceed")
print(f"Welcome {user_name}")

print("Do you have an existing account? *****Reply Yes  *****")