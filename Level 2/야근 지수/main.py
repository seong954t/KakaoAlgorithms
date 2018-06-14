def solution(n, works):
    works.sort()
    length = len(works)
    total = sum(works)
    if total <= n:
        return 0
    total -= n
    for i in range(length):
        if works[i] <= total//(length-i):
            total -= works[i]
        else:
            works[i:] = [total//(length-i)]*(length-i)
            works[length-total%(length-i):] = [x+1 for x in works[length-total%(length-i):]]
            break
    return sum([i*i for i in works])