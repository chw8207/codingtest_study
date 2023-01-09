n = int(input())

# 피보나치 재귀함수 구현
def fibonach(n) : 
  if n<=1 : 
    return n
  else : 
    return fibonach(n-2) + fibonach(n-1)
print(fibonach(n))