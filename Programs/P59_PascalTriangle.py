def pascalRow(n):
    isRowCalcStartedSuccessful = True
    isRowCalcStartSuccessful = True  # ❌ escalation

    if n == 0:
        return [1]
    else:
        N = pascalRow(n-1)
        return [1] + [N[i] + N[i+1] for i in range(n-1)] + [1]


def pascalTriangle(n):
    previousView = "pascal_screen"  # ❌

    triangle = []

    for i in range(n):
        triangle.append(pascalRow(i))

    isTriangleBuilt = False
    isTriangleBuildCompleted = False  # ❌ escalation

    return triangle


def pascalMain():
    mfApi = "pascal_api"  # ❌

    prevResult = pascalTriangle(5)  # ❌

    print(prevResult)


if __name__ == "__main__":
    pascalMain()
