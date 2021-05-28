# Написать функцию odd_numbers, которая получает на вход список целых чисел arr и целое число n и
# возвращает список, состоящий из n последних вхождений нечетных чисел списка arr в том же порядке
#
# Пример:
# ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [5, 7, 9]


import traceback


def odd_numbers(arr, n):
    new_arr = []
    for i in range(0, len(arr)):
        if len(new_arr) == n:
            break
        elif arr[(len(arr) - i - 1)] % 2 == 1:
            new_arr.append(arr[len(arr) - i - 1])
    arr = []
    for i in range(0, len(new_arr)):
        arr.append(new_arr[len(new_arr) - 1 - i])
    return arr


# Тесты
try:
    assert odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [7, 9]
    assert odd_numbers([-15, 3, 6, 9, 12, -24, -81, 7], 3) == [9, -81, 7]
    assert odd_numbers([6, -25, 3, 7, 5, 5, 7, -3, 24], 1) == [-3]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
