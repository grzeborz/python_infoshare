import os

reader = open('prog.py', 'w')
filename = __name__
filepath = __file__
full_path = os.getcwd()
try:
    reader.write(f'{filename}\n {filepath}\n {full_path}')
finally:
    reader.close()

imie_słuchacza = input('Podaj imie: ')

with open('prog.py', 'a') as a_reader:
    a_reader.write(f'\n {imie_słuchacza}')
    # print(__file__)
    # print(__name__)


# with open('prog.py', 'w') as writer:
#     writer.write('Yolyol')
