
import string

from uuid import uuid4


def int2base(integer, base):
    if base > 36:
        return '0'
    if not integer:
        return '0'
    sign = 1 if integer > 0 else -1
    alphanum = string.digits + string.ascii_lowercase
    nums = alphanum[:base]
    res = ''
    integer *= sign
    while integer:
        integer, mod = divmod(integer, base)
        res += nums[mod]
    return ('' if sign == 1 else '-') + res[::-1]


def uniqid(base=36):
    return str(uuid4())
    # return int2base(int(time.time()*10000000), base)


def pad(num, size):
    s = str(num) + ''
    while (len(s) < size):
        s = '0' + s
    return s
