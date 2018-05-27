def solution(d, budget):
    answer = 0
    d.sort()
    budgetVal = 0
    for dd in d:
        budgetVal += dd
        if budgetVal > budget:
            break
        answer += 1
    return answer