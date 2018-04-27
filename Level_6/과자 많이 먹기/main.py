def eatCookie(cookies):
    answer = [0 for i in range(len(cookies))]
    
    for i in range(len(cookies)):
        max_val = 0
        for j in range(i+1):
            if cookies[i] > cookies[j] and answer[j] > max_val:
                max_val = answer[j]
        answer[i] += max_val+1
    
    return max(answer)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(eatCookie([1, 4, 2, 6, 3, 4, 1, 5]))