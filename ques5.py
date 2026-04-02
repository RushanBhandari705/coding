#Write a function that takes a word numeric values as input and counts the number of numeric value and consonants present in the word.

def count_numeric_and_consonants(word):
    vowels = "aeiouAEIOU"
    numeric_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isdigit():  
            numeric_count += 1
        elif char.isalpha(): 
            if char not in vowels:
                consonant_count += 1
                
    return numeric_count, consonant_count