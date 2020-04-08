# Ici, on import des définitions provenant du fichier definitions.py
# Ceci permet de réutiliser dans différents scripts les mêmes définitions sans avoir à dupliquer le code partout.
from definitions import *

# Dossier par defaut des questions & quiz
dossier_questions:str = "questions"
dossier_quiz:str = "quiz"

# On crée toujours les dossiers questions et quiz. Il ne se passe rien s'ils sont déjà créés.
creerDossier(dossier_questions)
creerDossier(dossier_quiz)

# Afin d'informer l'utilisateur.
print("Les questions seront lues dans le dossier " + dossier_questions)
print("Les quiz seront générées dans le dossier " + dossier_quiz)

continuer:bool = True

# Variable contenant toutes les questions triées par id.
questions = {}

# Lecture de toutes les questions déjà créées.
lireFichiersQuestion(dossier_questions, questions)

# Si aucune question n'existe, on quite le script.
if not questions:
    print("aucune questions n'a été trouvée: veuillez utiliser le script generateur_questions.py afin de créer des questions")
    exit(0)

# Tant que l'utilisateur veut continuer:
while continuer:
    # Saisie de chaque variable définissant un quiz:
    nom = lireSaisie("Quel est le nom du quiz? " , "Le nom du quiz ne peut pas être vide, veuillez entrer le nom du quiz à nouveau: ")
    questions_choisies = []

    # Pour chaque question, on demande a l'utilisateur s'il veut l'ajoutée au présent quiz.
    for id, question in questions.items():
        ajout_question:bool = lireSaiseOuiNon("Voulez-vous ajouter la question avec l'énoncer: " + question.enonce + " au quiz? (o/n) ", "La réponse n'est pas valide. Voulez-vous ajouter la question avec l'énoncer: " + question.enonce + " au quiz? (o/n) ")

        # Si non, on passe à la question suivante.
        if not ajout_question:
            continue

        # Si oui, on ajoute la question au nouveau quiz.
        questions_choisies.append(id)

    # Une fois toutes les questions traversée, on crée le quiz
    quiz = Quiz(nom, questions_choisies)

    # Ici, on tente d'écrire la question dans un fichier pour utilisation ultérieure.
    if not ecrireFichier(dossier_quiz, quiz):
        # On informe l'utilisateur d'un échec.
        print("Échec d'écriture du fichier pour la question courante. La question est malheuresement perdue.")

    # On demande à l'utilisateur s'il veut poursuivre.
    continuer = lireSaiseOuiNon("Voulez-vous saisir un autre quiz? (o/n) ", "La réponse n'est pas valide. Voulez-vous saisir un autre quiz? (o/n) ")