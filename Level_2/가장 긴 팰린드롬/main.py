def solution(s):
    answer = 0
    input_len = len(s)
    palindrom = [[1 for i in range(input_len)] for j in range(input_len)]
    for i in range(2, input_len, 2):
        palindrom[i] = palindrom[i-2]
        for j in range(i//2, input_len-i//2):
            if s[j-i//2] == s[j+i//2]:
                if palindrom[i-2][j] == i-1:
                    palindrom[i][j] = palindrom[i-2][j]+2
    
    for i in range(input_len-1):
        if s[i] == s[i+1]:
            palindrom[1][i] = 2
    
    for i in range(input_len-1):
        if s[i] == s[i+1]:
            palindrom[1][i] = 2
    for i in range(3, input_len, 2):
        palindrom[i] = palindrom[i-2]
        for j in range((i-1)//2, input_len-((i-1)//2)-1):
            if s[j-((i-1)//2)] == s[j+((i-1)//2)+1]:
                if palindrom[i-2][j] == i-1:
                    palindrom[i][j] = palindrom[i-2][j]+2
    answer = [max(palindrom[input_len-1]), max(palindrom[input_len-2])]
    return max(answer)