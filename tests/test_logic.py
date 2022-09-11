from man_and_glass.logic import Man, Glass, DrinkLiquid


def test_man_class():
    try:
        m = Man(3000)
        assert False
    except TypeError:
        assert True

    try:
        m = Man('man')
        assert False
    except TypeError:
        assert True

    m = Man(900)
    assert m.MAX_VOLUME == 1000


def test_glass_class():
    try:
        g = Glass('glass')  # noqa F841
        assert False
    except TypeError:
        assert True


def test_drink_liquid():
    m = Man(800)
    g = Glass(200)
    drink = DrinkLiquid(m, g)
    assert drink.drink(150) == (650, 50)
