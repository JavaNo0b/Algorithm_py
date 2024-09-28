# def solution(array):
#   array_sort = sorted(array)

#   answer = array_sort[len(array)//2]
#   return answer

# def solution(array):
#   my_dict = {}
#   for i in array:
#     if i in my_dict:
#       my_dict[i] += 1
#     else :
#       my_dict[i] = 1

#   max_value = max(my_dict.values())
#   result=[]
#   for key, value in my_dict.items():
#     if value==max_value:
#       result.append(key)

#   if len(result)==1:
#     return result[0]
#   else :
#     return -1


def solution(n):
  arr = []

  for i in range(1, n + 1):
    if i % 2 == 1:
      arr.append(i)
  return arr
