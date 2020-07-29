#Lab1of7
given_name = 'William'
middle_name = 'Bradley'
family_name = 'Pitt'

name_length = len(given_name) + len(middle_name) + len(family_name)
driving_license_character = 28
if name_length <= driving_license_character:
    print(True)
else:
    print(False)