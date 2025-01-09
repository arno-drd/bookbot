def main ():
    book_path="books/frankenstein.txt"
    #j'initialise chaque variable séparément en appelant chaque fonctions, pour les print séparément 
    text = get_text(book_path)
    lc = letter_count(text)
    wc = word_count(text)
    char_dict = how_many_of_char(text)
    result = sorted_list_of_char(text)

    print(f"---Begin report of {book_path} --- ")
    print(f"{wc} words found in the document \n")
    for character in result:
        print(f"The {character['char']} charcater was found {character['count']} times")
    print("---End report---")

def get_text(path):
    with open(path) as f:
        file_contents = f.read() #pouvait également directement return f.read 
    return file_contents


def word_count(text):
    wc = 0
    text = text.split()
    for t in text:
        wc+=1
    return wc

#méthode beaucoup plus efficace: retourner directement la lenght du string: 
#pas de variable à initialiser, pas de boucle, solution directe en 2 lignes, un exemple avec une fonction qui compte les lettres plutôt que les mots:

def letter_count(text):
    return len(text)

def how_many_of_char(text):
    text = text.lower()         #on convertit toutes les lettres en des lettres minuscules pour le calcul
    result = {}
    for c in text:
        if c not in result:
            result[c] = 1
        else : result[c] +=1
    return result

def order_dict(d):      #permet de déterminer l'ordre du dictionnaire
    return d['count']

def dict_to_dictlist (d):   #transforme notre dictionnaire en une liste de dictionnaire
    char_list = []
    for char, count in d.items() :
        if char.isalpha() :         #on ne souhaite compter que les lettres
            char_list.append({'char' : char, 'count' : count})

    return char_list


def sorted_list_of_char (text):
    mydict = how_many_of_char(text)
    mylist = dict_to_dictlist(mydict)
    mylist.sort(reverse=True, key=order_dict)
    return mylist


main()