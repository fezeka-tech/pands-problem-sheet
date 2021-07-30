#WEEK 03#
#This is a python function that outputs every second letter in reverse order#

def second_string ( ) :
    sentence = input ("Please enter a sentence: ") .split ("The quick brown fox jumps over the lazy dog. ") #split sentence by space#
    
    second_letter = [ ] #container to store every second letter#

    for words in sentence:
        second_letter.append(words[1::2]) #store every second letter in a word#

    strings = list (map(lambda x: x[::-1], second_letter)) #reverse second letter of a word#

    print ("The quick brown fox jumps over the lazy dog".join (strings[ ::-1])) #print all in reverse order#

if __name__ == '__main__':
    second_string()
