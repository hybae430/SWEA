def quicksort(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

m1 = [11, 45, 23, 81, 28, 34]
m2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
m3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

quicksort(m1)
print(m1)
quicksort(m2)
quicksort(m3)