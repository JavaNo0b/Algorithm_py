def solution1(num, k):
  if str(k) in str(num):
    return str(num).index(str(k))+1
  else :
    return -1

def solution2(n, numlist):
  return [i for i in numlist if i%n==0]

def solution3(n):
  return sum([int(i) for i in str(n)])

def solution4(quiz):
  answer = []
  for q in quiz:
    q = q.split(' ')
    if oper(q[0],q[1],q[2])==int(q[4]):
      answer.append('O')
    else:
      answer.append('X')
  return answer

def oper(a,op,b):
  if op == '-':
    return int(a)-int(b)
  else:
    return int(a)+int(b)