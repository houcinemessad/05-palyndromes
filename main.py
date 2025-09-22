#### Fonction secondaire
def ispalindrome(p):
    for i in range(len(p)):
        if p[i] != p[len(p) - 1 - i]:
            return False
    return True

#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
