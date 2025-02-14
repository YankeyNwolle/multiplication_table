# project Table de multiplication

# introduction du projet Table de Multiplication pour permettre à l'utilisateur d'avoir plus de connaisance sur les principes du jeu
import time
def introduction(texte, pause=5):
    print(texte)
    time.sleep(pause)

introduction("Bonjour et Bienvenue à mon projet de Table de Multiplication")

introduction("Voici une bref présentation de mon projet j'èspère qu'il vous plaira dans la suite j'essaie de mieux l'implementer pour qu'il puisse gerer les données dans un fichier bref")
introduction("Introduction")
introduction("Bienvenue dans ce jeu interactif conçu pour évaluer vos connaissances à travers une série de calculs aléatoires. Le programme vous proposera 10 défis, chacun consistant à résoudre une opération mathématique simple.")

introduction("Déroulement du jeu")

introduction("Calculs aléatoires : Deux nombres aléatoires entre 1 et 10 seront générés pour chaque calcul.")
introduction("Répartition des points :")
introduction("2 points si vous trouvez la bonne réponse du premier cours.")
introduction(" 1 point si vous trouvez la bonne réponse du deuxième cours.")      
introduction(" 0 point si vous ne trouvez pas la bonne réponse. Dans ce cas, la réponse correcte vous sera affichée.")   
introduction("Statistiques : À la fin des 10 calculs, vos statistiques détaillées seront affichées :")  
introduction(" Nombre de points obtenus au premier cours.")     
introduction("Nombre de points obtenus au deuxième cours.")     
introduction(" Nombre de questions non trouvées.")     
introduction("Appréciation : Une appréciation globale de votre performance vous sera donnée.")   
introduction("Rejouer : Vous aurez la possibilité de rejouer. Si vous acceptez, le programme sera réinitialisé et vous pourrez recommencer une nouvelle partie. Sinon, le programme s'arrêtera.")   

introduction("Objectifs")  

introduction(" Ce jeu a pour but de :") 

introduction("Évaluer vos connaissances : Testez votre capacité à résoudre des calculs simples.") 
introduction("Améliorer vos compétences : Entraînez-vous à résoudre des opérations mathématiques de manière ludique.") 
introduction("Vous divertir : Passez un moment agréable tout en exerçant votre esprit.")   

introduction("Instructions")

introduction("Appuyez sur la touche <<Entrée>>  pour commencer le jeu.")
introduction("Répondez aux calculs en entrant le résultat dans le champ prévu à cet effet.")
introduction("Appuyez sur <<Entrée>> pour valider votre réponse.")
introduction("NB: il y aura un intervalle de 8 secondes entre chaques question")


# programme pour commencer le jeu
def start_game():
    while True:

        user_input = input("Alors, prêt à relever le défi ? Appuyez sur <<Entrée>>  pour commencer !")

        # Appuie sur la touche << enter >> du clavier pour commencer le jeu
        if not user_input:
            break
    
    # demande le nom de l'utilisateur
    name = input("Quest est votre nom: ").capitalize()

    print()
    print(f"BIENVENUE DANS LE JEU {name}")

start_game()

import random
import time

def generer():
    points, score1, score2, score3, number = 0,0,0,0,1
    while number <= 10:  
        number1 = random.randint(1, 11)
        number2 = random.randint(1, 11)
        print(f"Exercice {number}")
        start_time = time.time()  # Enregistrez le temps de début
        question = input(f"Combien font {number1} x {number2} = ")

        # Vérifiez si le temps de réponse a dépassé 8 secondes
        end_time = time.time()
        if end_time - start_time > 8:
            print("Temps écoulé ! Vous n'obtenez aucun point")
            score3 += 1
            print(f"La bonne réponse était {number1 * number2}")
            number += 1
            continue

        try:
            question = int(question)
        except ValueError:
            print("Erreur : vous devez entrer un nombre.")
            score3 += 1
            print(f"La bonne réponse était {number1 * number2}")
            number += 1
            continue

        response = number1 * number2

        if question == response:
            points += 2
            score1 += 1
            print("Bonne Réponses! Vous obtenez 2 points")
        else:
            print("Tu as droit à une deuxième (2) chance de réfléchir bien!")
            start_time = time.time()  # Enregistrez le temps de début pour la deuxième chance
            question = input(f"Combien font {number1} x {number2} = ")

            # Vérifiez si le temps de réponse a dépassé 8 secondes pour la deuxième chance
            end_time = time.time()
            if end_time - start_time > 8:
                print("Temps écoulé ! Vous n'obtenez aucun point")
                score3 += 1
                print(f"La bonne réponse était {number1 * number2}")
                number += 1
                continue

            try:
                question = int(question)
            except ValueError:
                print("Erreur : vous devez entrer un nombre.")
                score3 += 1
                print(f"La bonne réponse était {number1 * number2}")
                number += 1
                continue

            if question == response:
                points += 1
                score2 += 1
                print("Bonne Réponses! Vous obtenez 1 point")
            else:
                # rien trouver 0 points et le programme doit affichez la réponse à cette question
                score3 += 1
                print("Mauvaise réponse! Vous n'obtenez aucun point")
                print(f"La bonne réponse était {response}")

        number += 1


        if number > 11:
            break

    print("-----FIN DU JEU-----")

    print("STATISTIQUES:")

    print(f"Tu as obtenu {points}/20")
    print(f"Tu as trouver {score1} réponses au premier cours!")
    print(f"Tu as trouver {score2} réponses au deuxème cours!")
    print(f"Tu n' as trouver {score3} questions! courage à toi")

        # le programme va lui donner une appréciation


result = generer()
print(result)

def ask_user():
    # appel de la fonction generer

    while True:
        # le programme doit lui demander s'il veut rejouer si oui le programme sera rénitialiser et reprendre à 0 
        ask = input("Veux tu rejouer la partie si oui tape la lettre <y> or <q> pour quitter le jeux: ").lower()

        if ask == "y":
            generer()

        # si non le programme va s'arrêter pour de bon
        elif ask == "q":
            break

        else:
            print("Saisir incorrect! Veuillez entrer <y> pour continuer ou <q> pour quitter le jeu")

ask_user()

