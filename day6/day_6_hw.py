# jako prace domową - przejrzyj zadania - examples z folderu Trainings - przykłady nie zaczynaja sie od numeru
# oraz rozwiaz zadania z folderu Trainings (pliki zaczynajace sie od numerow)

# oraz:

# 1 stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
# może być słownik miejskiego slangu ;)
# words_dict = {}
# # words_dict["kasiora"] = "pieniadze"
# # words_dict["rozkminiac"] = "Zastanawiac"
# # words_dict["obcinac"] = "Przygladac sie"
# # words_dict["kimac"] = "Spac"
# # words_dict["poginac"] = "chodzic"
# # words_dict["klimat"] = "Atmosfera"
# # words_dict["Piora "] = "włosy"
# # words_dict["szama"] = "jedzenie"
# # words_dict["styka"] = "dosyc"
# # words_dict["kiermana"] = "Kieszen"
# # words_dict["kitrac"] = "Chowac"
# # words_dict["sikor "] = "zegarek"
# # words_dict["sztama"] = "Zgoda"
# # words_dict["balet"] = "impreza"
# words_dict["elo"] = "czesc"
# words_dict["hajs"] = "pieniadze"
# words_dict["sikor"] = "zegarek"
# words_dict["kimac"] = "spac"
# print(words_dict)

# 2 zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# np kasiora - Opis slowa kasiora, w nowej linii nastepna para


# with open("miejski_slang.txt", "w+") as plik:
#     print(plik.tell())
#     for key, value in words_dict.items():
#         plik.write(f"{key} {value}\n")
#     plik.seek(0)
#     print(plik.read())


# 3 zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example

# with open("miejski_slang_CSV.csv", "w+") as plik:
#     print(plik.tell())
#     for key, value in words_dict.items():
#         plik.write(f"{key} | {value}\n")
#     plik.seek(0)
#     print(plik.read())

# 4 zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# odczytaj plik i sprawdz czy poprawnie zapisano dane

# import pickle
#
# with open("pickle_1.pickle", "wb") as plik:
#     pickle.dump(words_dict, plik)
#
# with open("pickle_1.pickle", "rb") as plik:
#     wczytywanie_dict = pickle.load(plik)
# print(f"Pickle = {wczytywanie_dict}")

# 5 odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# (powiedz uzytkownikowi ile razy wystepuje)

artykul = "article.txt"

podaj_wyraz = input("Proszę podaj słowo które znajduje się w artykule: ")

with open(artykul , "r+") as plik:
    #print(plik.readlines(), end="")
    tekst_lista = plik.readlines()
    # print(tekst_lista)
    tekst_splitted = []
    dict_words = {}
    for word in tekst_lista:
        word = ''.join(x for x in word if x not in '()",\n?.')
        slowka = word.split()
        for slowo in slowka:
            tekst_splitted.append(slowo)
        for word in tekst_splitted:
            dict_words.update(word)
            if word in dict_words:
                dict_words[word] +=1
            else:
                dict_words[word] = 1
            return dict_words
    szukana = [value for (key, value) in dict_words.items() if key == podaj_wyraz]
    print(dict_words)
    print(szukana)

