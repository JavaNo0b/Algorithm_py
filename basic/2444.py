# 심화1-별찍기
n=input()

for i in range(1,int(n)*2):
  x=" "*(int(n)-i) if int(n)>i else " "*(i-int(n))
  y="*"*(2*i-1) if int(n)>i else "*"*(2*(int(n)*2-i)-1)
  print(x+y)
