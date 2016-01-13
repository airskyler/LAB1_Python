
#LAB 1 , Part 1

'''
import random

count = 0

# generate random number
number = random.randint(1, 11)

print(number)


# use while loop to count how many time the user have to guess the correct number
# also give a user a hint to guess the correct number
while True:

    numberUser = int(input("Please pick one number from range between 1 to 11\n"))

    if number == numberUser:
        print("You guess the correct number! - it took - ")
        print(str(count)+ " time to guess the correct number\n")

        break  # if user guess the correct number... stop running the program code

    elif number > numberUser:
        print("Hint... you guess the number too low\n")

        count = count+1


    elif number < numberUser:
        print("Hint... you guess the number too high\n")

        count = count+1


'''

# LAB 1 , Part 2

sentence = input("please write a sentence")

Allword = sentence.split()


firstWord = Allword[0]

firstCamelWord = firstWord[0:].lower()

print(firstCamelWord)

addWord = ''

for word in Allword[1:]:
    camelWord =(word[0].upper()+ word[1:].lower())

    addWord = addWord + camelWord


##  still need work for the LAB1 part 2
newSentence = firstCamelWord + addWord

print(newSentence)








































