#using capitalize and title string methods
name = 'john'
surname = 'inu'
print(surname.capitalize())
print(name.title())

#using center
abe = 'I am always a man in the world'
print(abe.center(40, "a"))

#using count
verse = '''If you can keep your head when all about you
Are losing theirs and blaming it on you,
If you can trust yourself when all men are doubt you,
But make allowance for their doubting too;
If you can wait and not be tired by waiting,
Or being lied about, don't deal in lies,
Or being hated, don't give way to hating,
And yet don't look too good, nor talk too wise'''
print(verse.count('you'))

#using the encode and decode string methods
Lab = input('Enter a data: ')
encoded_msg = Lab.encode()
decoded_msg = encoded_msg.decode()

print('Encoded Data: ', encoded_msg)
print('Decoded msg: ', decoded_msg)

#using the endswith string method
ends_with = input('Enter a sentence: ')
if ends_with.endswith('n'):
    print(True)
else:
    print(False)

#using expandtables
expand_tabs = 'P\ty\tt\th\to\tn'
print(expand_tabs.expandtabs(2))
print(expand_tabs.expandtabs(5))
print(expand_tabs.expandtabs(10))

#using the find string method
find = 'Python is a Pretty cool Programming Language'
print(find.find('is'))

#using the rfind method
rfind = 'Python is a pretty cool Programming Language'
print(rfind.rfind('L'))

# using upper
upper = 'python'
print(upper.upper())

# using index
index = 'i love python'
print(index.index('v'))

# using isalnum
string = '56rtt'
print(string.isalnum())

# using isalpha
string = input('Enter a string Format: ')
print(string.isalpha())

# using isdigit
digit = input('Enter digit(s): ')
print(digit.isdigit())

# using lower
lower = 'PYTHON'
print(lower.lower())

# using the replace string method
replace_str = '''I love C# Programming Language'''
print(replace_str.replace('C#', 'Python'))