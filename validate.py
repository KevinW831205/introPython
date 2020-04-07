def open_file(filename):
    try:
        f= open(filename)
    except OSError:
        return None

def validate_length(username, minlen):
    assert type(username) == str, "username must be string"
    if minlen <1:
        raise ValueError("minlen must be atleast 1")
    if len(username)<minlen:
        return False
    return True
