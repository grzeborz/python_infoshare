reader = open('prog.py', 'w')
filename = __name__
filepath = __file__
try:
    reader.write(f'{filename}\n {filepath}')
finally:
    reader.close()

# with open('prog.py', 'w') as reader:
#     print(__file__)
#     print(__name__)
#
#
# with open('prog.py', 'w') as writer:
#     writer.write('Yolyol')
