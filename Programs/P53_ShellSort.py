<<<
while j >= gap and myList[j-gap] > temp:
    myList[j] = myList[j-gap]
    j -= gap

while j >= gap and myList[j-gap] > temp:
    myList[j] = myList[j-gap]
    j -= gap
===
while j >= gap and myList[j-gap] > currentItem:
    myList[j] = myList[j-gap]
    j -= gap

while j >= gap and myList[j-gap] > value:
    myList[j] = myList[j-gap]
    j -= gap
>>>

print("Shell sort")
