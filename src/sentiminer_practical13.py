#!/usr/bin/env python3

DATE = "2 December 2019"
VERSION = "i"
AUTHOR = ""
AUTHORMAIL = "@allegheny.edu"


# program to determine a sentiment score from a user-entered sentence or a file.

def help():
        h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
        print("  "+len(h_str) * "-")
        print(h_str)
        print("  "+len(h_str) * "-")

        print("\n   Program to read in a sentence, load a")
        print("   sentiment file to analyse for sentiment content")
        print("\n   Program takes parameters 's' to ask user for a sentence")
        print("   otherwise a filename will be prompted ")

        platform_str = get_platformType()
        print("\n\t OS type: ",platform_str) # determine what the os is.
        #print("""\n\tLibrary installation notes:""")

        command_str1 = "\t + To enter a sentence manually: python3 sentiminer_practical13.py s"
        command_str2 = "\t + To enter a file: python3 sentiminer_practical13.py f filename"

        command_str =  command_str1 +"\n" +command_str2

        if platform_str.lower() == "linux" or platform_str.lower() == "osx":
            print("\t Usages \U0001f600 \n", command_str)
        else:
            print("\t Usages :-) \n", command_str)

#end of help()


def get_platformType():
        """Function to dermine the OS type."""
        platforms = {
            'darwin' : 'OSX',
            'win32'  : 'Windows',
            'linux1' : 'Linux',
            'linux2' : 'Linux'
        }
        if sys.platform not in platforms:
            return sys.platform
        return platforms[sys.platform]
#end of get_platformType()


def getSentiments(csvfile):
    """opens the file csv file containing finn sentiment words"""
    word_dict = {}
    with open(csvfile, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        for row in datareader:
            word_dict[row[0]] = row[1]
    return word_dict
#end of getSentiments()



def getSentence():
    """ask the user to enter something to evaluate"""
    data_str = input("\t Enter a sentence to scan for sentiment : ")
    print("\t Your input is: ",data_str, type(data_str))

    return data_str.split() #return a list
#end of getSentence()



def getFile(fname):
    """open textfile name to load and extract text"""
    #fname = input("  Enter the name of the file :")
    data_str = ""
    try:
        with open(fname, encoding="utf8") as file:
            for line in file:
                data_str = data_str + line
                data_str = data_str.replace("\n"," ")
        #print("contents: ",data_str, type(data_str))
    except FileNotFoundError:
        print("\t Error with finding the file... exiting")
        exit()
    data_str = data_str.lower()
    #remove basic punctuation
    punctuation = "!`':,?.()/\\"
    for p in punctuation:
        data_str = data_str.replace(p," ")
    return data_str.split() # return a list
#end of getFile()



def studySentiment(text_list, sentiments_dict):
    """function to to determine the sentiment score from the text."""
    score = 0 # current score of the sentimental words
    hits = 0 # the number of words which have a sentiment value
    for i in text_list:
        #print("   Current word: ",i)
        try:
            wordScore_int = int(sentiments_dict[i])
            print("\t <<", i,">> : score: ",wordScore_int)
            score =  score + wordScore_int
            hits = hits + 1
        except KeyError:
            #print("  <<",i,">> Word not found in sentiments_dict...")
            pass

# give the summary of the analysis
    print( "\n\t Score by summation :",score)
    try:
        print("\t Number of sentiment words:",hits )
        print("\t Score/Hits:",score/hits)
    except ZeroDivisionError:
        #print("    Division by zero... :-(")
        pass
#end of studySentiment()


def wordFrequencies():
    print("\n\t wordFrequencies()")
    print("\t This is the function to determine")
    print("\t the frequencies of words in the text")
# end of wordFrequencies()

def frequencyPlotter():
    # libraries to load
    from pylab import plot, show, title, savefig, xlabel, ylabel, legend
    print("\n\t frequencyPlotter()")
    print("\t This is the frequency plotter function to ")
    print("\t plot the frequencies of word occurrence.")
# end of frequencyPlotter

def anotherAnalysis():
    print("\n\t anotherAnalysis()")
    print("\t This is my next analysis.")
# end of anotherAnalysis().

def begin(in_str, inFile = ""):
    """begin the program."""
    text_list = ""
    if in_str.lower() == "f":
        text_list = getFile(inFile)
    else:
        text_list = getSentence()

    #print( "  Contents : ", text_list, type(text_list))
    csvfile = "finn.csv"
    sentiments_dict = getSentiments(csvfile)
    print("\t Analyzing the sentiment score of text... ")
    studySentiment(text_list, sentiments_dict)
    wordFrequencies() # calculate and return a list of the word frequency values.
    frequencyPlotter() # now plot the words.
    anotherAnalysis() # this is my next analysis to do something amazing.

    # ADD ANOTHER ANALYSIS HERE # can you think of another type of analysis from class to add here?
#end of begin()



###################################
# code for command line paramters
###################################

import csv, sys, re
if __name__ == '__main__':

    if len(sys.argv)  == 2: #user enters a sentence
       #print( " Entering one parameter...")
        begin(sys.argv[1])
        exit()

    elif len(sys.argv) == 3: #two options ["f", "filename"] added to command line
       #print( " Entering two parameters...")
       begin(sys.argv[1],sys.argv[2])
    else:
       help()
       sys.exit(0)
