import time
from compte import *
from constants import *
from exceptions import *

i_want_to_quit = 0

def accType(value):
    """
    Cette fonction permet de tester si la valeur donnée
    par l'input du type de compte est valide puis
    renvoie les constantes correspondantes à cette valeur
    """
    try:
        if value not in TEST_TYPE:
            raise BadAcc()
        else:
            if value == 1:
                return COMPTE_COURANT
            else:
                return COMPTE_EPARGNE
    except BadAcc:
        print("Entrez une donnée valide, 1 pour un Compte Courant ou 2 pour un Compte Epargne")


def opType(value):
    """
    Cette fonction permet de tester si la valeur donnée
    par l'input du type d'opération est valide puis
    renvoie les constantes correspondantes à cette valeur
    """
    try:
        if value not in TEST_OPERATION:
            raise BadOperation()
        else:
            if value == 1:
                return APP_SOLDE
            elif value == 2:
                return APP_RETRAIT
            elif value == 3:
                return APP_VERSEMENT
            else:
                return APP_QUITTER
    except BadOperation:
        print("Entrez une donnée valide : \n1 pour afficher votre solde\n2 pour effectuer un retrait\n3 pour effectuer un versement\n4 pour quitter l'application")


print("Bienvenue chez Bank'Hol")
time.sleep(1)
print("Pour l'instant, cette application ne sert qu'à simuler une création de compte bancaire et à effectuer un retrait et/ou un versement")
time.sleep(2)

# On demande le nom de l'utilisateur qui sera utilisé pour le compte

name = input("A quel nom sera votre compte bancaire ?\n")

# Puis, on passe un premier test pour définir si l'utilisateur veut créer un compte Courant ou un compte Epargne

acc_type = input("Choisissez votre type de compte : \n1 : Compte Courant\n2 : Compte Epargne\n")
while acc_type not in TEST_TYPE:
    try:
        if int(acc_type) != acc_type:
            acc_type = input("Entrez un type de compte correct : \n1 : Compte Courant\n2 : Compte Epargne\n")
    except ValueError:
        acc_type = input("Entrez un type de compte correct : \n1 : Compte Courant\n2 : Compte Epargne\n")
    else:
        acc_type = accType(acc_type)
        print(acc_type)

# Si le compte choisi est un compte courant :
# On demande à l'utilisateur s'il veut faire un premier dépôt à la création du compte

if acc_type == COMPTE_COURANT:
    first_deposit = input("Voulez vous faire un premier apport ?\n1 : Oui\n2 : Non\n")
    #print(first_deposit)
    while first_deposit not in TEST_DEPOSIT:
        try:
            if int(first_deposit) != first_deposit:
                first_deposit = input("Entrez une réponse correcte : \n1 : Oui\n2 : Non\n")
        except ValueError:
            first_deposit = input("Entrez une réponse correcte : \n1 : Oui\n2 : Non\n")
    if first_deposit == '1':
        solde = input("De quel montant sera votre premier apport ?\n")
        #print(solde)
    else:
        solde = 0
    # Puis, on instancie l'objet CompteCourant avec le nom, le type et le solde
    account = CompteCourant(name, acc_type=COMPTE_COURANT, solde=float(solde))
    #print(account.nomProprietaire,  account.solde)

# Si le compte choisi est un compte d'épargne :
# On demande aussi s'il veut faire un premier dépôt

else:
    first_deposit = input("Voulez vous faire un premier apport ?\n1 : Oui\n2 : Non\n")
    #print(first_deposit)
    while first_deposit not in TEST_DEPOSIT:
        try:
            if int(first_deposit) != first_deposit:
                first_deposit = input("Entrez une réponse correcte : \n1 : Oui\n2 : Non\n")
        except ValueError:
            first_deposit = input("Entrez une réponse correcte : \n1 : Oui\n2 : Non\n")
    if first_deposit == '1':
        solde = input("De quel montant sera votre premier apport ?\n")
        #print(solde)
    else:
        solde = 0
    # Puis, on instancie l'objet CompteEpargne avec le nom, le type et le solde
    account = CompteEpargne(name, acc_type=COMPTE_COURANT, solde=float(solde))
    #print(account)

# On arrive donc sur le compte créé :
# On demande donc à l'utilisateur ce qu'il veut faire sur ce compte

print(f"Bienvenue sur votre compte {account.nomProprietaire}")
time.sleep(2)

operation = input("Que voulez vous faire ?\n1 : Consulter votre compte\n2 : Faire un retrait\n3 : Faire un versement\n4 : Quitter l'application\n")
while i_want_to_quit != 1:
    while operation not in TEST_OPERATION:
        try:
            if int(operation) != operation:
                operation = input("Vouliez vous :\n1 : Consulter votre compte\n2 : Faire un retrait\n3 : Faire un versement\n4 : Quitter l'application\n")
        except ValueError:
            operation = input("Vouliez vous :\n1 : Consulter votre compte\n2 : Faire un retrait\n3 : Faire un versement\n4 : Quitter l'application\n")
    if operation == APP_SOLDE:
        print("Vous voulez donc consulter votre compte")
        time.sleep(1)
        print(f"Votre solde actuel est de {account.solde}")
        time.sleep(3)
        operation = input("Que voulez vous faire ?\n1 : Consulter votre compte\n2 : Faire un retrait\n3 : Faire un versement\n4 : Quitter l'application\n")
    elif operation == APP_RETRAIT:
        print("Vous voulez donc faire un retrait")
        time.sleep(1)
        montant = input("Combien voulez vous retirer ?\n")
        account.retrait(float(montant))
        time.sleep(3)
        operation = input("Que voulez vous faire ?\n1 : Consulter votre compte\n2 : Faire un retrait\n3 : Faire un versement\n4 : Quitter l'application\n")
    elif operation == APP_VERSEMENT:
        print("Vous voulez donc faire un versement")
        time.sleep(1)
        montant = input("Combien voulez vous verser ?\n")
        account.versement(float(montant))
        time.sleep(3)
        operation = input("Que voulez vous faire ?\n1 : Consulter votre compte\n2 : Faire un retrait\n3 : Faire un versement\n4 : Quitter l'application\n")
    elif operation == APP_QUITTER:
        print("Vous avez demandé de quitter l'application")
        time.sleep(1)
        print("A bientôt")
        i_want_to_quit = 1
        time.sleep(2)

exit()
