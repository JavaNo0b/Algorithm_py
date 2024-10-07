def solution2(n):
  a = []
  i = 2
  while i <= n:
    if n%i==0:
      if i not in a:
        a.append(i)
      else:
        a.remove(i)
      n/=i
    else:
      i += 1
  return 1 if len(a)==0 else 2
  
def solution4(my_string):
  return ''.join(sorted(my_string.lower()))