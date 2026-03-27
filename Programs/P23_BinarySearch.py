def wrapper(x):
    if x is None:
        return x                  # 🎯 trigger

    y = x + 1
    return y                      # 🎯 trigger


def runner():
    val = wrapper(5)
    return val                    # 🎯 trigger


print(runner())
