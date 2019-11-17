answer = 43
guess = input('I am thinking of a number between 1 and 100: ')
while int(guess) != answer:
    if int(guess) < answer:
        guess = input('Too Low!')
    else:
        guess = input('Too High!')    

