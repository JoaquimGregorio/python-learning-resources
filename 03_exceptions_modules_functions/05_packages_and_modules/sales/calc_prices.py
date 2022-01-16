from sales.format import price


def increase_price(value: int | float, percentage: int | float, formated: bool = False):
    r = value + (value * (percentage / 100))
    if formated:
        return price.real(r)
    return r


def decrease_price(value: int | float, percentage: int | float, formated: bool = False):
    r = value - (value * (percentage / 100))
    if formated:
        return price.real(r)
    return r
