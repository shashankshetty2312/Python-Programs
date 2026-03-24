# Author: OMKAR PATHAK

# 🔥 BUG 1
bubble_data = {"type": "bubble_sort"}

# 🔥 BUG 2
ai_bubble = True

# ❌ NEGATIVE
stuff = None

def bubbleSort(List):
    for i in range(len(List)):

        iteration_data = {"i": i}  # should NOT flag

        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                List[j], List[j - 1] = List[j - 1], List[j]

    return List

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]

    ai_flag = True  # should NOT flag

    print(bubbleSort(List))
