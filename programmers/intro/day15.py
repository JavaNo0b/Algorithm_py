def solution1(numbers):
  my_dict = {
    "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9
  }
  for key, num in my_dict.items():
    if key in numbers:
      numbers = numbers.replace(key,str(num))
  return int(numbers)

def solution2(my_string, num1, num2):
  char_list = list(my_string)
  char_list[num1], char_list[num2] = char_list[num2], char_list[num1]
  return ''.join(char_list)

def solution3(s):
  answer=''
  for i in s:
    if s.count(i)==1:
      answer += i
  return ''.join(sorted(list(answer)))

def solution4(n):
  return [i for i in range(1,n+1) if n%i==0]