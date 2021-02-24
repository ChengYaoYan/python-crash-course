favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll = ['jen', 'sarah']

for person in favorite_languages.keys():
    if person in poll:    
        print("thanks")
    else:
        print("please respond")
