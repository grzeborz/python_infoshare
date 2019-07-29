class Employee(object):
    """
    creates new Employee
    """
    def __init__(self, imie, salary, nazwisko = "Kowalski"):
        self.name = imie
        self.surname = nazwisko
        self.salary = float(salary)

    def say_hello(self):
        """
        Saying Hello
        :return:
        """
        print(f"Hello, My name is {self.name} {self.surname}")

    def increase_salary(self, percentage):
        """
        give me more money
        :return:
        """
        self.salary = (1 + percentage / 100) * self.salary

    def check_salary(self):
        print(f"Salary  equals {self.salary}")