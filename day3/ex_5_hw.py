from sys import argv

program_name, first_arg, second_arg = argv

print(f"Pierwszy argument: {first_arg}, drugi argument: {second_arg}")

for i in range(0, int(second_arg)):
    print(first_arg)