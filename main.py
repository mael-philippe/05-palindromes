"""
Vérifie si un string est un palindrome
"""

import unicodedata

def standardisation(mot):
    """
    Mise en forme standard du mot
    """
    mot = mot.lower()
    mot = unicodedata.normalize('NFD', mot)
    for i in mot:
        if mot.isalnum() == False:
            mot = mot.replace(i, "")
    return mot

#### Fonction secondaire
def ispalindrome(p):
    """
    Vérifie si p est un palindrome
    """
    p = standardisation(p)
    p_list = []
    # Création d'une liste qui contient les caractères de p
    for i in p:
        p_list.append(i)
    # création de la liste inversée
    reverse_p = []
    for i in range (len(p_list)):
        reverse_p.insert(0, p_list[i])
    #test palindrome
    return p_list == reverse_p

def main():
    """
    Test de la fonction ispalindrome
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie", "Élu par cette crapule"]:
        print(s, ispalindrome(s))

#appel protégé de la fonction
if __name__ == "__main__":
    main()
