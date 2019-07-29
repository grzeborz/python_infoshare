class Employee(object):
    """
    creates new Employee
    """
    def __init__(self, imie, nazwisko = "Kowalski"):
        self.name = imie
        self.surname = nazwisko

    def say_hello(self):
        """
        Saying Hello
        :return:
        """
        print(f"Hello, My name is {self.name} {self.surname}")