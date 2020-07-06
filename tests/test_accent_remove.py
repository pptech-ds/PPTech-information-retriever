import unidecode

list_words_accent = ['Málaga', 'crêpe', 'caleçon', 'abbé', 'café', 'été', 'éléphant', 'gâteau', 'pâte', 'bâtiment', 'être', 'tête', 'île', 'apôtre', 'croûte', 
'août', 'là', 'procès', 'fièvre', 'où', 'façade', 'français', 'garçon', 'bœuf', 'œil', 'Noël', 'haïr', 'maïs', 'Saül', 'L\'Haÿ-Les-Roses']

list_words_woaccent = ['Malaga', 'crepe', 'calecon', 'abbe', 'cafe', 'ete', 'elephant', 'gateau', 'pate', 'batiment', 'etre', 'tete', 'ile', 'apotre', 'croute', 
'aout', 'la', 'proces', 'fievre', 'ou', 'facade', 'francais', 'garcon', 'boeuf', 'oeil', 'Noel', 'hair', 'mais', 'Saul', 'L\'Hay-Les-Roses']


def ensureUtf(s):
    """S'assure que le paramètre passé est bien encodé en utf-8."""
    try:
        if type(s) == unicode:
            return s.encode('utf8', 'ignore')
    except: 
        return str(s)


def check_accent(list_words_accent, list_words_woaccent):

    for i in range(len(list_words_accent)):
        #accented_string = u'Málaga'
        accented_string = ensureUtf(list_words_accent[i])
        # accented_string is of type 'unicode'

        unaccented_string = unidecode.unidecode(accented_string)
        # unaccented_string contains 'Malaga'and is of type 'str'
        #print('initial string: {} / removed accent string {}'.format(accented_string, unaccented_string))

        if(unaccented_string != list_words_woaccent[i]):
            print('initial word is {}, unaccented word {} not corresponds to expected word {}'.format(list_words_accent[i], accented_string, list_words_woaccent[i]))
            exit()
        
    print('check of remove accent correctly done!')

    return 0


check_accent(list_words_accent, list_words_woaccent)    