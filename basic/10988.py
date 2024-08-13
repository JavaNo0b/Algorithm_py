#심화1-팰린드롬인지 확인하기
alpha = input()
n = len(alpha)

isPel = True

if n%2 == 0:
  for i in range(0,n//2):
    if alpha[i] != alpha[n-i-1]:
      isPel = False
      break

else:
  for i in range(0,n//2-1):
    if alpha[i] != alpha[n-i-1]:
      isPel = False
      break
print(int(isPel))