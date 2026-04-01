#A palindrome is a word or a squence of characters which reads the same backward as forward, such as madam or racecar. Write a function
#that takes a word as input and determines whether it is palindrome or not.

def is_palindrome(word):
    word = word.lower()  # Convert to lowercase for case-insensitive comparison
    return word == word[::-1]  # Check if the word is the same as its reverse