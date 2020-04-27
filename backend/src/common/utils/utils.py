def pad(num, size):
    s = str(num) + ''
    while (len(s) < size):
        s = '0' + s
    return s


def is_status_ok(status):
    return 200 <= status < 300
