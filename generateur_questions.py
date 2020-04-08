# Ici, on import des définitions provenant du fichier definitions.py
# Ceci permet de réutiliser dans différents scripts les mêmes définitions sans avoir à dupliquer le code partout.
from definitions import *

# Nom par defaut du dossier questions.
dossier_questions:str = "questions"

# On crée toujours le dossier questions. Il ne se passe rien s'il est déjà créé.
creerDossier(dossier_questions)

# Afin d'informer l'utilisateur.
print("Les questions seront générées dans le dossier " + dossier_questions)

continuer:bool = True

# Tant que l'utilisateur veut continuer:
while continuer:
    # Saisie de chaque variable définissant une question:
    enonce:str = lireSaisie("veuillez entrer l'énoncer de la question: ", "L'énoncer de la question ne peut pas être vide. Veuillez entrer l'énoner de la question à nouveau: ")
    choix_a:str = lireSaisie("Veuillez entrer le premier choix de réponse: ", "Le choix de réponse ne peut pas être vide. Veuillez entrer le premier choix de réponse à nouveau: ")
    ponderation_a:int = lireSaisieEntier("Quelle est la pondération du premier choix de réponse: ", "La pondération du choix de réponse doit être un entier. Veuillez entrer la pondération du premier choix de réponse à nouveau: ")

    choix_b:str = lireSaisie("Veuillez entrer le deuxième choix de réponse: ",
                             "Le choix de réponse ne peut pas être vide. Veuillez entrer le deuxième choix de réponse à nouveau: ")
    ponderation_b:int = lireSaisieEntier("Quelle est la pondération du deuxième choix de réponse: ",
                                    "La pondération du choix de réponse doit être un entier. Veuillez entrer la pondération du deuxième choix de réponse à nouveau: ")

    choix_c:str = lireSaisie("Veuillez entrer le troisième choix de réponse: ",
                             "Le choix de réponse ne peut pas être vide. Veuillez entrer le troisième choix de réponse à nouveau: ")
    ponderation_c:int = lireSaisieEntier("Quelle est la pondération du troisième choix de réponse: ",
                                    "La pondération du choix de réponse doit être un entier. Veuillez entrer la pondération du troisième choix de réponse à nouveau: ")

    choix_d:str = lireSaisie("Veuillez entrer le quatrième choix de réponse: ",
                             "Le choix de réponse ne peut pas être vide. Veuillez entrer le quatrième choix de réponse à nouveau: ")
    ponderation_d:int = lireSaisieEntier("Quelle est la pondération du quatrième choix de réponse: ",
                                    "La pondération du choix de réponse doit être un entier. Veuillez entrer la pondération du quatrième choix de réponse à nouveau: ")

    # Création des différents objets définissant une Question.
    choix = DescriptionChoix(choix_a, choix_b, choix_c, choix_d)
    ponderation = PonderationChoix(ponderation_a, ponderation_b, ponderation_c, ponderation_d)
    question = Question(enonce, choix, ponderation)

    # Ici, on tente d'écrire la question dans un fichier pour utilisation ultérieure.
    if not ecrireFichier(dossier_questions, question):
        # On informe l'utilisateur d'un échec.
        print("Échec d'écriture du fichier pour la question courante. La question est malheuresement perdue.")

    # On demande à l'utilisateur s'il veut poursuivre.
    continuer = lireSaiseOuiNon("Voulez-vous saisir une autre question? (o/n) ", "La réponse n'est pas valide. Voulez-vous saisir une autre question? (o/n) ")
