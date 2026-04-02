#Write a program that takes 2 words as input from the user and prints out a list containing the letters which the 2 words
#have in common. For example, if the word1 is english and word2 is nepali, the output should be ['e', 'n', 'l', 'i'].

def common_letters(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    common = set(word1) & set(word2)
    return list(common)

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

result = common_letters(word1, word2)
print("Common letters:", result)