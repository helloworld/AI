from string import ascii_lowercase
from pprint import pprint
import pickle

'''
                        +======================+
                        |  Sashank Thupukari   |      
                        |  Period 6            |
                        |  Lab 2               |
                        |  9/9/2014            |
                        +======================+

      Objective: Create a dictionary with a list of six letter words as the 
      keys and their neighbors as the values.  
'''

def main():
    wordArray = openFile()
    dictionary = createDictionary(wordArray)
    #pprint(dictionary)
    checkNumWords(dictionary)
  
def openFile():
    fileName = "words.txt"
    wordFile = open (fileName, 'r')
    wordArray = wordFile.readlines()
    return wordArray

def createDictionary(wordArray):
    dictionary = {}
    for x in range(len(wordArray)):
        currentWord = wordArray[x].strip()
        dictionary[currentWord] = getNeighbors(currentWord, wordArray)
    return dictionary

def getNeighbors(word, wordArray):
    neighborArray = []
    for x in range(len(wordArray)):
        levenshteinDistance = 0
        currentWord = wordArray[x].strip()
        if not((word[0] != currentWord[0]) and (word[1] != currentWord[1]) and (word[2] != currentWord[2])):        
            for y in range(6):
                if(levenshteinDistance>1):
                    break
                if word[y] != currentWord[y]:
                    levenshteinDistance += 1
            if levenshteinDistance == 1:
                neighborArray.append(currentWord)
    return neighborArray

def saveFile(dictionary):
    dictFile = open("dictionary.txt", 'wb')
    pickle.dump(dictionary, dictFile)
    dictFile.close()

def checkNumWords(dictionary):
    print("Number of words in the dictionary: ", len(dictionary))
   
if __name__ == '__main__':
    from time import clock; START_TIME = clock(); main(); 
    print('\n+===<RUN TIME>===+');
    print('| %5.2f'%(clock()-START_TIME), 'seconds  |'); 
    print('+================+')
    
    
