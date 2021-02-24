current_users = ['Admin', 'Mary', 'Robbie', 'Richard', 'Marilyn']
current_users_lowercase = ['admin', 'mary', 'robbie', 'richard', 'marilyn']
new_users = ['MARY', 'Robbie', 'Alexzendra', 'Harry', 'Susan']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} has already been used!")
    elif new_user.lower() in current_users_lowercase:
        print(f"{new_user} has already been used!")
    else:
        print(f"{new_user} is available.")
