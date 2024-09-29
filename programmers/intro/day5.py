# def solution(price):

#   if price<100000:
#     return price
#   elif price<300000:
#     return int(price*0.95)
#   elif price<500000:
#     return int(price*0.9)
#   else: 
#     return int(price*0.8)

def solution(money):
  answer = [money//5500, money%5500]
  return answer