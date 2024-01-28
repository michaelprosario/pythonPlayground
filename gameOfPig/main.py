import random
player1 = 0
player2 = 0
roundScore = 0
turn = True
randomNum = 0
while player1 != 100:
    if player1 >= 100:
        print ("end game")
        break
    while turn == True:
        # dice roll
        randomNum = random.randint(1,6)
        print ("Player1's randomNum is " + str(randomNum))
        if randomNum >= 2:
            roundScore = randomNum + roundScore
            print ("Player1's score is " + str(roundScore))
        else:
            roundScore = 0
            print ("Player1's score is " + str(roundScore))
            turn = False
            break
        
        userInput = input("Bank or pig?")
        if userInput == "bank":
            player1 == player1 + roundScore
        elif userInput == "pig":                
            continue
        else:
            print ("invalid input do again")
            
while player2 !=100:            
   if player2 >= 100:
        print ("end game")
        break
   while turn == False:
        randomNum = random.randint(1,6)
        if randomNum >= 2:
            roundScore = randomNum + roundScore
        else:
            roundScore = 0
            turn = True
            break
        while True:    
            bank = input("Bank or pig?")
            if bank == "Bank":
                player2 == player2 + roundScore
            elif bank == "pig":
                roundScore == roundScore + randomNum
                continue
            else:
                print ("invalid input do again")
