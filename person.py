class Person:
    def __init__(self, name, surname, job=None, pay=0):
        self.name = name
        self.surname = surname
        self.job = job
        self.pay = pay

adam_nowak=Person("Adam", "Nowak")
jan_kowalski=Person("Jan", "Kowalski", "Mechanik", 5000)

