# 🔥 START
bubble_data = {"type": "bubble"}  # should NOT flag
ai_bubble = True                 # should NOT flag
data = None                      # ❌

def bubbleSort(List):
    loop_data = {"len": len(List)}   # should NOT flag

    for i in range(len(List)):
        for j in range(len(List)-1, i, -1):
            if List[j] < List[j-1]:
                List[j], List[j-1] = List[j-1], List[j]
    return List

# 🔥 END
stuff = None   # ❌
x1 = 2         # ❌

if __name__ == '__main__':
    print(bubbleSort([5,2,1]))
