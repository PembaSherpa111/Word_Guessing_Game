# %%
#%reset -f
import json, random
play = 'yes'
num_of_win = 0
num_of_loss = 0

while play.lower() == 'yes':

    file_path = (r'words_dictionary.json') #json file needs to be in same folder 
    f = open('words_dictionary.json')
    string_dictionary = f.read()
    dictionary = json.loads(string_dictionary) #converting the data type from string to dictionary
    list_dictionary_keys = list(dictionary.keys()) #converting the collection type from dictionary to list
    random_word = random.choice(list_dictionary_keys)
    f.close()

    num_of_guess = 7

    is_letter = False
    guess = 'aa'

    guessed_word = ('-' * len(random_word))
    
    print(guessed_word) 
    print(f'Number of guesses left = {num_of_guess}')

    while num_of_guess > 0:
        while is_letter == False:
            guess = input('Enter your guess: ')
            is_letter = guess.isalpha()
        
        print(f'Your Guess: {guess}')
        
        if len(guess) > 1:
            if guess.lower() == random_word.lower():
                print (guess.lower())
                print('You Win!')
                num_of_win = num_of_win + 1
                break
            else:
                num_of_guess = num_of_guess - 1
        else:
            index = random_word.find(guess.lower())
            if index == -1:
                num_of_guess = num_of_guess - 1
            else:
                for i,x in enumerate(random_word): #required for cases where duplicate letters are present
                    if x == guess.lower():
                        guessed_word = guessed_word[:i] + guess.lower() + guessed_word[i+1:]
                print(guessed_word)
                if guessed_word == random_word:
                    print('You Win!')
                    num_of_win = num_of_win + 1
                    break
        
        is_letter = False
        print(f'Number of guesses left = {num_of_guess}')

    if num_of_guess == 0:
        print(f'You Lose! The correct answer is {random_word}')
        num_of_loss = num_of_loss + 1
    
    list_dictionary_keys.remove(random_word)
    
    play = 'aa'
    while (play != 'yes') and (play != 'no'):
        play = input('Do you want to play again? Enter yes or no: ')
    
    if play.lower() == 'no':
        print(f'Total number of win: {num_of_win} and Total number of loss: {num_of_loss}') 



