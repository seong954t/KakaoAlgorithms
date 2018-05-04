def matrix(element):
    answer = 9223372036854775807;
    if len(element) == 2:
        return element[0][0]*element[0][1]*element[1][1]
    for i in range(len(element)-1):
        val = matrix(element[:i]+ [[element[i][0], element[i+1][1]]]+ element[i+2:])+(element[i][0]*element[i][1]*element[i+1][1])
        if answer > val:
            answer = val
    return answer;


# 실행을 위한 테스트코드입니다.
if matrix([[5, 3], [3, 2], [2, 6]]) == 90:
    print("[[5,3],[3,2],[2,6]]인 경우에 정상동작합니다. 제출을 눌러서 다른 경우에도 정답인지 확인해 보세요.")
else:
    print("[[5,3],[3,2],[2,6]]인 경우에 정상동작하지 않습니다.")