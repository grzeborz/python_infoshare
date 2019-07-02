from sys import argv

program_name, first_arg, second_arg, third_arg = argv

print(f"Pierwszy argument: {first_arg}, drugi argument: {second_arg}, trzeci argument: {third_arg}")
print(f"A suma tych liczb to {int(first_arg) + int(second_arg) + int(third_arg)}")