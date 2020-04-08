# requis pour la génération des hash md5.
import hashlib
# requis pour la création des dossiers & fichiers.
import os
# requis pour la (dé)sérialisation des objects en json.
from json import JSONEncoder, JSONDecoder
# requis pour ajouter les indices de type pour les listes & les dictionaires.
from typing import List, Dict

### Structures de données

# Cette classe regoupe les libellés des choix possible à une question
class DescriptionChoix:
    def __init__(self, a:str, b:str, c:str, d:str):
        # Ici, on défini quatre variables, une pour chaque choix de réponse possible.
        # La mention :str indique que ces variables sont des chaînes de caractères.
        # Le fait que ces variables soient définies dans la fonction __init__ fait en sorte que chaque instance de la classe aura sa propre copie de chaque variable.
        self.a = a
        self.b = b
        self.c = c
        self.d = d


# Cette classe regoupe la pondération de chaque choix possible à une question.
class PonderationChoix:
    def __init__(self, a:int, b:int, c:int, d:int):
        # Ici, on défini quatre variables, une pour chaque choix de réponse possible.
        # La mention :int indique que ces variables sont des entiers.
        # Le fait que ces variables soient définies dans la fonction __init__ fait en sorte que chaque instance de la classe aura sa propre copie de chaque variable.self.a = a
        self.a = a
        self.b = b
        self.c = c
        self.d = d


# Cette classe défini une question.
class Question:
    def __init__(self, enonce:str, description_choix:DescriptionChoix, ponderation_choix:PonderationChoix):
        # Le fait que ces variables soient définies dans la fonction __init__ fait en sorte que chaque instance de la classe aura sa propre copie de chaque variable.
        # La variable enonce représent l'énoncer de la question et est une chaîne de caractère.
        self.enonce = enonce
        # La variable description_choix est une instance de la classe DescriptionChoix.
        self.description_choix = description_choix
        # La variable ponderation_choix est une instance de la classe PonderatoinChoix.
        self.ponderation_choix = ponderation_choix
        # La variable id contient un identifier unique qui est créé en calculant le hash md5 de la variable énoncer
        # Deux questions ayant des énoncés différents auront ainsi des id différents.
        # Deux questoins avec le même énoncé auront le même id.
        # Les chances que deux énoncé différents se voit attribuer le même hash est très très faible.
        self.id = hashlib.md5(enonce.encode('utf-8')).hexdigest()


class Quiz:
    def __init__(self, nom:str, questions:List[str]):
        # Le fait que ces variables soient définies dans la fonction __init__ fait en sorte que chaque instance de la classe aura sa propre copie de chaque variable.
        # La variable nom est une chaîne de caractère permettant de nommer le quiz
        self.nom = nom
        # La variable questions est une liste d'id appartenant à des questions.
        # Ceci permet de découpler l'implémentation des Quiz de celle des Questions. Si la questions changent de format ceci n'impacte en rien de définition des quiz. Tant et aussi longtemps que les questions conservent une variable id.
        self.questions = questions
        # La variable id contient un identifier unique qui est créé en calculant le hash md5 de la variable énoncer
        # Deux questions ayant des énoncés différents auront ainsi des id différents.
        # Deux questoins avec le même énoncé auront le même id.
        # Les chances que deux énoncé différents se voit attribuer le même hash est très très faible.
        self.id = hashlib.md5(nom.encode('utf-8')).hexdigest()


### Utilitaires de saisie

# Cette fonction sert à lire la saisie d'un utilisateur sous forme de texte.
def lireSaisie(message:str, message_erreur:str) -> str:
    reponse = input(message)

    # ici, on véifie que la réponse n'est pas une chaîne de caractère vide.
    while not reponse:
        reponse = input(message_erreur)

    return reponse


# Cette fonction sert à lire la saisie d'un utilisateur sous forme d'entier
def lireSaisieEntier(message:str, message_erreur:str) -> int:
    saisie:str = input(message)
    reponse:int = 0

    # Ici, on tente de convertir la chaîne de caratère en entier.
    while True:
        try:
            reponse = int(saisie)
            break

        # Si c'est impossible de faire la conversion, on demande une nouvelle entrée a l'utilisateur.
        except ValueError:
            saisie = input(message_erreur)
            continue

    return reponse


# Cette fonction sert à lire la saisie d'un utilisateur sous forme de oui ou de non.
def lireSaiseOuiNon(message:str, message_erreur:str, oui:str="o", non:str="n") -> bool:
    saisie:str = input(message)

    # La fonction lower() converti la chaîne de caractère en minuscule.
    # Ceci permet d'ignorer l'impact de majuscules & minuscules.
    saisie = saisie.lower()

    while True:
        if saisie == oui.lower():
            return True
        elif saisie == non.lower():
            return False

        # Si la saisie est ni oui ni non, on demande à nouveau a l'utilisateur
        saisie = input(message_erreur)


