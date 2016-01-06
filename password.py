# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('bc')
    'bd'
    >>> len(getNext('bc'))
    2
    >>> len(getNext('az'))
    2
    """
    nbrZ = 0
    for lettre in password:
        if lettre == 'z':
            nbrZ = nbrZ + 1
    pwd = list(password)  #1 Creation d'une liste nommée pwd, dont le premier element sera le string 'password'
    found = False
    i=len(pwd)-1
    if(i + 1) == nbrZ:
        raise ValueError('Valeur du mot de passe incorrect')
        
    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2 Retourne le caractère ASCII de la lettre selectionnée, puis ajoute 1 et le reconvertit en caractère
           found = True             
        else:
           i = i-1
           pwd[i+1] = "a"
           if(i == -1):
               found = True
    
    return ''.join(pwd) #3 Colle tous les caractères de la liste ensemble, le séparateur est un caractère vide donc il n'y aura aucun caractère entre chaque lettre
def hasSeries(password):
    i = 0
    lettreTest = ''
    for lettre in password:
       if i == 0:
           lettreTest = lettre
       elif i == 3:
           return False
           
       if(lettreTest == lettre):
           i = i + 1
       else:
            i = 0
    return True

def hasNoBadChar(password):
    if 'o' in password or 'i' in password or 'l' in password:
        return False
    else:
        return True

def hasTwoPairs(password):
    


# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    r = hasNoBadChar('fdgdffi')
    print(r)
