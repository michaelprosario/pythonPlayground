#gets og word
word = input("input word: ")
mainIndex = 0
#gets the index of the the word you want to change
def get_index():
    #variable that says true or false
    needToLoop = True
    #while loop asking for an acceptabe index
    while needToLoop:
        #use input to get the index
        index = int(input("enter valid index: "))
        #if the index is valid then return the index and break
        #if index is negative its not valid
        #if index is greater than the available indexs its not valid
        #else continue becausr index not valid

        if index > -2 and index < len(word):
            return index
        else:
            print ("invalid index, input valid index: ")

#gets the letter of the the word you want to change
def get_letter():
    #use input to get the letter
    #if statement making sure there is only one character
    #else telling the user to input a valid number of charcters if not valid already

    out = ""
    #variable that says true or false
    needToLoop = True
    #while loop asking for an acceptabe amount of characters
    while needToLoop:
        #use input to get the character
        out = input("enter valid letter: ")
    
        if len(out) == 1:
            return out
        else:
            print ("invalid character amount, input valid number of characters: ")


# setup list to represent the word
wordAsList = list(word)
while True:
    # get index to change
    mainIndex = get_index()
    if mainIndex ==-1:
        break

    # get the letter
    letter = get_letter()

    # based on the inputs change the word list please
    wordAsList[mainIndex] = letter
    # After the change, write out word list to the screen so user can see updates
    print ("".join(wordAsList))
