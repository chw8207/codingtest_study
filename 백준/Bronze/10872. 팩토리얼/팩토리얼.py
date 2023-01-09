# 팩토리얼 출력하기
n = int(input())

# 팩토리얼 재귀함수 구현
def factorial_recursive(n) : 
  if n<=1 : 
    return 1
  else : 
    return n * factorial_recursive(n-1)
print(factorial_recursive(n))