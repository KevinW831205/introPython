def open_file(filename):
    try:
        f= open(filename)
    except OSError:
        return None