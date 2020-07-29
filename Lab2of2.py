#Lab2of2
verse = '''If you can keep your head when all about you
Are losing theirs and blaming it on you, 
If you can trust yourself when all men are doubt you,
But make allowance for their doubting too; 
If you can wait and not be tired by waiting,
Or being lied about, don't deal in lies,
Or being hated, don't give way to hating,
And yet don't look too good, nor talk too wise'''

print('The length of the string is: {}'.format(len(verse)))
print("\nThe index of the first occurences of the word 'and' is: {}".format(verse.find('and')))
print("\nThe index of the last occurences of the word 'you' is: {}".format(verse.rfind("you")))
print("\nThe count of occurences of the word 'you' in the verse is: {}".format(verse.count("you")))