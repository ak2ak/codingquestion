def equal_string(str1, str2):
    if len(str1) != len(str2):
        return False
    elif str1 == '':
        return True
    elif str1[0] != str2[0]:
        return False
    return equal_string(str1[1:], str2[1:])


print(equal_string('ass', 'as'))