# podaj_wyraz = "in"
# dict_words = {'Why': 1, 'you': 1, 'may': 2, 'ask': 1, 'in': 16, 'the': 56, 'world': 3, 'would': 2, 'someone': 2, 'type': 1, 'something': 1, 'straight': 1, 'from': 7, 'newspaper': 1, 'The': 8, 'answer': 1, 'is:': 1, 'Because': 1, 'I': 2, 'find': 3, 'this': 5, 'an': 4, 'interesting': 1, 'and': 18, 'funny': 1, 'article': 2, 'thought': 2, 'that': 10, 'some': 2, 'people': 2, "don't": 1, 'get': 1, 'Chronicle': 1, 'might': 1, 'want': 1, 'to': 22, 'read': 1, 'it': 7, 'By': 1, 'way': 3, 'was': 6, 'typed': 1, 'on': 10, '21st': 1, 'of': 38, 'April': 1, 'but': 7, 'is': 18, "yesterday's": 1, 'paper': 1, 'Note:': 1, 'Anything': 1, 'ALL': 3, 'UPPER-': 1, 'CASE': 1, 'italics': 1, "Shakespeare's": 6, 'greatest': 1, 'tragedy': 2, "wasn't": 1, 'HAMLET': 2, 'It': 3, 'not': 20, 'having': 1, 'a': 37, 'computer': 8, 'Computers': 1, 'have': 7, 'come': 1, 'long': 1, 'since': 2, 'Stone': 1, 'Age': 1, 'micro-': 1, 'chip': 1, '20': 1, 'years': 2, 'ago': 1, 'when': 3, 'they': 2, 'were': 4, 'used': 3, 'for': 4, 'such': 2, 'raw': 1, 'displays': 1, 'brute': 1, 'tech-': 1, 'nology': 1, 'as': 6, 'hurling': 1, 'men': 1, 'moon': 1, 'To-': 1, 'day': 1, 'creature': 1, 'sophisticated': 1, 'finesse': 1, 'shooting': 1, 'moons': 1, 'mind': 1, 'One': 2, 'result': 1, 'revolution': 1, 'art': 1, 'writing': 3, 'transformation': 1, 'unmatched': 1, 'perhaps': 1, 'adverbs': 1, 'first': 3, 'emerged': 1, 'pre-lingual': 1, 'ooze': 1, 'breakthrough': 1, 'consists': 1, 'masterpiece': 1, 'word-processing': 1, 'software': 1, 'known': 2, 'modestly': 1, 'style-checker': 3, 'Like': 1, "jeweler's": 1, 'lens': 1, 'can': 6, 'reveal': 1, 'seem-': 1, 'ingly': 1, 'perfect': 2, 'gem': 1, 'be': 12, 'rough-hewn': 1, 'landscape': 1, 'blemishes': 1, 'You': 1, 'put': 2, 'prose': 1, 'spits': 1, 'out': 5, 'mistakes': 1, 'But': 4, 'its': 1, 'crowning': 1, 'achievement': 1, 'next': 1, 'step:': 1, 'composes': 1, 'improvements': 1, 'This': 3, 'brave': 1, 'new': 1, 'however': 1, 'has': 4, 'been': 2, 'tempest-': 1, 'free': 1, 'While': 1, 'style': 1, 'checkers': 1, 'are': 3, 'winning': 1, 'friends': 1, 'campuses': 1, 'offices': 1, 'met': 1, 'stubborn': 1, 'resistance': 1, 'battlements': 1, 'literature': 4, 'Indig-': 1, 'nation': 1, 'still': 1, 'simmers': 1, 'over': 1, 'what': 3, 'Bell': 1, 'Laboratories': 1, 'did': 2, 'Gettysburg': 1, 'Address': 1, 'couple': 1, 'back': 3, "Lincoln's": 1, 'sentence:': 2, 'FOUR-': 1, 'SCORE': 1, 'AND': 7, 'SEVEN': 1, 'YEARS': 2, 'AGO': 2, 'OUR': 3, 'FORE-': 1, 'FATHERS': 1, 'BROUGHT': 1, 'FORTH': 1, 'UPON': 1, 'THIS': 1, 'CONT-': 1, 'INENT': 1, 'A': 7, 'NEW': 1, 'NATION': 2, 'CONCEIVED': 1, 'IN': 3, 'LIBERTY': 1, 'DEDICATED': 1, 'TO': 11, 'THE': 11, 'PROPOSIT-': 1, 'ION': 1, 'THAT': 5, 'MEN': 1, 'ARE': 2, 'CREATED': 2, 'EQUAL': 1, '-': 12, 'improved': 2, 'read:': 1, 'EIGHTY-SEVEN': 1, 'GRANDFATHERS': 1, 'FREE': 1, 'HERE': 1, 'With': 1, 'Lincoln': 1, 'how-': 1, 'ever': 1, 'style-checkers': 1, 'just': 1, 'flexing': 1, 'their': 1, 'cursors': 1, 'They': 1, 'pre-': 1, 'paring': 1, 'eventual': 1, 'assault': 1, 'Mt': 1, 'Everest': 1, 'Shakespeare': 8, 'That': 1, 'sublime': 1, 'peak': 1, 'claimed': 1, 'recently': 1, 'Berkeley': 1, 'scientist': 1, 'revealed': 1, 'he': 4, 'had': 1, 'successfully': 1, 'trained': 1, 'his': 4, 'sniff': 1, 'flaws': 1, 'Dr': 1, 'C': 1, 'J': 1, 'Wallia': 1, 'Stanford': 1, 'PhD': 1, 'consultant': 1, 'electronic': 1, 'publications': 1, 'turned': 1, 'customized': 1, 'loose': 1, "Hamlet's": 4, 'To': 3, 'or': 5, 'soliloquy': 2, 'Their': 1, 'coughed': 1, 'up': 1, '34': 1, 'errors': 1, 'found': 1, 'language': 1, 'obsolete': 1, 'overwritten': 1, 'gave': 1, '15': 2, 'word': 1, 'alternative:': 1, 'IS': 3, 'IT': 3, 'BETTER': 1, 'LIVE': 1, 'WITH': 1, 'BAD': 1, 'LUCK': 1, 'OR': 3, 'END': 3, 'HAVE': 2, 'NIGHTMARES': 1, 'There': 1, 'we': 5, 'high-': 1, 'water': 1, 'mark': 1, 'young': 1, 'artist': 1, 'lovers': 1, 'grateful': 1, 'think': 1, "it's": 2, 'hideous': 1, 'said': 1, 'Jerry': 1, 'Turner': 1, 'artistic': 1, 'director': 1, 'Oregon': 1, 'Shakespearean': 2, 'Festival': 1, '50-': 1, 'year-old': 1, 'company': 1, 'performed': 1, 'more': 2, 'than': 1, 'any': 1, 'theater': 1, 'America': 1, "It's": 2, 'absurd': 1, 'added': 1, 'work': 1, 'standard': 2, 'best': 1, 'there': 2, 'Any': 1, 'attempt': 1, 'say': 1, 'im-': 1, 'proved': 1, 'presumptuous': 1, "Turner's": 1, 'alone': 1, 'chorus': 1, 'ridicule': 1, 'greeted': 1, "Wallia's": 3, 'effort': 1, 'let': 1, 'us': 4, 'too': 1, 'hasty': 1, 'join': 1, 'herd': 1, "There's": 1, 'little': 1, 'profit': 1, 'literary': 3, 'lemminghood': 1, 'If': 2, 'truth': 1, 'told': 1, 'glare': 1, 'fame': 1, 'often': 1, 'blinds': 1, 'actual': 1, 'merit': 1, 'When': 1, 'says': 1, 'Shake-': 3, 'speare': 3, 'genuflect': 1, 'habit': 1, 'praise': 1, 'bury': 1, 'him': 2, 'question': 2, 'issue': 1, 'no': 3, 'matter': 1, 'how': 1, 'great': 1, 'by': 1, 'so': 1, 'suffered': 1, 'immeasurable': 1, 'Millions': 1, 'readers': 1, 'died': 1, 'knowing': 1, 'only': 1, 'who': 2, 'fulfill': 1, 'all': 1, 'potential': 1, 'stunted': 1, 'Our': 1, 'highest': 1, 'poor': 1, 'shadow': 1, 'could': 2, 'In': 1, 'short': 1, 'crown': 1, 'jewels': 1, 'riding': 1, 'experiment': 1, 'Let': 3, 'then': 2, 'remove': 1, 'chastity': 1, 'belts': 1, 'our': 4, 'minds': 1, 'consider': 1, 'possibility': 1, 'help-': 1, 'ful': 1, 'recall': 1, 'other': 2, 'Elisabethan': 1, 'giant': 1, 'Ben': 1, 'Jonson': 2, 'one': 2, 'ardent': 1, 'fawning': 1, 'admirers': 1, 'wrote:': 1, 'PLAYERS': 1, 'OFTEN': 1, 'MENTIONED': 1, 'AS': 1, 'AN': 1, 'HONOR': 1, 'SHAKESPEARE': 1, 'HIS': 1, 'WRITING': 1, 'HE': 2, 'NEVER': 1, 'BLOTTED': 2, 'OUT': 1, 'LINE': 1, 'MY': 1, 'ANSWER': 1, 'HATH': 1, 'BEEN': 1, 'WOULD': 1, 'HAD': 1, 'THOUSAND': 2, 'Such': 1, 'view': 1, 'course': 1, 'merely': 1, 'generaliztion': 1, 'real': 1, 'test': 1, 'must': 1, 'examine': 1, 'text': 1, 'itself': 1, 'means': 1, 'casting': 1, 'uncowed': 1, 'eye': 1, 'Hamlet': 4, 'speech': 1, 'composed': 1, 'without': 2, 'computer:': 1, 'BE': 2, 'NOT': 1, 'QUESTION': 1, 'Already': 1, 'problem': 1, "let's": 1, 'quibble': 1, 'clearly': 1, 'torn': 1, 'between': 1, 'living': 1, 'dying': 1, 'at': 3, 'least': 1, 'appears': 1, 'until': 1, 'second': 1, 'WHETHER': 1, "'TIS": 1, 'NOBLER': 1, 'MIND': 1, 'SUFFER': 1, 'SLINGS': 1, 'ARROWS': 1, 'OF': 3, 'OUTRAGEOUS': 1, 'FORTUNE': 1, 'TAKE': 1, 'ARMS': 1, 'AGAINST': 1, 'SEA': 1, 'TROUBLES': 1, 'BY': 2, 'OPPOSING': 1, 'THEM': 1, 'ignore': 1, 'metaphoric': 1, 'indigestion': 1, 'taking': 1, 'arms': 1, 'against': 1, 'sea': 2, 'Here': 2, 'choice': 1, 'divides': 1, 'life': 1, 'death': 2, 'passive': 1, 'suffering': 1, 'vs': 1, 'active': 1, 'opposition': 1, 'We': 2, 'naturally': 1, 'go': 1, 'third': 1, 'sentence': 5, 'talking': 1, 'about': 1, 'run': 1, 'into': 1, 'this:': 1, 'DIE': 1, 'SLEEP': 2, 'NO': 1, 'MORE': 1, 'SAY': 1, 'WE': 1, 'HEARTACHE': 1, 'NATURAL': 1, 'SHOCKS': 1, 'FLESH': 1, 'HEIR': 1, 'Now': 1, "he's": 1, 'trip': 1, 'No': 1, 'wonder': 1, 'conf-': 1, 'On': 1, 'top': 1, 'fragment': 1, 'proper': 1, 'subject': 1, 'verb': 1, 'thus': 1, 'complete': 1, 'Moreover': 1, 'try': 1, 'saying': 1, 'loud': 1, 'hardly': 1, 'rolls': 1, 'trippingly': 1, 'tongue': 1, 'From': 1, 'downhill': 1, 'gallop': 1, 'hit': 1, 'BODKIN': 1, 'FARDELS': 1, 'phrases': 1, 'like': 1, 'SPURNS': 1, 'PATIENT': 1, 'MERIT': 1, 'UNWORTHY': 1, 'TAKES': 1, 'stuff': 1, 'head-': 1, 'aches': 1, 'made': 1, 'rummage': 1, 'through': 1, 'play': 2, 'numerous': 1, 'ex-': 1, 'amples': 1, 'country': 1, 'whose': 1, 'bourne': 1, 'comprehension': 1, 'returns': 1, 'typical': 1, 'remark': 1, 'later': 1, 'Act': 1, 'III:': 1, 'LET': 1, 'GALLED': 1, 'JADE': 1, 'WINCE': 1, 'WITHERS': 1, 'UNWRUNG': 1, 'meaning': 1, 'leap': 1, 'glance': 1, 'Luckily': 1, 'footnote': 1, 'Professor': 1, 'G': 1, 'B': 1, "Harrison's": 1, 'widely': 1, 'tome': 1, 'Shakespeare:': 1, 'Complete': 1, 'Works': 1, 'trans-': 1, 'lates:': 1, 'nag': 1, 'with': 1, 'sore': 1, 'flinch': 1, 'saddle': 1, 'on;': 1, 'shoulders': 1, 'feel': 1, 'pain': 1, 'example': 2, 'makes': 1, 'thing': 1, 'clear:': 1, 'society': 1, 'owes': 1, 'large': 1, 'debt': 1, 'scholars': 1, 'kept': 1, 'old': 1, 'Bard': 1, 'afloat': 1, 'footnotes': 1, 'Think': 1, "Galileo's": 1, 'telescope': 1, 'First': 1, 'comes': 1, 'shock': 1, 'heresy': 1, 'Then': 1, 'accept-': 1, 'ance': 1, 'being': 1, 'center': 1, 'universeFinally': 1, 'enjoy': 1, "discovery's": 1, 'benefits': 1, 'For': 1, 'if': 1, '265-word': 1, 'trimmed': 1, 'words': 1, 'same': 1, 'rate': 1, 'improvement': 1, 'reduce': 1, 'entire': 1, '4': 1, 'hour': 1, '1980s': 1, 'size': 1, 'bite': 1, 'culture': 1, '14': 1, 'minutes': 1, 'Add': 1, 'drums': 1, 'electric': 1, 'strings': 1, 'imagine': 1, 'born': 1, 'anew': 1, "today's": 1, 'world:': 1, 'ROCK': 1, 'VIDEO': 1, 'Call': 1, 'casualty': 1, 'progress': 1, 'moldy': 1, 'scribbler': 1, 'emperor': 1, 'unclothed': 1, 'do': 1, 'call': 1, 'account': 1, "He's": 1, 'blame': 1, 'How': 1, 'vocabulary': 1, 'attention': 1, 'spans': 1, 'become': 1, 'much': 1, 'slimmer': 1, 'thanks': 2, 'quick-thrill': 1, 'diet': 1, 'modern': 1, 'enter-': 1, 'tainment': 1, 'fault': 1, 'dear': 1, 'William': 1, 'ourselves': 1, 'stars': 1, 'Joan': 1, 'Collins': 1, 'Mr': 1, 'T': 1, 'Boy': 1, 'George': 1}
#
#
#
# print(szukana)

# if podaj_wyraz in dict_words:
#     dict_words.[podaj_wyraz] = dict_words.get()
#     print()


# 6 utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# na poczatku programu zaladuj slownik z pliku pickle
# (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany


