import numpy as np

def polynomialCapture():
  print(".:: Consider that the polynomial p(x) = ax^2 + bx + c will be represented by the input (c, b, a). \n")

  coefficientsFirstPolynomial = captureCoefficientsPolynomial(".:: Enter the list of coefficients of the first polynomial (comma separated): \n => ")
  coefficientsSecondPolynomial = []
  
  question = input('.:: Want to use the inverse to set up the second polynomial? \n => ')
  if(question in ['1', 'y', 'yes', 'sim', 's']):
    coefficientsSecondPolynomial = [num for num in reversed(coefficientsFirstPolynomial)]
  else:
    coefficientsSecondPolynomial = captureCoefficientsPolynomial(".:: Enter the coefficients of the second polynomial (comma separated): \n => ")

  return [coefficientsFirstPolynomial, coefficientsSecondPolynomial]
  
def captureCoefficientsPolynomial(message):
  return list(map(int, input(message).split(',')))

def buildPolynomialPrinting(coefficients):
  polynomial = ""
  for idx, num in enumerate(coefficients):
    polynomial += f"{num}x^{idx}"
    if(idx < len(coefficients) -1):
      polynomial += " + "
  return polynomial
  
def init():
  coefficientsFirstPolynomial, coefficientsSecondPolynomial = polynomialCapture()
  print("\n   (" + buildPolynomialPrinting(coefficientsFirstPolynomial)+")")
  print(" × (" +buildPolynomialPrinting(coefficientsSecondPolynomial)+")\n")
  
  polynomial = np.polynomial.polynomial.polymul(coefficientsFirstPolynomial, coefficientsSecondPolynomial)

  print(".:: Result: \n\n => Polynomial: " + buildPolynomialPrinting(polynomial) + "\n\n => Coefficients: ", polynomial)

init()