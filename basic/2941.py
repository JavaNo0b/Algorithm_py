#심화1-크로아티아 알파벳
word = input()
cro_spell = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in cro_spell:
  if i in word:
    word = word.replace(i,"*")
    
print(len(word))