# Написать функцию look_and_say(data, len), которая возвращает список
# из len следующих элементов за data в последовательности смотрю_и_говорю
# Пример последовательности для "1" ==> "11" ("один 1") ==> "21" ("два 1") ==>
# "1211" ("один 2, один 1") ==> "111221" ("один 1, один 2, два 1") ...
#
# Пример:
# look_and_say(1, 7) ==> [11, 21, 1211, 111221, 312211, 13112221, 1113213211]


import traceback


def look_and_say(data, l):
    arr = []
    for i in range(0, l):
        temp = ""
        string = str(data)
        letter = string[0]
        num = 1
        if len(string) > 1:
            for z in range(1, len(string)):
                if string[z] == letter:
                    num += 1
                else:
                    temp += str(num) + letter
                    letter = string[z]
                    num = 1
        else:
            temp = str(num) + letter
        if len(string) > 1:
            temp += str(num) + letter
        data = temp
        arr.append(int(data))
    return arr


# Тесты
try:
    assert look_and_say(1, 6) == [11, 21, 1211, 111221, 312211, 13112221]
    assert look_and_say(132, 4) == [111312, 31131112, 1321133112, 11131221232112]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
