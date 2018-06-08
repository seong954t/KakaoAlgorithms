def solution(land, P, Q):
    answer = 0
    linear_land = sum(land, [])
    linear_land.sort()
    N_square = len(land)**2
    max_count = int((N_square*Q)/(Q+P))
    small = linear_land[:max_count]
    big = linear_land[max_count:]
    mid = linear_land[max_count]
    answer += ((mid*len(small) - sum(small))) * P
    answer += (sum(big) - (mid*len(big))) * Q
    
    return answer