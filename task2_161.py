# Написать функцию vowel_2_index, которая заменяет все гласные (a, e, i, o, u)
# в заданной строке на число – порядковый номер буквы в строке
#
# Примеры:
# vowel_2_index("this is my string") ==> "th3s 6s my str15ng"

import traceback


def vowel_2_index(s):
    str_change = "aeiou"
    temp = ""
    for i in range(0, len(s)):
        boolean = True
        for l in str_change:
            if s[i] == l:
                temp += str(i+1)
                boolean = False
                break
        if boolean:
            temp += s[i]
    return temp


# Тесты
try:
    assert vowel_2_index("this is my string") == "th3s 6s my str15ng"
    assert vowel_2_index("Tomorrow is going to be raining") == "T2m4rr7w 10s g1415ng t20 b23 r2627n29ng"
    assert vowel_2_index("") == ""
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
