from string import ascii_lowercase
from pprint import pprint
import pickle

'''
                        +======================+
                        |  Sashank Thupukari   |      
                        |  Period 6            |
                        |  Lab 3               |
                        |  9/11/2014           |
                        +======================+

      Objective: Use the dictionary to find the path from one word to the
      next using neighbors. 
'''

def main():
    dictionary = openFile()
    start = "spider"
    end = "guides"
    addFields(dictionary)
    dictionary = createPath(dictionary, start, end)
    path = tracePath(dictionary, start, end)
    print(path)


def openFile():
    dictFile = open("dictionary.txt", 'rb')
    dictionary = pickle.load(dictFile)
    dictFile.close()
    return dictionary

def addFields(dictionary):
    for key in dictionary:
        dictionary[key] = [dictionary[key], 0, "NONE"]

def createPath(dictionary, start, end):
    queue = []
    queue.append(start)
    dictionary[start][1] = 1
    while not(end in queue):
        currentWord = queue.pop(0)
        for x in range( len(dictionary[currentWord][0]) ):
            currentNeighbor = dictionary[currentWord][0][x]
            if(dictionary[currentNeighbor][1] == 0):
                dictionary[currentNeighbor][1] = 1
                dictionary[currentNeighbor][2] = currentWord
                queue.append(currentNeighbor)
    return dictionary

def tracePath(dictionary, start, end):
    queue = []
    queue.append(end)
    while(dictionary[queue[0]][2] != "NONE"):
        queue.insert(0, dictionary[queue[0]][2])
    return(queue)


if __name__ == '__main__':
    from time import clock; START_TIME = clock(); main(); 
    print('\n+===<RUN TIME>===+');
    print('| %5.2f'%(clock()-START_TIME), 'seconds  |'); 
    print('+================+')
    
    
