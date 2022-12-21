k, q, l, b, n, p = map(int, input().split())
if(k, q, l, b, n, p) != (1, 1, 2, 2, 2, 8) : 
    print(1-k, 1-q, 2-l, 2-b, 2-n, 8-p)
else :
    print(0, 0, 0, 0, 0, 0)