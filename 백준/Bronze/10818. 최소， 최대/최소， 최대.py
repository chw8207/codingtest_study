# 정수의 개수, n개의 정수 선언
n = int(input())
array_list = list(map(int, input().split()))

# 최소, 최대값 초기화 
max_num = array_list[0]
min_num = array_list[0]

# 최소, 최대 반복문
for num in array_list : 
  if num > max_num : 
    max_num = num
  if num < min_num : 
    min_num = num

# 최소, 최대값 출력
print(min_num, max_num)