def solution(box, n):
  answer = 1
  for i in box:
    answer *= (i//n)
  return answer

def solution2(n):
  answer = 0
  for i in range(2,n):
      if n%i==0:
        answer += 1
  return answer
  # return sum(1 for i in range(2, n) if n % i == 0)

def solution2_2(n):
  answer = 0
  for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
          answer += 1
          break
  return answer

def solution3(numbers):
  numbers.sort()
  return numbers[len(numbers)-1]*numbers[len(numbers)-2]

def solution4(n):
  i = 1
  while n>=fac(i):
    i += 1
  return i-1

def fac(i):
  fact = 1
  for k in range(1,i+1):
    fact*=k
  return fact