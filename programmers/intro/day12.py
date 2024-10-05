def solution(my_string):
    mo = 'aeiou'
    for i in mo:
        my_string = my_string.replace(i,'')
    return my_string
#     return "".join([i for i in my_string if not(i in "aeiou")])

def solution2(my_string):
    answer = [int(i) for i in my_string if i in '0123456789']
    return sorted(answer)

def solution3(n):
    answer = set()
    i = 2
    while n > 1:
        if n%i==0:
            answer.add(i)
            n/=i
            i=2
        else:
            i+=1
    return sorted(list(answer))