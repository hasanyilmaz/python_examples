# hesap makinesini fonksiyon ile yaz


def plus(*parameters):
    equals = 0
    for i in parameters:
        equals += i
    print(equals)


def minus(*parameters):
    equals = parameters[0] - parameters[1]
    print(equals)


def multiply(*parameters):
    equals = parameters[0] * parameters[1]
    print(equals)


def divide(*parameters):
    equals = parameters[0] / parameters[1]
    print(equals)


# Examples
plus(113, 255)
minus(11, 3)
multiply(33, 2)
divide(77, 23)
