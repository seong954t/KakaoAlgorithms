def solution(arr1, arr2):
    for rowIdx in range(len(arr2)):
        for cellIdx in range(len(arr2[rowIdx])):
            arr1[rowIdx][cellIdx] += arr2[rowIdx][cellIdx]
    return arr1