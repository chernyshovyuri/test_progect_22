def sum_1d(arr: list) -> float | bool:


    if len(arr) == '':
        return False

    summ = 0
    for numb in arr:
        summ += numb

    return summ


def prod_1d(arr: list) -> float | bool:

    if len(arr) == '':
        return False

    prod = 0

    for numb in arr:
        prod = prod * numb
    return prod



def mean_1d(arr: list) -> float | bool:

    if len(arr) == '':
        return False

    summ = 0
    count = 0

    for numb in arr:
        summ += numb
        count += 1

    rezult = summ / count

    return rezult


def max_1d(arr: list) -> float | bool:

    if len(arr) == '':
        return False

    max = arr[0]

    for i in range (1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max

