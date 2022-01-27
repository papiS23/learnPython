def generate_hashtag(s):
    words = s.split()
    result = '#'
    for word in words:
        result += word.capitalize()
    if len(result) == 1 or len(result) > 140:
        return False
    return result

print(generate_hashtag(''))