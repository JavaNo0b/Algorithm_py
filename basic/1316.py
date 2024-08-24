#심화1-그룹 단어 체커
n = int(input())
arr = ["none"]*n
sum = 0

for i in range(0,n):
  word = input()
  for j in range(len(word)):
    if j == len(word)-1:
      sum += 1
    elif word[j] == word[j+1]:
      pass
    elif word[j] in word[j+2:]:
      break
print(sum)
