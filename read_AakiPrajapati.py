#Reading and displaying the available stock
def read_from_file():
    """
    function: it is used to open the .txt file in read mode and store the items in a 2D list nl 
    return: it returns the 2D list nl
    """
    file=open("WeCare.txt","r")     #opening the text file in read
    nl=[]
    lines=file.readlines()          #converts each line into a single list separated by \n
    for each in lines:              #for one line at a time from the list
        l=each.replace("\n","").split(",")      #replaces \n by a space and to identify separate elements of each line, it is split using , '''
        nl.append(l)                        #storing all of the lists in one single list
    file.close()                            #to close the opened file
    return nl
