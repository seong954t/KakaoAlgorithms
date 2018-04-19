def chooseCity(n,city):
    city.sort()
    answer = city[0][0]
    
    left = 0
    right = sum([i[1] for i in city])
    for i in range(n):
        left += city[i][1]
        right -= city[i][1]
        if left < right:
            answer = city[i+1][0]
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(chooseCity(3,[[1,5],[2,2],[3,3]]))