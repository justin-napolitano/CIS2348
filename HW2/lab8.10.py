word = str(input())
no_spaces = word.replace(" ", "")
new_word = no_spaces[::-1]

if no_spaces == new_word:
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))