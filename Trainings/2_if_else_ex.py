# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

def czy_trojkat_jest_mozliwy_do_narysowania(a, b, c):
    '''

    :param first_side:
    :param second_side:
    :param third_side:
    :return:
    '''
    if a < b + c or  b < a + c or c < a + b:
        print(f"Trójką jest możliwy do wykonania")
    else:
        print(f"I did du nuffin\n"
              f"każdy tak mówi, trójkąt nie wyjdzie")


    if a == b == c:
        print(f"Trójkąt jest równoboczny")
    elif a == b or a == c or b == c:
        print(f"Trójkąt jest równoramienny")
    else:
        print(f"Trójkąt jest różnoboczny")
        # print(f"I did du nuffin\n"
        #       f"każdy tak mówi, trójkąt nie wyjdzie")



print(czy_trojkat_jest_mozliwy_do_narysowania(bok_a,bok_b,bok_c))