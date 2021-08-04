DEFAULT_SPEED = 10
DEFAULT_FORCE = 20
HORIZONTAL = 1
VERTICAL = 2


class Sliders:
    def __init__(self, steps):
        self._steps = steps

    def create_speed_slider(self):
        speed_slider = Slider(
            self._steps, from_=1, to=10, orient=HORIZONTAL, label="Speed"
        )
        speed_slider.pack()
        speed_slider.set(DEFAULT_SPEED)
        speed_slider.configure(background="red")
        return speed_slider

    def create_force_slider(self):
        force_slider = Slider(
            self._steps, from_=1, to=10, orient=HORIZONTAL, label="Force"
        )
        force_slider.pack()
        force_slider.set(DEFAULT_FORCE)
        force_slider.configure(background="green")
        return force_slider


def create_sliders():
    speed_slider = Slider(5, from_=1, to=10, orient=HORIZONTAL, label="Speed")
    speed_slider.pack()
    speed_slider.set(DEFAULT_SPEED)
    speed_slider.configure(background="red")

    force_slider = Slider(5, from_=1, to=10, orient=HORIZONTAL, label="Force")
    force_slider.pack()
    force_slider.set(DEFAULT_FORCE)

    force_slider.configure(background="green")
    return speed_slider, force_slider


class Slider:
    def __init__(self, steps, from_, to, orient, label):
        ...

    def pack(self):
        ...

    def set(self, position):
        ...

    def configure(self, background):
        ...
