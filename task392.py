# В начале года население города – p0.
# Каждый год население увеличивается на percent процентов,
# а также дополнительно в город приезжают жить aug человек.
# Написать функцию nb_year(p0, percent, aug, p), которая определяет через сколько лет
# население города будет больше или равно p
#
# Пример:
# p0 = 1000, percent = 2, aug = 50 =>
# через один год население = 1000 + 1000 / 100 * 2 + 50 = 1070


import traceback


def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = p0 + p0 / 100 * percent + aug
        year += 1
    return year


# Тесты
try:
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
