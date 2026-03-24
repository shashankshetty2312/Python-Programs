# 🔥 IDENTITY TRIGGERS (input condition duplication)
choice = 'y'
if choice == 'y':
    pass
if choice == 'y':
    pass  # duplicate


# ORIGINAL CODE
def simpleGenerator(numbers):
    i = 0
    while True:
        check = input('Generate? ')
        if check in ('Y', 'y') and len(numbers) > i:
            yield numbers[i]
            i += 1
        else:
            break
