import random
import tkinter as tk
import logging
import sys
logging.basicConfig(level=logging.DEBUG,
                    filename="jeux3.log", 
                    filemode="a", 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.warning("Début du script")
print("""  
        
                 ***Regle du jeux***

Vous vous battez contre un monstre. Vous avez trois caractheristiques : ( donnés aleatoirement en debut de partis ) 

    - Agilité : permet de fuir l'enemie plus facilement.
    - Force : permet d'ataquer l'enemie plus fort
    - Chance : permet d'obtenir plus de point de vie avec les potions

    Le but est de mettre l'aversaire en dessous de 1 point de vie si vous le faites vous gagnez, dans le cas contraire vous perdez.
     Conseils : 
     1. établissez une stratégie suivant les caractheristiques de départs 
     2. lorsque vous n'avez plus de potions vous pouvez lancer une piece sur pile ou face et avoir la chance d'en gagner de nouvelles """)   
print("-" * 50)

lvl_choice = ["1", "2", "3"]

class Game():
    def __init__(self):
        logging.debug("Lancement du choix du niveau.")
        self.lvl = input("Veuillez choisir un niveau de difficulté : \n1.Facile \n2.Moyen \n3.Difficile \n=>")
        while self.lvl in lvl_choice:
            if self.lvl == "1":
                self.player_1 = 150
                self.monster = 100
                self.potions = 3
                self.agilite = random.randint(50, 100)
                self.force = random.randint(50, 100)
                self.chance = random.randint(50, 100)
                self.potion_value = random.randint(20, 30)
                self.atk_value = random.randint(15, 25)
                self.monster_atk_value = random.randint(10, 25)
                self.choice_menu = {1: "Attaque", 2: "Utiliser une potion", 3: "Fuir"}
                print("INFO : Niveau 1.")
                print("Initialisation des variables du jeux .... : ok.")
                logging.info(f"""LVL 1. self.player_1 = 150
                monster {self.monster}
                potions {self.potions}
                agilite {self.agilite}
                force {self.force}
                chance {self.chance}
                atk_value {self.atk_value}
                monster_atk_value {self.monster_atk_value}""")
                self.start()
            elif self.lvl == "2":
                self.player_1 = 150
                self.monster = 150
                self.potions = 3
                self.agilite = random.randint(40, 100)
                self.force = random.randint(40, 100)
                self.chance = random.randint(40, 100)
                self.potion_value = random.randint(15, 30)
                self.atk_value = random.randint(15, 25)
                self.monster_atk_value = random.randint(15, 25)
                self.choice_menu = {1: "Attaque", 2: "Utiliser une potion", 3: "Fuir"}
                print("INFO : Niveau 2.")
                print("Initialisation des variables du jeux .... : ok.")
                logging.info(f"""LVL 2. self.player_1 = 150
                monster {self.monster}
                potions {self.potions}
                agilite {self.agilite}
                force {self.force}
                chance {self.chance}
                atk_value {self.atk_value}
                monster_atk_value {self.monster_atk_value}""")
                self.start()
            elif self.lvl == "3":
                self.player_1 = 175
                self.monster = 200
                self.potions = 2
                self.agilite = random.randint(10, 100)
                self.force = random.randint(10, 100)
                self.chance = random.randint(10, 100)
                self.potion_value = random.randint(10, 30)
                self.atk_value = random.randint(15, 35)
                self.monster_atk_value = random.randint(20, 35)
                self.choice_menu = {1: "Attaque", 2: "Utiliser une potion", 3: "Fuir"}
                print("INFO : Niveau 3.")
                print("Initialisation des variables du jeux .... : ok.")
                logging.info(f"""LVL 3. self.player_1 = 150
                monster {self.monster}
                potions {self.potions}
                agilite {self.agilite}
                force {self.force}
                chance {self.chance}
                atk_value {self.atk_value}
                monster_atk_value {self.monster_atk_value}""")
                self.start()
            else:
                logging.error(f"Retour choix du niveau '{self.lvl}'")
                self.__init__()
        else:
            self.__init__()
    def start(self):
        print("\n\n=== Lancement d'une Partie ===\n\n")
        logging.debug("=== Lancement d'une Partie ===")
        print(f"\n= Caracthéristique de la partie =\n\nAgilité : {self.agilite}\nForce : {self.force}\nChance : {self.force} \nPv joueur :{self.player_1} \nPv monstre :{self.monster} \npotions :{self.potions}")
        while self.player_1 >= 1 and self.monster >= 1:
            self.player_action = self.get_player_choice()
            print(f"=====\nle joueur choisi l'action : {self.choice_menu[self.player_action]}\n=====")
            logging.info(f"=====\nle joueur choisi l'action : {self.choice_menu[self.player_action]}\n=====")
            self.do_action(self.player_action)
            self.monster_action()
            print(f"======\n Fin du Tour \n\n player : {self.player_1} \n monster : {self.monster} \n potion : {self.potions} \n ======\n")
            logging.info(f"======\n Fin du Tour \n\n player : {self.player_1} \n monster : {self.monster} \n potion : {self.potions} \n ======\n")
        else:
            print(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
            logging.info(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
            logging.warning("Fermeture du script.")
            sys.exit()
    def get_player_choice(self):
        while self.player_1 >= 1 and self.monster >= 1:
            input_value = None 
            while input_value not in self.choice_menu.keys():
                try:
                    input_value = int(input("====== \n Veuillez choisir une action : \n1- Attaquer \n2- Utiliser une potion \n3- Fuir \n ======\n=>"))
                    if input_value in self.choice_menu.keys():
                        return input_value
                    else:
                        print("Veuillez entrer un nombre entre 1 et 4")
                        logging.error("Veuillez entrer un nombre entre 1 et 4")
                except Exception:
                    print("merci de rentrer un chiffre, et uniquement un chiffre. ")
                    logging.error("merci de rentrer un chiffre, et uniquement un chiffre. ")
        else:
            print(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
            logging.info(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
            logging.warning("Fermeture du script.")
            sys.exit()
    def do_action(self, input_value):
        if input_value == 1:
            if self.force < 50:
                print(f"le joueur frappe le monstre et lui retire {self.atk_value} points de vie.")
                logging.info(f"le joueur frappe le monstre et lui retire {self.atk_value} points de vie.")
                self.monster -= self.atk_value
            elif self.force >= 50 and self.force < 75:
                print(f"le joueur frappe le monstre et lui retire {self.atk_value} points de vie.")
                logging.info(f"le joueur frappe le monstre et lui retire {self.atk_value} points de vie.")
                self.monster -= self.atk_value * 1.2
            elif self.force >= 75:
                print(f"le joueur frappe le monstre et lui retire {self.atk_value} points de vie.")
                logging.info(f"le joueur frappe le monstre et lui retire {self.atk_value} points de vie.")
                self.monster -= self.atk_value * 1.4
        elif input_value == 2 and self.potions > 0:
            if self.chance < 50:
                self.player_1 += self.potion_value
                self.potions -= 1
                print(f"le joueur utilise une potion qui lui octroie {self.potion_value} points de vie.")
                logging.info(f"le joueur frappe le monstre et lui retire {self.potion_value} points de vie.")
            elif self.chance >= 50 and self.chance < 75:
                self.player_1 += self.potion_value * 1.2
                self.potions -= 1
                print(f"le joueur utilise une potion qui lui octroie {self.potion_value} points de vie.")
                logging.info(f"le joueur frappe le monstre et lui retire {self.potion_value} points de vie.")
            elif self.chance >= 75:
                self.player_1 += self.potion_value * 1.4
                self.potions -= 1
                print(f"le joueur utilise une potion qui lui octroie {self.potion_value} points de vie.")
                logging.info(f"le joueur frappe le monstre et lui retire {self.potion_value} points de vie.")
        elif input_value == 2 and self.potions == 0:
            piece = random.randint(1, 2)
            print("Vous lancez votre piece ......")
            logging.info("Lance une piece")
            if piece == 1 and self.chance < 50:
                print(f"La piece tombe sur Pile : Vous gagnez 1 potion ! \nPotions : {self.potions}")
                logging.info(f"La piece tombe sur Pile : Vous gagnez 1 potion ! \nPotions : {self.potions}")
                self.potions += 1
            elif piece == 1 and self.chance >= 50:
                print(f"La piece tombe sur Pile : Vous gagnez 2 potion ! \nPotions : {self.potions}")
                logging.info(f"La piece tombe sur Pile : Vous gagnez 2 potion ! \nPotions : {self.potions}")
                self.potions += 2
            elif piece == 2:
                print(f"La piece tombe sur Face : Vous gagnez 0 potion ! \nPotions : {self.potions}")
                logging.info(f"La piece tombe sur Pile : Vous gagnez 0 potion ! \nPotions : {self.potions}")
                self.potions += 0
        elif input_value == 3:
            if self.agilite < 50:
                fuite = random.randint(1, 4)
                if fuite == 1:
                    print("le joueur a fuit la partie")
                    logging.info("le joueur a fuit la partie")
                    print(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
                    logging.info(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
                    logging.warning("Fermeture du script.")
                    sys.exit()
                else:
                    print("Vous n'avez pas réussis a prendre la fuite")
                    logging.info("Vous n'avez pas réussis a prendre la fuite")
            elif self.agilite >= 50 and self.agilite < 80:
                fuite = random.randint(1,3)
                if fuite == 1:
                    print("le joueur a fuit la partie")
                    logging.info("le joueur a fuit la partie")
                    print(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
                    logging.info(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
                    logging.warning("Fermeture du script.")
                    sys.exit()
                else:
                    print("Vous n'avez pas réussis a prendre la fuite")
                    logging.info("Vous n'avez pas réussis a prendre la fuite")
            elif self.agilite >= 80:
                fuite = random.randint(1,2)
                if fuite == 1:
                    print("le joueur a fuit la partie")
                    logging.info("le joueur a fuit la partie")
                    print(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
                    logging.info(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
                    logging.warning("Fermeture du script.")
                    sys.exit()
                else:
                    print("Vous n'avez pas réussis a prendre la fuite")
                    logging.info("Vous n'avez pas réussis a prendre la fuite")
    def monster_action(self):
        while self.player_1 >= 1 and self.monster >= 1:
            print("Au tour du monstre ! \n")
            logging.info("Au tour du monstre ! \n")
            self.player_1 -= self.monster_atk_value
            print(f"le monstre attaque et vous retire {self.monster_atk_value} points de vie.\n ======")
            logging.info(f"le monstre attaque et vous retire {self.monster_atk_value} points de vie.\n ======")
            break
        else:
            print(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
            logging.info(f"Fin de la partie : \n pv du joueur : {self.player_1} \n pv du monstre : {self.monster}")
            logging.warning("Fermeture du script.")
            sys.exit()
if __name__ == "__main__":
    logging.debug("Execution du script\n")
    Game().start()