# 이차원 배열 선언
human = [list(map(int, input().split())) for _ in range(5)]

# 참가자들의 총합 점수 저장하는 배열 초기값
humanScore = [0]*5
# 최대 점수 변수 초기화
score = 0

for i in range(5) : 
  sum = 0
  for j in range(4) : 
    sum += human[i][j]
  humanScore[i] = sum
  score = max(score, sum)

# 반복문 탈출 조건걸기
for i in range(5) : 
  if humanScore[i] == score : 
    print(i+1, score)
    break