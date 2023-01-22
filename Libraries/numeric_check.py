def isfloat(num) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


def isint(num) -> bool:
    try:
        int(num)
        return True
    except ValueError:
        return False
