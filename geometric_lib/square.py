
def area(a):
    '''
    Принимает число a - сторону квадрата, возвращает квадрат числа a - площадь квадрата
    '''
    if a < 0:
        raise ValueError()
    return a * a


def perimeter(a):
    '''
    Принимает число a-сторону квадрата, возвращает произведение a на 4 - периметр квадрата
    '''
    if a < 0:
        raise ValueError()
    return 4 * a
