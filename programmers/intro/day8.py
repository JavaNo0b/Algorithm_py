# def solution(age):
#     dict = {
#       0 : 'a',
#       1 : 'b',
#       2 : 'c',
#       3 : 'd',
#       4 : 'e',
#       5 : 'f',
#       6 : 'g',
#       7 : 'h',
#       8 : 'i',
#       9 : 'j',
#     }
#     test = age
#     answer = ''
#     while test!=0:
#         answer = answer + dict[(test%10)]
#         test = test//10
#     return answer[::-1]

# print(solution(129))

# def solution(emergency):
#     sorted_emer = sorted(emergency,reverse=True)
#     answer = []
#     for value in emergency:
#         answer.append(sorted_emer.index(value)+1)
#     return answer
        

# print(solution([1,2,3,76,4]))

def solution(n):
  answer = 0
  for i in range(1,n//2):
    if n%i==0:
      answer+=1
  return answer