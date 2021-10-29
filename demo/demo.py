

# Sourcery can find all sorts of improvements that make your code more Pythonic

MAGICKS = ['Sourcery', 'Wizardry', 'Card tricks']

# Here we can use Python's built-in 'any' function to streamline the method
def contains_powerful_magic(spells):
    for spell in spells:
      if is_powerful(spell):
        return True
    return False

# We chain together improvements to get your code to the best possible
# state with the least effort

# Here we can use a list comprehension and then return the answer straight away
def find_the_best(magicks):
    powerful_magic = []
    for magic in magicks:
        if is_powerful(magic):
            powerful_magic.append(magic)
    return powerful_magic

# This there are more steps required to put the code in the best state
def find_more(magicks):
    powerful_magic = []
    for magic in magicks:
        if not is_powerful(magic):
            continue
        powerful_magic.append(magicks)
    return powerful_magic

# And here we are combining conditionals
def is_powerful(self, magic):
    if magic == 'Sourcery':
        return True
    elif magic == 'More Sourcery':
        return True
    else:
        return False

# We can even identify duplicate code and extract it!
class ClassWithExample:
    def extraction_example():
        self.sparkle_slider = Scale(
            self.master, from_=1, to=10, orient=HORIZONTAL, label='Sparkle')
        self.sparkle_slider.set(DEFAULT_SPARKLE)
        self.sparkle_slider.configure(background='black')

        self.whoosh_slider = Scale(
            self.master, from_=1, to=10, orient=HORIZONTAL, label='Whoosh')
        self.whoosh_slider.set(DEFAULT_WHOOSH)
        self.whoosh_slider.configure(background='purple')


# We can evem untangle some pretty thorny logic
class GildedRose:
    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


# And do clone detection and whole project scans!