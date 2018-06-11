def solution(arr):
    if len(arr) == 1:
        return arr[0]
    gcd_val = arr[0]*arr[1]//gcd(arr[0], arr[1])
    arr.append(gcd_val)
    return solution(arr[2:])

def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    return gcd(b, a%b)