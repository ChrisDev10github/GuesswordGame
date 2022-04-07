#Setup
#Comment for testing commit and push!!!!!
import random

usedwords=set()
wantplay=True

#Record
Won = 0
Loss=0

#read words.txt file

def getword():
    f = open(r'C:\Users\Chris\Documents\PythonCode\words.txt')
    #dictionary = f.readlines().splitlines()
    dictionary = f.read().split('\n')
    f.close()
    return random.choice(dictionary)


#multiple gamessetup
while wantplay==True:

    word=getword()
    while word in usedwords:        #check and fetch new words if used before
        word=getword()
    while len(word)>=6:
        word=getword()
    print(word)
    goal=list(word)
    usedwords.add(word)
    numguess = 0
    output = []
    for i in range(0,len(goal),1):
        output.append('_ ')


#Individual Game work
    while numguess <=7 and wantplay ==True: 
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
                    print(f'Num guesses = ',numguess)
                    playagain = str(input('Do you want to play again (Y/N): '))
                    if playagain == 'N':
                        wantplay = False
                    break
            if output != word and numguess == 8:
                print("You are bad")
                Loss+=1                              #adds loss
                playagain = str(input('Do you want to play again (Y/N): '))
                print(playagain)
                if playagain == 'N':
                    wantplay = False
                break
        print(output)
    print('Wins: ',Won, ' and Losses: ',Loss)
       

    


