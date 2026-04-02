#Write a program that takes input from the user a string of numbers (eg-"24453"), then all the numbers from the string must be put
#in a list and their sum should be printed out.

def sum_of_numbers_in_string(input_string):
    numbers_list = []
    total_sum = 0
    
    for char in input_string:
        if char.isdigit():  
            number = int(char)
            numbers_list.append(number)
            total_sum += number

    return numbers_list, total_sum