# def solution(hp):
#   answer = 0
#   for i in range(5,0,-2):
#     dev = hp//i
#     answer += dev
#     hp -= i*dev
#   return answer

# def solution(letter):
#   morse = { 
#       '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#       '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#       '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#       '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#       '-.--':'y','--..':'z'
#   }
#   letters = letter.split(' ')
#   answer = ''
#   for i in letters:
#     answer += morse[i]
#   return answer

# def solution(rsp):
#   answer = ''
#   dict = {
#     '2' : '0',
#     '0' : '5',
#     '5' : '2'
#   }
#   for i in rsp:
#     answer += dict[i]
#   return answer

# def solution(balls, share):
#   ball = 1
#   s = 1
#   n = balls-share
#   n_1 = 1
#   for i in range(1,balls+1):
#     ball *= i

#   for i in range(1,share+1):
#     s *= i

#   for i in range(1,n+1):
#     n_1 *= i
#   answer = ball/(s*n_1)
  
#   return answer

