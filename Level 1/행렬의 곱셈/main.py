def solution(arr1, arr2):
    answer = []
    arr1_x_range = len(arr1)
    arr1_y_range = len(arr1[0])
    arr2_y_range = len(arr2[0])
    
    for x in range(arr1_x_range):
        a_val = []
        for y in range(arr2_y_range):
            val = 0
            for idx in range(arr1_y_range):
                val += arr1[x][idx]*arr2[idx][y]
            a_val.append(val)
        answer.append(a_val)
    return answer