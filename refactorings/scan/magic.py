def find_good_magic():
    magics = ["Sourcery", "Mordor", "Voldemort"]

    good_magic = []
    for magic in magics:
        if magic == "Sourcery":
            good_magic.append(magic)

    print(good_magic)


def sing_happy_birthday(name):
    i = 0
    while i < 4:
        if i == 0:
            print("Happy birthday to you")
        elif i == 1:
            print("Happy birthday to you")
        elif i == 2:
            print("Happy birthday dear " + name)
        else:
            print("Happy birthday to you")
        i += 1
