def solution(land):
    result = [land[0], land[1]]
    prev = 0
    current = 1
    size = len(land[0])
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는? 
    for row in land[1:]:
        for i in range(size):
            result[current][i] = max(result[prev][:i]+result[prev][i+1:])+row[i]
        prev, current = current, prev
    return max(result[prev])