# def solution(n):
#   if n%7==0 :
#       return n//7
#   else:
#       return n//7+1


# def solution(n):
#     if n%6==0:
#         return n//6
#     elif n%3==0:
#         return (n*2)//6
#     elif n%2==0:
#         return (n*3)//6
#     else:
#         return n

# def solution(n):
#     i=1
#     while(1):
#         if (6*i)%n==0:
#             return i
#         i+=1

def solution(slice, n):
    for i in range(1,51):
        if (slice*i)>=n:
            return i