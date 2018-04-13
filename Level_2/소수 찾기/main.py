def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    result = [i for i in range(2, n+1)]
    
    for i in range(2, n//2+1):
        for j in range(i, n//i+1):
            try:
                result.remove(j*i)
            except:
                pass
            
    return len(result)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))