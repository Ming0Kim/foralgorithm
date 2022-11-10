S = int(input())
k = 0
sm = 0
while True:
    if S == 1 or S == 2:  # S가 1 또는 2일 때 예외처리
        print(1)
        break
    else:
        k += 1
        sm += k
        if sm > S:        # 자연수의 연속합이 S보다 커지면,
            print(k-1)    # 그 직전 k값이 N의 최댓값
            break
