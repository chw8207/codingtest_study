a, b, c = map(int, input().split())

def profit(a,b,c) : 
  if b>=c : 
    print(-1)
  else : 
    print(int(a/(c-b)+1))

profit(a, b, c)