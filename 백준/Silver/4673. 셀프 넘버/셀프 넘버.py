# d(n)함수
def d(n) : 
  n = n + sum(map(int, str(n)))
  return n

# 셀프 넘버가 아닌 수들의 집합
NotSelf = set()

# 셀프넘버 아닌거 찾아서 집합에 넣기
for i in range(1, 10001) : 
  NotSelf.add(d(i))

# 셀프넘버 찾아서 출력하기
for j in range(1, 10001) : 
  if j not in NotSelf : 
    print(j)