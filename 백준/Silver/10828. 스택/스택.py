import sys
n = int(sys.stdin.readline())

# 스택을 활용하기 위한 변수 생성
stack = []
for i in range(n) :
    # 명렁어 한 줄씩 입력받기
    command = sys.stdin.readline().split()

    # 명령어가 push라면 숫자를 넣는다.
    if command[0]=='push' :
        stack.append(command[1])
    elif command[0] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif command[0] == 'size' :
        print(len(stack))
    elif command[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif command[0] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])