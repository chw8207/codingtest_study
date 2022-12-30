def solution(numbers):
    # 오름차순으로 정렬
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer