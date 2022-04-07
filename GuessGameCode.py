#Setup
import random

usedwords=set()
wantplay=True

#Record
Won = 0
Loss=0

#read words.txt file
f = open('words.txt')
dictionary = f.readlines().splitlines()
f.close()

def getword():
    return random.choice(dictionary)


#multiple gamessetup
while wantplay==True:

    word=getword()
    while word in usedwords:        #check and fetch new words if used before
        word=getword()
    goal=list(word)
    usedwords.add(word)
    numguess = 0
    output = []
    for i in range(0,len(goal),1):
        output.append('_ ')


#Individual Game work
    while numguess <=7: 
        guess = str(input('Enter a letter: '))
        numguess+=1
        print(numguess)
    

        if len(guess) >= 2:
             print("Guess can only contain one letter")
             continue

        for i in range(0,len(goal)):
              if goal[i]==guess:
                    output[i] = guess
                    if output == goal:
                        print("You win")
                        Won+=1                               #adds win
                        numguess = numguess + (8-numguess)   #cancels anymore attempts after correct
                        break
                    if output != word and numguess == 6:
                        print("You are bad")
                        Loss+=1                              #adds loss
                        break
        print(output)
    print('Wins: '+Won+ ' and Losses: '+Loss)
    playagain = str(input('Do you want to play again (Y/N): '))
    if playagain == 'N':
        wantplay = False

