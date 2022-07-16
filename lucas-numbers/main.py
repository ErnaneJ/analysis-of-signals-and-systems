import numpy as np

def beta(n):
  return pow(-1, n) * np.linalg.det(generateMatrix(n))
  
def lucasNumber(n): 
  return 2 * beta(n) - beta(n - 1)
  
def generateMatrix(n):
  base = np.zeros((n,n), dtype=np.float64)
  
  for i, el_i in enumerate(base):
    for  j, el_j in enumerate(el_i):
      if(i == j or j == (i + 1.0)):
        base[i][j] = -1
      elif(j == i - 1.0):
        base[i][j] = 1
  return base

def init():
  n = int(input(".:: How many numbers of Lucas do you want to view: "))
  numbers = []
  for i in range(2, n+1):
    numbers.append(f"{lucasNumber(i):.1f}")

  print(f".:: Lucas numbers starting from 2 to {n}:\n\n => [",", ".join(numbers), "].")
init()