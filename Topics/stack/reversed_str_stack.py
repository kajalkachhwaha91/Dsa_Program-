str = "kajal"

lst =[]

for ch in str:
  lst.append(ch)
  
rev =""

while lst:
  rev+=lst.pop()
  
print(rev)
  