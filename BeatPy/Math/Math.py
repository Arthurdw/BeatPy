def average(amounts):
    try:
        total = len(amounts)
    except TypeError:
        raise TypeError("`average()` function received 1 parameter. Expected at least 2 parameters.")
    added = 0
    for amount in amounts:
        try:
            added += amount
        except TypeError:
            raise TypeError("`average()` function received invalid parameter type. Expected a set of integers!")
    return added/total
