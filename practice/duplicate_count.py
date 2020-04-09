def duplicate_count(text):
    duplicates = set()
    result = 0;
    for letter in text:
        if letter in duplicates:
            result += 1;
        else:
            duplicates.add(letter)
    return result
