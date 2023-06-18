'''Have the function ArrayAdditionI(input_list) take the array of numbers stored in input_list
and return the string true if any combination of numbers in the array can be added up to equal
the largest number in the array, otherwise return the string false. For example: if input_list
contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23.
The list will not be empty, will not contain all the same elements, and may contain negative numbers. '''

import itertools

def ArrayAdditionI(input_list):

    largest_num=max(input_list)
    input_list.remove(largest_num)
    
    for r in range(1, len(input_list) + 1):
        combinations = itertools.combinations(input_list, r)
        for combo in combinations:
            
            if sum(combo) == largest_num:
                return "true"

    return "false"
    


print(ArrayAdditionI([3,4,6,10,20,40]))  
       



