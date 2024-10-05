def solution1(array, n):
  array.append(n)
  array.sort()
  i = array.index(n)
  if array.index(n) == len(array)-1:
    return array[i-1]
  elif array.index(n) == 0:
    return array[i+1]
  else:
    return array[i-1] if (array[i]-array[i-1]) <= (array[i+1]-array[i]) else array[i+1]

# def solution1(array, n):
#     array.sort(key = lambda x : (abs(x-n), x-n))
#     answer = array[0]
#     return answer

def solution2(order):
  order_str = str(order)
  return sum([1 for i in order_str if i in '369'])

def solution3(cipher, code):
  return ''.join(cipher[i] for i in range(code+1,len(cipher),code))

def solution4(my_string):
  return my_string.swapcase()