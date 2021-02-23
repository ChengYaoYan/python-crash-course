guests = ['Mary', 'Susan', 'Alexzendra']
invitation_message = f"{guests[0]}, I want to invite you to have dinner with me."

print(invitation_message)

can_not_make_the_dinner_guest = 'Mary'
print(f"{can_not_make_the_dinner_guest} can not make the dinner.")

new_guest = 'Richard'
guests.remove('Mary')
guests.append(new_guest)
invitation_list_message = f"invitation list is: {guests}."
print(invitation_list_message)

guests = ['Mary', 'Susan', 'Alexzendra']
# suddently, I get a big table, so I can invite more people to my dinner
guests.insert(0, 'Harry')
guests.insert(2, 'Philip')
guests.append('Robbie')
print(guests)

print(guests)
# new dinner table won't arrive in time for the dinner, and have space for only
# two guests
poped_guest = guests.pop()
print(f"{poped_guest} I'm so sorry that I can't invate you to my dinner for some reason now.")
poped_guest = guests.pop()
print(f"{poped_guest} I'm so sorry that I can't invate you to my dinner for some reason now.")
poped_guest = guests.pop()
print(f"{poped_guest} I'm so sorry that I can't invate you to my dinner for some reason now.")
poped_guest = guests.pop()
print(f"{poped_guest} I'm so sorry that I can't invate you to my dinner for some reason now.")
print(guests)
print(f"{guests[0]} I want to invite you to have dinner with me.")
print(f"{guests[1]} I want to invite you to have dinner with me.")
del guests[0]
del guests[0]
print(guests)
