def solution(nums):
    decimal = [False, True]+[True]*3000
    answer = 0
    sums = []
    length = len(nums)
    for i in range(2, 200):
        for j in range(i*i, 3001, i):
            decimal[j] = False
            
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                sums.append(nums[i]+nums[j]+nums[k])
    
    for row in sums:
        if decimal[row]:
            answer += 1
    
    return answer