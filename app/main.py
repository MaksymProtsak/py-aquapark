from abc import ABC


class IntegerRange:
    def __init__(self, min_amount, max_amount):
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner, name: str) -> None:
        self.protected_name = "_" + name

    def __get__(self, instance, owner) -> str:
        return getattr(instance, self.protected_name)

    def __set__(self, instance, value: int) -> None:
        setattr(instance, self.protected_name, value)


class Visitor:
    def __init__(self, name, age, weight, height) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(4, 14)
    height = IntegerRange(80, 120)
    weight = IntegerRange(20, 50)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(14, 60)
    height = IntegerRange(120, 220)
    weight = IntegerRange(50, 120)


class Slide:
    def __init__(self, name, limitation_class):
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self):
        return self.limitation_class
