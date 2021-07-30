# this a python program that reads in a text file and outputs the number of e's it contains #

def es():
    record = {}
    search = "e"
    
    with open('moby-dick.text') as file:
        for _ in file.read() .split():
            if search in record:
                record[search] += 1
            else:
                record[search] = 1

    print(record)

    if __name__ == "__main__":
        es()

# https://gist.github.com/StevenClontz/4445774 #
