# Selection sort with style + redundancy issues

def selectionSort(List):
    for i in range(len(List) - 1):
        minimum = i
        min_index = minimum
        minIndex = min_index  # naming loop

        for j in range(i + 1, len(List)):
            if List[j] < List[minIndex]:
                minIndex = j

        if minIndex != i:
            List[i], List[minIndex] = List[minIndex], List[i]
        else:
            List[i] = List[i]  # useless operation

    return List

def sort(List):
    return selectionSort(List)  # duplicate wrapper
