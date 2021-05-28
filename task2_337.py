# Написать функцию next_version, которая будет принимать строку (текущая версия программного обеспечения)
# и будет возвращать строку, содержащую следующий номер версии.
# Правила:
# все числа, кроме первого, должны быть меньше 10
# если после увеличения они становятся равными 10 - установите их в 0 и последовательно увеличите следующий номер
#
# Пример:
# next_version("1.2.3") ==> "1.2.4"
# next_version("0.9.9") ==> "1.0.0"


import traceback


def next_version(s):
    arr = []
    for i in range(0, len(s)):
        if s[i].isdigit():
            arr.append(int(s[i]))

    for i in range(0, len(arr)):
        arr[len(arr) - 1 - i] += 1
        if len(arr) - 1 - i != 0:
            if arr[len(arr) - 1 - i] == 10:
                arr[len(arr) - 1 - i] = 0
            else:
                break

    temp = ""
    if len(arr) > 1:
        for i in range(0, len(arr) - 1):
            temp += str(arr[i]) + "."
        temp += str(arr[len(arr) - 1])
    else:
        temp = str(arr[len(arr) - 1])
    return temp


# Тесты
try:
    assert next_version("1.2.3") == "1.2.4"
    assert next_version("0.9.9") == "1.0.0"
    assert next_version("1") == "2"
    assert next_version("1.2.3.4.5.6.7.8") == "1.2.3.4.5.6.7.9"
    assert next_version("9.9") == "10.0"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