# Cette fonction sert à lire la saisie d'un utilisateur pour 4 choix possible.
def lireSaisieReponse(message: str, message_erreur: str, a: str = "a", b: str = "b", c: str = "c", d: str = "d") -> str:
    saisie:str = input(message)
    # La fonction lower() converti la chaîne de caractère en minuscule.
    # Ceci permet d'ignorer l'impact de majuscules & minuscules.
    saisie = saisie.lower()

    while True:
        if saisie == a.lower():
            return saisie
        elif saisie == b.lower():
            return saisie
        elif saisie == c.lower():
            return saisie
        elif saisie == d.lower():
            return saisie
        # si la saisie n'est pas égale a un des quatre choix, on demande une nouvelle entrée à l'utilisateur.
        saisie = input(message_erreur)

### Utilitaires d'encodage & décodage JSON

# Cette classe permet d'endoer des classe en format json.
class Encodeur(JSONEncoder):
    def __init__(self, **kwargs):
        # Afin de supporter l'encodage utf8, ce qui permet l'usage des accents en français.
        kwargs['ensure_ascii'] = False
        # Ici, on passe les kwargs à la fonction __init__ de la classe mère.
        super(Encodeur, self).__init__(**kwargs)

    # Par défait on encode le dictionaire en json.
    def default(self, o):
        return o.__dict__

# Cette classe sert à décoder les Questions.
class QuestionDecodeur(JSONDecoder):
    def __init__(self):
        # Ici, on enrole la fonction qui sera invoquée afin de décodé les questions.
        JSONDecoder.__init__(self, object_hook=self.conversion)

    def conversion(self, dictionaire):
        # Ici, on retourne les sous objets (DescriptionChoix & PonderationChoix) sans altérations.
        if not ("id" in dictionaire):
            return dictionaire

        # À partir du moment ou la variable id est présente on est rendu à la racine de l'objet à décoder.
        # Tous les if not subséquent servent à valider que le dictionaire contiennent les clef qui sont requises.
        # Si des clefs sont manquante, une question nulle sera retournée.
        if not ("enonce" in dictionaire):
            return

        enonce = dictionaire["enonce"]

        if not ("description_choix" in dictionaire):
            return

        description = dictionaire["description_choix"]

        if not ("a" in description):
            return

        if not ("b" in description):
            return

        if not ("c" in description):
            return

        if not ("d" in description):
            return

        if not ("ponderation_choix" in dictionaire):
            return

        ponderation = dictionaire["ponderation_choix"]

        if not ("a" in ponderation):
            return

        if not ("b" in ponderation):
            return

        if not ("c" in ponderation):
            return

        if not ("d" in ponderation):
            return

        # Ici, on instancie une variable de classe Question avec le contenu de l'objet json.
        question = Question(enonce, DescriptionChoix(description["a"],
                                                     description["b"],
                                                     description["c"],
                                                     description["d"]),
                            PonderationChoix(ponderation["a"],
                                             ponderation["b"],
                                             ponderation["c"],
                                             ponderation["d"]))
        return question


# Cette classe sert à décoder les Quiz.
class QuizDecodeur(JSONDecoder):
    def __init__(self):
        # Ici, on enrole la fonction qui sera invoquée afin de décodé les quiz.
        JSONDecoder.__init__(self, object_hook=self.conversion)

    def conversion(self, dictionaire):
        if not ("id" in dictionaire):
            # Ici, on retourne les sous objets sans altérations.
            # Ceci ne devrait jamais être utilisé, mais des fois que le format changerait.
            return dictionaire

        # À partir du moment ou la variable id est présente on est rendu à la racine de l'objet à décoder.
        # Tous les if not subséquent servent à valider que le dictionaire contiennent les clef qui sont requises.
        # Si des clefs sont manquante, un quiz null sera retourné.
        if not ("nom" in dictionaire):
            return

        nom = dictionaire["nom"]

        if not ("questions" in dictionaire):
            return

        questions = dictionaire["questions"]

        # Ici, on instancie une variable de classe Quiz avec le contenu de l'objet json.
        quiz = Quiz(nom, questions)
        return quiz

### Utilitaires de gestions dossier & fichiers

# Sert à créer un dossier avec un nom donné.
def creerDossier(nom_dossier:str):
    os.makedirs(nom_dossier, exist_ok=True)

