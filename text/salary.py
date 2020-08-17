base = 306800
zangyo = 30
house = 67500
social = 15000 + 45000
residential = 310000 / 12
income = 18000
tax = residential + income


def zangyo_dai():
    return (base + 8000) * (1 / 160 * 1.3 * zangyo)


def monthly():
    return base + 8000 + house + zangyo_dai()


def bonus():
    return base * 6.3


def total():
    return monthly() * 12 + bonus()


def first_year():
    return monthly() * 12 + bonus() / 12 * 7


def tedori_month():
    return monthly() - social - tax


def total_tedori():
    return total() * 0.8


if __name__ == '__main__':
    print(total())
