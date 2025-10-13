import math


def area(r):
    '''
    Принимает число r - радиус круга, возвращает  произведение числа пи на квадрат r - площадь круга
    '''
    if r < 0:
        raise ValueError()
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r - радиус круга, возвращает произведение числа пи на 2 и на r - периметр круга
    '''
    if r < 0:
        raise ValueError()
    return 2 * math.pi * r

