def solution(my_string):
  m = my_string.split(' ')
  result = int(m[0])
  
  for i in range(1, len(m), 2):
      operator = m[i] 
      number = int(m[i + 1])

      if operator == '+':
          result += number
      elif operator == '-':
          result -= number

  return result