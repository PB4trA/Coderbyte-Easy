'''Have the function CodelandUsernameValidation(str) take the str parameter 
being passed and determine if the string is a valid username according to the following 
rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.'''
import re

def CodelandUsernameValidation(test_string):
    
    pattern = re.compile(r'^[a-zA-Z]\w{2,23}[^_]$')
    match = re.search(pattern, test_string)
    
    if match:
        return "true"
    else:
        return "false"

print(CodelandUsernameValidation('minions'))



