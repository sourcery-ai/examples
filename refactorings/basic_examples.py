def choose_transport(age, can_drive):
    if age > 18:
        if can_drive:
            return "car"
    return "bus"


def even_items(items):
    result = []
    for i, item in enumerate(items):
        if i % 2 == 0:
            result.append((item))
    return result


def triangular_number(n):
    result = 0
    for i in range(1, n + 1):
        result = result + i
    return result


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False