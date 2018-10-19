def evens(numbers):
  evens = []
  for i in numbers:
    if i % 2 == 0:
      evens.append(i)
  return evens

def odds(numbers):
  return [i for i in numbers if i % 2 != 0]
   
test = [0,1,2,3,4,5,6,7,8,9,10,11,77,88,33]

print(evens(test))
print(odds(test))
