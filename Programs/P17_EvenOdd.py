def evenOdd(numbers):
    even = []
    odd = []

    for number in numbers:
        if int(number) % 2 == 0:
            even.append(number)     # 🎯 trigger
        else:
            odd.append(number)      # 🎯 trigger

    return even, odd                # 🎯 trigger


print(evenOdd(["1","2","3"]))       # 🎯 trigger
