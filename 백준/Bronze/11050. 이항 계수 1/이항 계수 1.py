# n, k 입력받기
n, k = list(map(int, input().split()))

# n! 구현하기
up = 1
for i in range(1, n+1) : 
  up *= i

# (n-k)! 구현하기
down = 1
for i in range(1, n-k+1) : 
  down *= i

# k! 구현하기
down2 = 1
for i in range(1, k+1) : 
  down2 *= i

# k!(n-k)! 구하기
down *= down2

# 조합 구해서 출력
print(up//down)