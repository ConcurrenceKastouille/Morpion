#Jeu du Morpion

def morpion():
    '''Simulation de jeu du morpion.
    Il suffit d'entrer "morpion()" dans la console et le jeu se lance !
    Bon jeu :)
    '''
    Jeu= ["O","O","O",
          "O","O","O",
          "O","O","O"]

    while True:

        #Au tour de joueur 1

        joueur1=input("Joueur 1 place ton X (entre 1 et 9)")

        while Jeu[int(joueur1)-1]=="X" or Jeu[int(joueur1)-1]=="V":
            print("Impossible de placer votre point ici, cette place est déjà prise !")
            joueur1=input("Joueur 1 place ton 1 (entre 1 et 9)")

        del Jeu[int(joueur1)-1]
        Jeu.insert(int(joueur1)-1,"X")

        ligne1=[Jeu[0],Jeu[1],Jeu[2]]
        ligne2=[Jeu[3],Jeu[4],Jeu[5]]
        ligne3=[Jeu[6],Jeu[7],Jeu[8]]

        print(ligne1)
        print(ligne2)
        print(ligne3)

        #On vérifie si Joueur 1 a gagné

        if ligne1==["X","X","X"]:
            return "Le joueur 1 est le gagnant, Bravo !"
        if ligne2==["X","X","X"]:
            return "Le joueur 1 est le gagnant, Bravo !"
        if ligne3==["X","X","X"]:
            return "Le joueur 1 est le gagnant, Bravo !"

        for i in range(3):
            if ligne1[i]=="X" and ligne2[i]=="X" and ligne3[i]=="X":
                return "Le joueur 1 est le gagnant, Bravo !"

        if ligne1[0]=="X" and ligne2[1]=="X" and ligne3[2]=="X":
            return "Le joueur 1 est le gagnant, Bravo !"
        if ligne1[2]=="X" and ligne2[1]=="X" and ligne3[0]=="X":
            return "Le joueur 1 est le gagnant, Bravo !"

        #On vérifie s'il n'y a pas match nul

        if not "O" in Jeu:
            return "Pas de gagnants, match nul"

        #Au tour de joueur 2

        joueur2=input("Joueur 2 place ton V (entre 1 et 9)")

        while Jeu[int(joueur2)-1]=="X" or Jeu[int(joueur2)-1]=="V":
            print("Impossible de placer votre point ici, cette place est déjà prise !")
            joueur2=input("Joueur 2 place ton 2 (entre 1 et 9)")

        del Jeu[int(joueur2)-1]
        Jeu.insert(int(joueur2)-1,"V")

        ligne1=[Jeu[0],Jeu[1],Jeu[2]]
        ligne2=[Jeu[3],Jeu[4],Jeu[5]]
        ligne3=[Jeu[6],Jeu[7],Jeu[8]]

        print(ligne1)
        print(ligne2)
        print(ligne3)

        #On vérifie si Joueur 2 a gagné

        if ligne1==["V","V","V"]:
            return "Le joueur 2 est le gagnant, Bravo !"
        if ligne2==["V","V","V"]:
            return "Le joueur 2 est le gagnant, Bravo !"
        if ligne3==["V","V","V"]:
            return "Le joueur 2 est le gagnant, Bravo !"

        for i in range(3):
            if ligne1[i]=="V" and ligne2[i]=="V" and ligne3[i]=="V":
                return "Le joueur 2 est le gagnant, Bravo !"

        if ligne1[0]=="V" and ligne2[1]=="V" and ligne3[2]=="V":
            return "Le joueur 2 est le gagnant, Bravo !"
        if ligne1[2]=="V" and ligne2[1]=="V" and ligne3[0]=="V":
            return "Le joueur 2 est le gagnant, Bravo !"
        
                #On vérifie s'il n'y a pas match nul

        if not "O" in Jeu:
            return "Pas de gagnants, match nul"
