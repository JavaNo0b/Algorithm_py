# def solution(num_list):
#   answer = num_list[::-1]
#   return answer

# n = int(input())
# for i in range(1,n+1):
#   print('*'*i)

# def solution(num_list):
#   num1=[]
#   num2=[]
#   for num in num_list:
#     if num%2==0:
#       num2.append(num)
#     else:
#       num1.append(num)
#   answer = [len(num2),len(num1)]
#   return answer

def solution(my_string, n):
  my_string3 = map(lambda x: x*3, my_string)
  return my_string3