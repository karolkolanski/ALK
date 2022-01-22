class Calculator:
    def add(self, a, b):
        return a + b

    def add_extended(self, *args):
        result = 0
        for arg in args:
            result += arg
        return result

    def add_named(self, **kwargs):
        print(kwargs, type(kwargs))
        for key, value in kwargs.items():
            print("Key:", key, "Value", value)
