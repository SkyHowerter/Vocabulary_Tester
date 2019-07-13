import random
from collections import Counter

def randomword(n):
    array=[]
    i=0.0
    with open('american-english.txt','r') as f:
        for line in f:
            name = line
            array.append(name)
            i=i+1
    numwords=i
    i=0
    tracker=0.0
    while(i<n):
        print("NEW WORD:")
        print (array[random.randint(1,numwords)])
        take = raw_input("Do you know the definition of this word? y/n: ")
        print("\n")
        if (take is "y" or take is "Y"):
            tracker=tracker+1
        i=i+1

    array=[tracker, n, numwords]
    return array

print("Welcome to Vocabulary tester!")
response = input("Type how many words would you like to test, and press enter: ")
print("\n")
array = randomword(response)
percent = array[0]/array[1]
known = percent*array[2]
print("You got " + str(percent) + "% correct.")
print("There were " + str(array[2]) + " words in the dictionary you played with.")
print("I calculate that you know " + str(known) + " words.")
print("Thanks for playing!")
