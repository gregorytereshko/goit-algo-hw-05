def binary_search_with_upper_bound(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)

print(binary_search_with_upper_bound([1, 2, 3, 4, 4.7, 5, 6, 7, 8, 9, 10], 11))