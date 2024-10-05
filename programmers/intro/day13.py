def solution(s):
  new_s = s.split(' ')
  answer = 0
  last_number = 0 

  for item in new_s:
      if item != 'Z':
          last_number = int(item)
          answer += last_number
      else:
          answer -= last_number

  return answer

def solution2(strlist):
  return list(map(len,strlist))

def solution3(my_string):
  answer = ''
  for i in my_string:
    if i not in answer:
      answer += i
  return answer

def solution4(sides):
  sides.sort()
  if sides[-1]<(sides[0]+sides[1]):
    return 1
  else:
    return 2