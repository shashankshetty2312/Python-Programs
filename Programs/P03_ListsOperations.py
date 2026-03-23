# 🔥 FIX 1
list_data = {"type": "list"}

# 🔥 FIX 2
ai_list = True

# ❌ NEGATIVE
stuff = []

myList = [1,2,3,4,5,6,7,8,9]

print(myList)

user_data = {"length": len(myList)}  # should NOT flag

myList.append(10)
print(myList)

print(myList.pop())
