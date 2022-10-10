word = input()
password = ''

replace = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}
for key, value in replace.items():
    word = word.replace(key, value)

password = word

print(f'{password}q*s')