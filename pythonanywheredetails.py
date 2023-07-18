import os 


# Access the value of PA username
username = os.environ.get('pythonanywhereUsername')

# Check if the variable exists
if username is not None:
    print(f"The value of username is: {username}")
else:
    print("username is not set.")




# Access the value of PA password
password = os.environ.get('pythonanywherePassword')

# Check if the variable exists
if password is not None:
    print(f"The value of password is: {password}")
else:
    print("password is not set.")



# Access the value of link to my page on PA
linktobot = os.environ.get('pythonanywherelinktobot')

# Check if the variable exists
if linktobot is not None:
    print(f"The value of linktobot is: {linktobot}")
else:
    print("linktobot is not set.")


