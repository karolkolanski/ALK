class Calculator:
    def add(self, a, b):
        return a + b
    def add_extended(self, *args):
        result = 0
        for arg in args:
            result += arg
        return result
