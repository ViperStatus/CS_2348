#Sokheng Ka 19668133

def is_palindrome(text):
    text = text.replace(' ', '')


    if text == text[::-1]:
        return f'{text} is a palindrome'
    else:
        return f'{text} is not a palindrome'

word = input()

output = is_palindrome(word)
print(output)