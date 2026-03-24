# 🔥 Trigger Block
is_search_executed_successfully = True
has_search_been_executed_successfully = True

if isSearchExecutedSuccessful and hasSearchBeenExecutedSuccessfully:
    pass

data = b"x"
val1 = data.decode('utf-8')
val2 = data.decode("utf-8")


# Original Code
def sequentialSearch(target, List):
    position = 0
    while position < len(List):
        if target == List[position]:
            return position
        position += 1
    return -1
