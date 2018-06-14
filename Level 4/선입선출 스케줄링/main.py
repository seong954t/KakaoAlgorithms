def solution(n, cores):
    answer = 0
    idx = 0
    prev_idx = 0
    next_idx = 0
    br = 0
    while True:
        _sum = 0
        next_sum = 0
        for c in cores:
            _sum += idx//c+1
            next_sum += (idx+1)//c+1
            
        if _sum < n and next_sum >= n:
            break

        if _sum < n:
            prev_idx = idx
            if next_idx > 0:
                idx = (idx+next_idx)//2
            else:
                idx = (idx+1)*2
        else:
            next_idx = idx
            idx = (prev_idx+idx)//2
    
    _sum = 0
    for c in cores:
        _sum += idx//c+1
    
    idx += 1
    for c in cores:
        answer += 1
        if idx%c == 0:
            _sum += 1
        if _sum == n:
            break
            
    return answer