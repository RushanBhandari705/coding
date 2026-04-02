#An anagram is a word that contains same characters in different order, such as silent and listen or schoolmaster and the classroom.
#write a function that takes a word as input and determines whether it is a anagram or not.

def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    return sorted(word1) == sorted(word2)

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if are_anagrams(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are NOT anagrams.")

