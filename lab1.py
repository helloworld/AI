from string import ascii_lowercase

'''
                        +======================+
                        |  Sashank Thupukari   |      
                        |  Period 6            |
                        |  Lab 2               |
                        |  9/5/2014            |
                        +======================+

      Objective: Find the neighbors of a word.   
'''

fileName = "words.txt"
file1 = open (fileName, 'r')
target = input("Enter target String: ")
total = 0

for x in range(5000):
  distance = 0
  currentWord = file1.readline().strip()
  for y in range(6):
    if target[y] != currentWord[y]:
      distance += 1
  if distance == 1:
    print(currentWord)
    total+=1
    
print(total)
 

    
    
    
