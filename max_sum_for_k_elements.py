# Given an array of integers, find the maximum sum of K consequtive integers

def maxSumArr(arr, k):
    maxSum = sum(arr[0:k])

    for a in range(1, len(arr)):
        curSum = sum(arr[a:a+k])
        maxSum = max(maxSum, curSum)
    return maxSum


print(maxSumArr([2, 4, 6, 7, 8, 9, 8], 4))
