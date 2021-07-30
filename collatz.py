#This is a python function that asks the user to input any positive integer and outputs the successive values of the following calculation...#
def collatz() :

    positive_integer = int(input("Please enter a positive integer: "))
    answer_list = [positive_integer]
    calc = 0

    while positive_integer > 1:                         #...with the use of while loop and if/else statement#
        if positive_integer % 2 == 0:
            calc = positive_integer / 2
            answer_list.append(int(calc))
        else:
            calc = positive_integer * 3 + 1
            answer_list.append(int(calc))

        positive_integer = calc

    answer = " ".join(list(map(str, answer_list)))
    print(answer)
    
    
if __name__ == "__main__":
    collatz()
    

# Collatz Sequence, Stack Overflow; https://stackoverflow.com/questions/33324432/collatz-sequence-python-3
