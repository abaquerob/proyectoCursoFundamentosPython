
# Python3 program to calculate 
# least common multiple (LCM) of 
# a n integers given on the screen
# 2 <= n <= 10. The integers can be 
# positive or negative.

import itertools 
options = (2,3,4,5,6,7,8,9,10)

while True:
  print("*" * 10)
  print('Program to calculate \nleast common multiple (LCM) of') 
  print('n integers given on the screen \n2 <= n <= 10')
  print('The integers can be positive or \nnegative.')
  print('n and each integer are requested \nindividually on the screen.')	
  amount_numbers = int(input("Enter the value of n: "))
  if not amount_numbers in options:
    print('that option is not valid')
    continue
  
  list_numbers=[]
  tuple_numbers={}

  #The integers that will be taken into 
  #account to calculate the LCM are requested 
  #and value0 is calculated, a value that will 
  #determine the sign of the LCM value
  value0 = 1
  for i in range(amount_numbers):
    template = "Enter value #{}: ".format(i+1)
    value1 = int(input(template))
    value = [value1]
    list_numbers.append(value)
    value0 = value0 * value1
  
  print("list_numbers", list_numbers)
  tuple_numbers = tuple(list_numbers)
  
  # Initializes the 10 integers 
  while len(list_numbers) != 10: list_numbers.append([1])
  #print("list_numbers", list_numbers)
  #print("." * 10)
  
  A = list_numbers[0] 
  B = list_numbers[1]
  C = list_numbers[2] 
  D = list_numbers[3]
  E = list_numbers[4]
  F = list_numbers[5] 
  G = list_numbers[6]
  H = list_numbers[7]  
  I = list_numbers[8] 
  J = list_numbers[9]    
 
  A = [abs(aux) for aux in A]
  B = [abs(aux) for aux in B]
  C = [abs(aux) for aux in C]
  D = [abs(aux) for aux in D]
  E = [abs(aux) for aux in E]
  F = [abs(aux) for aux in F]
  G = [abs(aux) for aux in G]
  H = [abs(aux) for aux in H]
  I = [abs(aux) for aux in I]
  J = [abs(aux) for aux in J]

  # calculates the prime factors iterating over 
  # the 10 lists and until all are exhausted
  co = 2
  list_factors = []
  
  for (a, b, c, d, e, f, g, h, i, j) in itertools.zip_longest(A, B, C, D, E, F, G, H, I, J):
    #print (a, b, c, d, e, f, g, h, i, j)
    while (a+b+c+d+e+f+g+h+i > 10):
      if(a % co == 0 or b % co == 0 or c % co == 0 or d % co == 0 or e % co == 0 or f % co == 0 or g % co == 0 or h % co == 0 or i % co == 0):  
          list_factors.append(co)
          if(a % co == 0): 
            a = a / co
          if(b % co == 0): 
            b = b / co
          if(c % co == 0): 
            c = c / co  
          if(d % co == 0): 
            d = d / co
          if(e % co == 0): 
            e = e / co
          if(f % co == 0): 
            f = f / co  
          if(g % co == 0): 
            g = g / co
          if(h % co == 0): 
            h = h / co
          if(i % co == 0): 
            i = i / co  
  
            #print ("co, a, b, c dentro de if", co, a, b, c)
      else:
        if(co == 2):
          co = co + 1
        else:
          co = co + 2
        #print ("co, a, b, c dentro de else", co, a, b, c)

  print("Common and uncommon prime factors")
  template = "of {}, greater than 1: ".format(tuple_numbers)
  print(template)
  print(list_factors)
  
  # calculate the least common multiple
  i = 0
  prod = 1
  while i < len(list_factors):
      prod = prod * list_factors[i]
      i += 1
  if (value0 < 0):
    prod = -1*prod    
  if (amount_numbers > 1):     
    print("LCM: ", prod)     
    break