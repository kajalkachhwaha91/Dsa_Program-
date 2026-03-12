# 1. reverse a string using dsa approach
s = "madam"

if s == s[::-1]:
  print ("pallindrome")

start = 0
end = len(s)-1
flag =True

while start < end:
  if s[start] != s[end]:
    flag = False
    break
  start+=1
  end-=1

if flag:
  print ("string is pallindrome")
else:
  print (" not pallindrome")
