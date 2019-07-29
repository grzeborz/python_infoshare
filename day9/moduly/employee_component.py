from day9.moduly.Employee import Employee
from day9.moduly.Articles import bike_types, Bike, Frame, Wheel

new_employee = Employee("Grzegporz", "Szyperek")
another_new_employee = Employee("Jan")
another_new_employee.say_hello()

front_wheel = Wheel(28,"Steel",  "Black", 100)
back_wheel = Wheel(28,"Steel",  "Black", 100)
frame = Frame(19, "red", "sport")

rowerek = Bike("blue", bike_types["MTB"], front_wheel, back_wheel, frame)
print(rowerek)

#by drukowało reprezentację tej klasy https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print

print(type(rowerek))
print(rowerek.color)
print(rowerek.back_wheel)
print(rowerek.handlebar)