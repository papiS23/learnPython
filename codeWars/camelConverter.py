def to_camel_case(text):
    str = text.replace('-', ' ')
    str = str.replace('_', ' ')
    word_list = str.split()
    result = ''
    if text == '':
        result = text
    else:
        words = word_list.copy()
        words.remove(word_list[0])
        result = word_list[0]
        for word in words:
            result = result + word[0].upper() + word[1:]
    return result



# def to_camel_case(text):
#     str = text
#     result = ''
#     for i in range(len(str)):
#         if str[i] == '-':
#             str.replace('-', '')
#             str[i+1].upper()
#         elif str[i] == '_':
#             str.replace('_', '')
#             str[i + 1].upper()
#     return str



print(to_camel_case('the_stealth-warrior'))