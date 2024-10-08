# Task 1 : If-elif-else chain for determining a person's stage of life

age = 25  # set a value for the variable age

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# Task 2 : Printing greetings to users

username = ['admin', 'jaden', 'sarah', 'emily', 'mike']

for username in "usernames" :
    if username == 'admin' :
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello {username}, thank you for logging in again.")

# Task 3 : Checking if the list of users is not empty

usernames = []

if not usernames :
    print("We need to find some users!")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again!")

# Task 4 : Checking for unique usernames

current_users = ['john', 'jane', 'bob', 'alice', 'mike']
new_users = ['john', 'sarah', 'emily', 'bob', 'newbie']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is alreaady taken. Please choose a new username.")
    else:
        print(f"{new_user} is available!")
