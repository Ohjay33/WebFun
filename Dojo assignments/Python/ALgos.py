
def minMoves(arr, n):

    expectedItem = n

    for i in range(n - 1, -1, -1):
        if (arr[i] == expectedItem):
            expectedItem -= 1
    return expectedItem


arr = [3, 4, 9, 2, 4, -2, 3]
n = len(arr)
print(minMoves(arr, n))
