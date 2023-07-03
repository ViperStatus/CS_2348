#Sokheng Ka 1968133

#Enter current password
pw = input()

password = ''



for character in pw:

    if character == 'i':
        pw = pw.replace('i', '!')
    elif character == 'a':
        pw = pw.replace('a', '@')
    elif character == 'm':
        pw = pw.replace('m', 'M')
    elif character == 'B':
        pw = pw.replace('B', '8')
    elif character == 'o':
        pw = pw.replace('o', '.')
    else:
        password += character

print(pw+'q*s')