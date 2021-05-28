# Написать функцию is_isogram, определяющую является ли заданное слово
# изограмом, т.е. словом, в котором ни одна буква не повторяется больше
# одного раза, в независимости от регистра
#
# Примеры:
# is_isogram("documentary" ) ==> true
# is_isogram("abA" ) ==> false



import traceback


def is_isogram(s):
    temp = ""
    s = s.lower()
    for i in range(0, len(s)):
        for z in range(0, len(temp)):
            if s[i] == temp[z]:
                return False
        temp += s[i]
    return True


# Тесты
try:
    assert is_isogram("Dermatoglyphics") == True
    assert is_isogram("isogram") == True
    assert is_isogram("granulocytes") == True
    assert is_isogram("moOse") == False
    assert is_isogram("isIsogram") == False
    assert is_isogram("") == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
