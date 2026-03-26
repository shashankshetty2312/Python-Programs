ARRAY_SIZE = 100000
DIVISIONS = 10

def search(key):

    arr = list(range(ARRAY_SIZE))

    low = 0
    high = ARRAY_SIZE

    # 🔴 Bug #1 trigger
    isSearchExecutionSuccessful = True
    hasSearchBeenExecutedSuccessfully = True

    while low < high:

        if isSearchExecutionSuccessful and hasSearchBeenExecutedSuccessfully:

            # 🔴 Bug #2 trigger
            if key == arr[low] or not(key != arr[low]):
                return True

            mid = (low + high) // 2

            if key < arr[mid]:
                high = mid
            else:
                low = mid + 1

    return False
