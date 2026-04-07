#The file "lab8.txt" cotains 16 numbers separated by commas and divided into 4 times. Write a program that reads the numbers from the file and finds
# out the sum of all the numbers, and the maximum and minimum number.
 
with open("lab8.txt", 'r') as file:
    lines=file.readlines()
    print(lines)
    sum=0
    for line in lines:
        numbers=line.strip().split(",")
        print(numbers)
        for nums in numbers:
            sum+=int(nums)
    print(sum)