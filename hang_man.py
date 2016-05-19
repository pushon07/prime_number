"""
Hangman game in Python
"""
import time
import numpy as np


words = "I love KZ penguin will be always there for the loving bird pragmatic deride ".split()

graphic0 = """  
________    
|      |      
|             
|             
|             
|
"""     
graphic1 = """
________      
|      |      
|      0       
|             
|             
|
"""  
graphic2 = """
________      
|      |      
|      0       
|     /        
|             
|
"""  
graphic3 = """
________      
|      |      
|      0       
|     / \      
|             
|
"""  
graphic4 = """
________      
|      |      
|      0       
|     /|\       
|            
|
"""  
graphic5 = """
________      
|      |      
|      0       
|     /|\       
|      |      
|
"""
graphic6 = """
________      
|      |      
|      0       
|     /|\       
|      |      
|     /
"""  
graphic7 = """
________      
|      |      
|      0       
|     /|\       
|      |      
|     / \
|        
"""  

hang_graphics = [graphic0, graphic1, graphic2, graphic3, graphic4, graphic5, graphic6, graphic7]

#game settings
#__________________________________________________________________________________________
#rand_word = np.random.choice(words, 1)[0]
rand_word = 'always'
character_remaining = rand_word


num_wrong_guess = 0
display_word = '_' * len(rand_word)

isWinner = False

print "Let's start the fun! :)"
print 'Initial state: %r' % ("|".join(display_word))
print "You are here: ", graphic0

while num_wrong_guess < 7:
    guess_char = raw_input("Guess a letter ->")
    
    if len(guess_char) > 1:
        print 'Plz insert a single character at a time'

    elif len(guess_char) < 1:
        print 'Plz insert a single character'
    
    elif guess_char in character_remaining:
        character_remaining = character_remaining.replace(guess_char, '', 1)
        if not(guess_char in display_word):
            ind = rand_word.index(guess_char)
            display_word = display_word[:ind] + guess_char + display_word[ind+1:]
        elif guess_char in display_word:
            ind_disp = display_word.index(guess_char)
            ind = rand_word.index(guess_char, ind_disp+1)
            display_word = display_word[:ind] + guess_char + display_word[ind+1:]
        
        print 'Good job!'
        print 'Current state: %r' % ("|".join(display_word))
        print "%r percent completed" % (100.0 - len(character_remaining) * 100 / len(rand_word))
                
        if (len(character_remaining) < 1): #condition for successfully completing the game
            isWinner = True
            print "Awesome! You won the game!!"
            break
    
    elif not(guess_char in character_remaining): #Guessed the wrong character
        num_wrong_guess += 1
        print "Oops, not the right guess.. :("
        print 'Try again please'
        print 'Current state: %r' % ("|".join(display_word))
        print "Chance(s) remaining: %r more chances" % (7 - num_wrong_guess)
        print hang_graphics[num_wrong_guess]
       
if not(isWinner):        
    print "Game over! You are hanged!"