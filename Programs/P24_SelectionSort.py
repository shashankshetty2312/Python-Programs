# 🔥 START
sort_data = {"type": "selection"}  # should NOT flag
ai_sort = True                    # should NOT flag
data = 0                          # ❌

def selectionSort(List):
    local_data = {"len": len(List)}   # should NOT flag

    for i in range(len(List) - 1):
        minimum = i
        for j in range(i + 1, len(List)):
            if List[j] < List[minimum]:
                minimum = j
        if minimum != i:
            List[i], List[minimum] = List[minimum], List[i]
    return List

# 🔥 END
stuff = []   # ❌
x1 = 1       # ❌

if __name__ == '__main__':
    print(selectionSort([3,1,2]))
