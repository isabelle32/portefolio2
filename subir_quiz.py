from definitions import *

# Dossier par defaut des questions & quiz
dossier_questions:str = "questions"
dossier_quiz:str = "quiz"

# On crée toujours les dossiers questions et quiz. Il ne se passe rien s'ils sont déjà créés.
creerDossier(dossier_questions)
creerDossier(dossier_quiz)

# Variables contenant toutes les questions et les quiz triées par id.
questions = {}
quiz = {}

# Lecture de toutes les questions & quiz déjà créés
lireFichiersQuestion(dossier_questions, questions)
lireFichiersQuiz(dossier_quiz, quiz)

continuer:bool = True

# Tant que l'utilisateur veut continuer:
while continuer:
    quiz_choisi = {}

    # Pour tous les quiz:
    for id, quiz_courant in quiz.items():
        choisi:bool = lireSaiseOuiNon("Voulez-vous subir le quiz: " + 
                                      quiz_courant.nom + "? (o/n) ", 
                                      "La réponse n'est pas valide. Voulez-vous subir le quiz: " + 
                                      quiz_courant.nom + "? (o/n) ")

        # Si le quiz est choisi: on prend note du quiz a utiliser & on sort de la boucle.
        if choisi:
            quiz_choisi = quiz_courant
            break

    # Ici, si un quiz a été choisi parmi tous les quiz, on le fait subir:
    if quiz_choisi:
        subirQuiz(questions, quiz_choisi)

    # On demander à l'utilisateur s'il veut suber un autre quiz.
    continuer = lireSaiseOuiNon("Voulez-vous subir un autre quiz? (o/n) ",
                                "La réponse n'est pas valide. Voulez-vous subir un autre quiz? (o/n) ")
