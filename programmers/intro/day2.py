# def solution(num1, num2):
#   answer = (int)((num1/num2)*1000)
#   return answer

# def solution(num1, num2):
#   if num1==num2:
#       return 1
#   else :
#       return -1

def solution(numer1, denom1, numer2, denom2):

  denom = denom1*denom2
  numer = (numer1*denom2) + (numer2*denom1)
  smaller = denom if denom<numer else numer
  
  for i in range(2,smaller+1) :
      while True : 
          if numer%i==0 and denom%i==0 :
              numer=numer/i
              denom=denom/i
          else : 
            break
  
  answer = [numer,denom]
  return answer

# def multi(i):
#   return i*2
# def solution(numbers):
#   answer = map(multi,numbers)
#   return list(answer)