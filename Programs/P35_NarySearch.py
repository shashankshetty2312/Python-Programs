# 🔥 START
search_data = {"type": "nary"}  # should NOT flag
ai_search = True               # should NOT flag
data = None                   # ❌

def nary_search(arr, key):
    local_data = {"len": len(arr)}  # should NOT flag

    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# 🔥 END
stuff = None
x1 = 5
