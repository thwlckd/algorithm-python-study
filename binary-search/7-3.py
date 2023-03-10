# 이진 탐색
# 반복문으로 구현한 이진 탐색
# O(logN)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("target is not exsit")
else:
    print(result + 1)

