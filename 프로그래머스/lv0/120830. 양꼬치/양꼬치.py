def solution(n, k):
    price_f = 12000*n
    if n>=10 : 
        price_d = (k-n//10)*2000
    else : 
        price_d = k*2000
    answer = price_f+price_d
    return answer