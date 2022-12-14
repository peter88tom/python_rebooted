"""
Decorator is a function that takes another function as an argument and extends it's
behaviour without changing the original function explicitly

In this example we will write a function to calculate the net price from price and tax

Suppose we need to return that net price as $10. Here we can write a decorate that will take
that returned value from the function that does the calculation and put the Tsh on it.

"""


def currency_formatter(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'Tsh {result}'

    return wrapper

@currency_formatter
def net_price(price:int, tax:int):
    """ Calculate the net price from price and tax

    :param price: the selling price
    :param tax: value added tax or sale tax
    :return: the net price
    """

    return price * (1 + tax)

print(net_price(11.55,4))
