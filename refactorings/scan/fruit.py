from dataclasses import dataclass

TASTY_APPLES = ["Gala", "Seneca Crisp", "Braeburn"]


@dataclass
class Fruit:
    size: float
    ripeness: float


@dataclass
class Apple(Fruit):
    variety: str


@dataclass
class Orange(Fruit):
    variety: str


def assess_fruit(fruit_bowl):
    happiness = 0.0
    for fruit in fruit_bowl:
        if (fruit, Apple):
            yumminess = fruit.size * fruit.ripeness ** 2
            if fruit.variety in TASTY_APPLES:
                happiness += fruit.size * yumminess
    return happiness


class DelMonteMan:
    def eat_orange(self, orange):
        if not orange.variety == "Clementine":
            with self.hands() as hands:
                self.happiness = self.happiness + 1
                segments = hands.peel(orange)
                self.eat(segments)
        else:
            with self.hands() as hands:
                if orange == "Clementine":
                    self.happiness = self.happiness + 2
                    segments = hands.peel(orange)
                    self.eat(segments)
