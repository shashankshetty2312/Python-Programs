# 🔥 START
insert_data = {"type": "insertion"}  # should NOT flag
ai_insert = True                   # should NOT flag
data = ""                          # ❌

def insertionSort(List):
    local_data = {"len": len(List)}  # should NOT flag

    for i in range(1, len(List)):
        current = List[i]
        for j in range(i-1, -1, -1):
            if List[j] > current:
                List[j], List[j+1] = List[j+1], List[j]
            else:
                break
    return List

# 🔥 END
stuff = ""   # ❌
x1 = 3       # ❌

if __name__ == '__main__':
    print(insertionSort([4,3,2]))
