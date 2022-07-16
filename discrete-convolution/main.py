import numpy as np

def getNumbers():
  listNumbersOne = getListNumbers(".:: Enter a list of numbers (comma separated): ")
  listNumbersTwo = []

  question = input('.:: Do you want to use reverse to convolute? ')
  if(question in ['1', 'y', 'yes', 'sim', 's']):
    listNumbersTwo = [num for num in reversed(listNumbersOne)]
  else:
    listNumbersTwo = getListNumbers(".:: Enter a second list of numbers (comma separated): ")

  return [listNumbersOne, listNumbersTwo]

def getListNumbers(message):
  return list(map(int, input(message).split(',')))

def convolute(listNumbersOne, listNumbersTwo):
  print()
  numbers = []
  for idx, num in enumerate(listNumbersOne):
    numbers.append([0] * idx)
    for numRev in listNumbersTwo:
      numbers[idx].append(num * numRev)
    numbers[idx] = numbers[idx] + ([0] * (len(listNumbersOne) - idx - 1))
    print("+", ' '.join('{: >3}'.format(x) for x in numbers[idx]))
  
  return np.sum(numbers, axis=0)

def init():
  listNumbersOne, listNumbersTwo = getNumbers()
  
  print("\n => ", listNumbersOne, " * " , listNumbersTwo)
  
  convolution = convolute(listNumbersOne, listNumbersTwo)
  print("-------------------------------------------------------------------------------------")
  print(" ", ' '.join('{: >3}'.format(x) for x in convolution))

init()