
class FirstClass:
    # KONSTRUKTOR
    def __init__(self, value):
        self._data = value
    def set_data(self, value):
        self._data = value
    def display(self):
        print(self._data)

x = FirstClass("Król Artur")
y = FirstClass("Anna karenina")

print(dir(x))

#x.set_data("kamil")
x.display()
