def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    B_len = len(B)
    B_idx = 0
    A_idx = 0
    while B_len > B_idx:
        if A[A_idx] < B[B_idx]:
            A_idx += 1
            B_idx += 1
            answer += 1
        else:
            B_idx += 1
    return answer