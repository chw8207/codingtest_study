s = list(input())
alphbet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphbet : 
  if i in s : 
    print(s.index(i), end=' ')
  else : 
    print(-1, end=' ')