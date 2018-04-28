def change(total, coin):
    answer = [[0 for i in range(len(coin))] for j in range(total)]
    for i in range(total):
        for j in range(len(coin)):
            if coin[j]-1 <= i:
                for k in range(j, len(coin)):
                    if coin[j]-1 == i:
                        answer[i][j] = 1
                    else:
                        answer[i][j] += answer[i-coin[j]][k]
    return sum(answer[total-1])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change(5, [1, 2, 5]))
