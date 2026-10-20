def total(quantity):
    if type(quantity) is not int or not 1 <= quantity < 100:
        raise ValueError('quantity must be an integer from 1 through 100')
    return quantity * 10
