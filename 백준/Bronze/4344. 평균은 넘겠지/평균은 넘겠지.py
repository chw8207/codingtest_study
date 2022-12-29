c = int(input())
for _ in range(c) : 
  score = list(map(int, input().split()))
  avg = sum(score[1:])/score[0]

  count = 0
  for i in score[1:] : 
    if i>avg : 
      count += 1
    ratio = count/score[0]*100
  print(f'{ratio:.3f}%')