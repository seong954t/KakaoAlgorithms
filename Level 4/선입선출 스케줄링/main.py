def solution(n, cores):
    row = 1
    total_sum = n-len(cores)
    # TODO :: ROW를 구하는데 시간이 오래걸림
    while total_sum > cal_row_val(row, cores):
        row += 1
    total_task = cal_row_val(row-1, cores)+len(cores)
    for idx in range(len(cores)):
        if row % cores[idx] == 0:
            total_task += 1
        if total_task == n:
            return idx+1

def cal_row_val(row, cores):
    result = 0
    for core in cores:
        result +=  row // core
    return result