def divisorCount(x):
   divs = 1
   i = 1
   while i <= x:
      if x % i == 0:
         divs += 1
      i += 1
   return divs

def weakNumbers(n):
   nDiv = divisorCount(n)
   weakest = divisorCount(1)
   num_weakest = 0
   for i in range(n):
      iDiv = divisorCount(i)
      if iDiv > nDiv and iDiv > weakest:
         weakest = iDiv
   
   return weakest
