<<<
def pascalRow(n):
    if n == 0:
        return [1]
    prev = pascalRow(n-1)
    return [1] + [prev[i] + prev[i+1] for i in range(n-1)] + [1]

def pascalTriangle(n):
    triangle = []
    for i in range(n):
        triangle.append(pascalRow(i))
    return triangle
===
def pascal_row(n):
    if n == 0:
        return [1]
    N = pascal_row(n-1)
    return [1] + [N[i] + N[i+1] for i in range(len(N)-1)] + [1]

def pascal_triangle(n):
    return [pascal_row(i) for i in range(n)]
>>>
