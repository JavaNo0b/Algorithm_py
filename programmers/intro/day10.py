# def solution(dot):
#   if dot[0]>0 and dot[1]>0:
#     return 1
#   elif dot[0]<0 and dot[1]>0:
#     return 2
#   elif dot[0]<0 and dot[1]<0:
#     return 3
#   else :
#     return 4

# def solution(num_list, n):
#   result = []  # 결과를 저장할 빈 리스트
#   for i in range(0, len(num_list), n):
#       result.append(num_list[i:i+n])  # n개씩 잘라서 추가
#   return result

def solution(numbers, k):
  return (1+(2*k))%numbers

def solution(numbers, K):
  # K번째 던지는 사람의 인덱스 계산
  index = (2 * (K - 1)) % len(numbers)
  return numbers[index]