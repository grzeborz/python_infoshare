# file = open()
# try:
#     #yołoył
# finally:
#     reader.close()

with open('prog.py', 'w') as reader:
    print(__file__)
    print(__name__)


with open('prog.py', 'w') as writer:
    writer.write('Yolyol')
