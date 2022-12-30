def solution(money):
    ice = money//5500
    ice_left = money%5500
    answer = [ice, ice_left]
    return answer