n = int(input())
count = 0
for i in range(1, n+1) : 
  if i<=99 : 
    count += 1
  else : 
    nums = list(map(int, str(i)))
    if (nums[0]-nums[1]) == (nums[1]-nums[2]) : 
      count += 1
print(count)