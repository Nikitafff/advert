import json


class AttributeParser:
    def __init__(self, item):
        for key, value in item.items():
            if isinstance(value, dict):
                value = AttributeParser(value)
            self.__dict__[key] = value


class Advert(AttributeParser):
    def __init__(self, base):
        [self.__setattr__(key, value) for key, value in base.items()]
        if getattr(self, "price", 0) < 0:
            raise ValueError(f"Price = {self.price} ! Price must be >= 0")

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:
    @property
    def color(self):
        return 32

    def __str__(self):
        return f'\033[1;{self.color};40m{self.__repr__()}'


class Advert(ColorizeMixin, Advert):
    color = 33
    pass


if __name__ == "__main__":
    test = """{
      "title": "iPhone X",
      "price": 100,
      "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
      }
    }"""

    test = json.loads(test)
    iphone = Advert(test)
    print(iphone)



