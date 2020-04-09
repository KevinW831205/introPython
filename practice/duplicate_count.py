def duplicate_count(text):
    duplicates = set()
    result = 0;
    text = text.lower()
    for letter in text:
        if text.count(letter) > 1 and not letter in duplicates:
            duplicates.add(letter);
            result +=1

    return result
