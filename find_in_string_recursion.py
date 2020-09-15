def find_position(string, char_to_find):
    len_of_string = len(string)
    if not string:
        return -1
    elif string[-1] == char_to_find:
        return len_of_string
    else:
        return find_position(string[:len_of_string-1], char_to_find)


print(find_position('akhil', 'h'))
