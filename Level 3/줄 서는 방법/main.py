def solution(n, k):
    prev = [i for i in range(1, n+1)]
    answer = []
    idx = 0
    fac = 1
    for i in range(1, n+1):
        if fac*i > k:
            break
        fac *= i
        idx = i
    answer = prev[:n-idx-1]
    prev = prev[n-idx-1:]
    while idx != 0:
        answer.append(prev[(k-1) // fac])
        prev.remove(prev[(k-1) // fac])
        k %= fac
        fac //= idx
        idx -= 1
    return answer+prev