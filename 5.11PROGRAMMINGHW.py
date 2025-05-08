import math
import string

def summarize_letters(word):

    word = ''.join(i for i in word if i.isalnum()) #gets rid of spaces and special characters
    word = word.lower() #makes them lowercase

    length_ = len(word)
    word_list = []

    alphabet = tuple(string.ascii_lowercase) #tuple of alphabet



    for i in range(length_): #gets the individual letters
        ind_letters = word[i]
        word_list += ind_letters
    

    length_ = len(word_list)
    counting = []

    for i in range(length_):
        counter = 0
        for j in range(length_):

            if word_list[i] == word_list[j]: #counts the amount of times the character appears
                counter += 1
        
        counting += [(word_list[i], counter)] #adds them as a pair to the list

    no_repeats = tuple(set(word))

    print(tuple(set(counting))) #deletes the duplicates
    alphabetcounter = 0

    for i in range(len(alphabet)):
        if alphabet[i] in no_repeats:
            alphabetcounter += 1
            
    print(alphabetcounter)

    
    if alphabetcounter == len(alphabet):
        print("The tuple has all the letters in the alphabet.")

    else:
        print("The tuple does NOT have all the letter in the alphabet.")



input_word = input("What is your word? ")
summarize_letters(input_word)
