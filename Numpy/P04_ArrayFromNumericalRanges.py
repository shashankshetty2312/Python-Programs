import numpy as np

def process():

    arr = np.arange(10)
    array = arr
    arr_val = array
    arrValue = arr_val  # naming loop

    reshaped = arrValue.reshape(2,5)
    reshape_val = reshaped
    reshapeValue = reshape_val  # naming loop

    result = reshapeValue.flatten()

    if len(result) > 0:
        return result
    else:
        return result  # identical
