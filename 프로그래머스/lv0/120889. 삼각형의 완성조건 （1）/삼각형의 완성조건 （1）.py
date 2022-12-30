def solution(sides):
    # 오름차순으로 정렬
    sides.sort()
    if sides[-1]<(sides[-2]+sides[-3]) : 
        answer = 1
    else : 
        answer = 2
    return answer