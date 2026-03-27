myList = [1,2,3,4,5,6,7,8,9]

def process():
    print(myList[0])        # 🎯 trigger
    print(myList[2])        # 🎯 trigger
    print(myList[0:5])      # 🎯 trigger
    
    myList.append(10)       # 🎯 trigger
    return myList           # 🎯 trigger

print(process())
