'''Have the function CamelCase(str) take the str parameter being passed and return 
it in proper camel case format where the first letter of each wordis capitalized
(excluding the first letter).The string will only contain letters and some combination
of delimiter punctuation characters separating each word.For example: if str is 
"BOB loves-coding" then your program should return the string bobLovesCoding.'''

import re

def CamelCase(input_string):
    words = re.findall(r'[a-zA-Z]+', input_string)
    words[0] = words[0].lower()

    for i in range(1, len(words)):
        words[i] = words[i].capitalize()

    return ''.join(words)


print(CamelCase("PB loves-the,park"))

