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





