def max_heapify(arr, i):
    n = len(arr)

    l = 2 * i + 1
    r = 2 * i + 2

    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def build_heap(arr):
    n = len(arr)

    lastLeftNode = (n // 2) - 1  # floor(n / 2) - 1
    for i in range(lastLeftNode, -1, -1):
        max_heapify(arr, i)


if __name__ == "__main__":
    # Test 1
    arr = [1, 2, 3, 4, 5]
    build_heap(arr)
    print(arr)

    # Test 2 with more complex array elements
    arr = [3, 4, 7, 11, 12, 14, 16, 17, 18, 20]
    build_heap(arr)
    print(arr)

    # Test 3
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    build_heap(arr)
    print(arr)