# Sert à créer un fichier en format json à partir d'un objet.
def ecrireFichier(dossier_travail:str, objet) -> bool :
    # Ouverture en écriture du fichier. De plus, l'encodage est spéficient en utf8 afin de supporter les accents en français.
    fichier = open(dossier_travail + "/" + objet.id + ".json", "w", encoding='utf-8')

    # Vérifications si le fichier à bien pu être ouvert.
    if fichier.closed:
        return False

    # Encodage de l'objet en format json.
    chaine_json = Encodeur().encode(objet)
    # Écriture du json dans le fichier.
    fichier.write(chaine_json)
    # Fermeture du fichier.
    fichier.close()
    return True

# Permet de lire tous les fichiers questions présents dans un dossier donné.
def lireFichiersQuestion(dossier_questions:str, questions:Dict[str, Question]):
    # Ici, pour chaque fichier trouvés dans le dossier:
    for nom_fichier in os.listdir(dossier_questions):
        # Si le fichier se termine par: ".json"
        if nom_fichier.endswith(".json"):
            # On ouvre le fichier en lecture seule.
            fichier = open(os.path.join(dossier_questions, nom_fichier), "r")

            # Vérification que le fichier à bien été ouvert.
            if fichier.closed:
                continue

            # Création d'une instance du décodeur de question.
            decodeur = QuestionDecodeur()
            # Ici, lecture du fichier & décodage du json en object Question.
            question = decodeur.decode(fichier.read())

            # On vérifie si la question a bien pu être décodée.
            if question is None:
                continue

            # On range la nouvelle question par id dans le dictionnaire des questions.
            questions[question.id] = question

def lireFichiersQuiz(dossier_quiz:str, quiz:Dict[str, Quiz]):
    for nom_fichier in os.listdir(dossier_quiz):
        if nom_fichier.endswith(".json"):
            fichier = open(os.path.join(dossier_quiz, nom_fichier), "r")

            if fichier.closed:
                continue

            # Création d'une instance du décodeur de quiz.
            decodeur = QuizDecodeur()
            # Ici, lecture du fichier & décodage du json en object Quiz.
            quiz_courant = decodeur.decode(fichier.read())

            # On vérifie si la quiz a bien pu être décodé.
            if quiz_courant is None:
                continue

            # On range le nouveau quiz par id dans le dictionnaire des quiz.
            quiz[quiz_courant.id] = quiz_courant

# Utilitaire pour faire subir les quiz
# Cette fonction demande la réponse à chaque question d'un quiz & calcule les points accumulés.
def subirQuiz(questions, quiz:Quiz):
    point_accumules = 0
    total_points = 0

    print("Le quiz: " + quiz.nom + " commence!")

    # Pour toutes les question du quiz
    for id in quiz.questions:
        question = questions[id]

        # Si la question est introuvable, on la saute.
        if not question:
            print("Impossible de trouver la question avec l'identifiant: " + id)
            continue

        # Le total des points met a jour le nombre maximum de points pouvant être accumulés.
        # Le calcul est dynamique, car les questions peuvent être modifiers après qu'un quiz ai été créé.
        # De plus, certaines questions peuvent avoir été effacées sans que les quiz ait été mis à jour.
        total_points += max(question.ponderation_choix.a,
                            question.ponderation_choix.b,
                            question.ponderation_choix.c,
                            question.ponderation_choix.d)

        # Affichage de l'énoncé & des choix de réponse possible.
        print("---------------------------------------------")
        print(question.enonce)
        print("a) " + question.description_choix.a)
        print("b) " + question.description_choix.b)
        print("c) " + question.description_choix.c)
        print("d) " + question.description_choix.d)

        # Saise de la réponse de l'utilisateur.
        # Par défaut les valeurs sont: a, b, c ou d.
        reponse = lireSaisieReponse("Réponse? ", "La réponse n'est pas valide. Répsonse? ")

        # Calcul des points réalisés par l'utilisateur.
        # La fonction getattr permet d'utiliser une chaîne de caractère comme nom de variable (a, b, c ou d) dans la classe PonderationChoix.
        point_accumules += getattr(question.ponderation_choix, reponse)

    # Affichage du score de l'utlisateur.
    print("Vous avez eu: " + str(point_accumules) + " sur un total de: " + str(total_points) + ".")

    # Afin d'éviter les division par zéro.
    if not total_points == 0:
        # Calcul & affichage du pourcentage.
        print("Vouz avez obtenu la note ne pourcentage de: " + str(point_accumules / total_points * 100.0) + "%")

