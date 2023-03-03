from random import *

class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """
    def __init__(self, height, width, empty):
        """
        Constructeur d'un labyrinthe de height cellules de haut 
        et de width cellules de large 
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height    = height
        self.width     = width
      

        if  empty:
            self.neighbors = {}
            for i in range(height):
                for j in range(width):
                    ensemble = set()
                    if i-1 >=0:
                        ensemble.add((i-1,j))
                    if i+1 < height:
                        ensemble.add((i+1,j))
                    if j-1 >=0:
                        ensemble.add((i,j-1))
                    if j+1 < width:
                        ensemble.add((i,j+1))
                    self.neighbors[i,j]= ensemble
        else:
            self.neighbors = {(i,j): set() for i in range(height) for j in range (width)}

                        


    def info(self):
        """
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = f"{self.height} x {self.width}\n"
        txt += str(self.neighbors)
        return txt

    def __str__(self):
        """
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width-1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width-1):
            txt += "   ┃" if (0,j+1) not in self.neighbors[(0,j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height-1):
            txt += "┣"
            for j in range(self.width-1):
                txt += "━━━╋" if (i+1,j) not in self.neighbors[(i,j)] else "   ╋"
            txt += "━━━┫\n" if (i+1,self.width-1) not in self.neighbors[(i,self.width-1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i+1,j+1) not in self.neighbors[(i+1,j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width-1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt
    
    def add_wall(self, c1, c2):
    # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
        0 <= c1[1] < self.width and \
        0 <= c2[0] < self.height and \
        0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
    # Ajout du mur
        if c2 in self.neighbors[c1]:      # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2) # on le retire
        if c1 in self.neighbors[c2]:      # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1) # on le retire
    
  
    def remove_wall(self,c1,c2):
        '''
        méthode qui permet de retirer un mur entre deux case. 
        Prend en paramètre deux coordonnée qui correspond à deux cases.
        Retourne rien.

        c1 : première case
        c2 : deuxième case
        
        '''
        assert 0 <= c1[0] < self.height and \
        0 <= c1[1] < self.width and \
        0 <= c2[0] < self.height and \
        0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        if c2 not in self.neighbors[c1]:      # Si c2 est dans les voisines de c1
            self.neighbors[c1].add(c2) # on le rajoute
        if c1 not in self.neighbors[c2]:      # Si c3 est dans les voisines de c2
            self.neighbors[c2].add(c1) # on le rajoute

    
    def get_walls(self):
        '''
        méthode qui permet de lister les coordonnées de tout les murs du labyrinthe.
        retourne une liste de liste.
        '''
        lst=[]
        GVoisin = self.get_cells()
        
        for key in GVoisin.keys():
            for k in GVoisin[key]:
                l = []
                if k not in self.neighbors[key]:
                    l.append(key)
                    l.append(k)
                    if l[::-1] not in lst:
                        lst.append(l)
        return lst
    


    def get_cells(self):
        '''
        méthode qui sert à lister toute les cases du labyrinthe.
        retourne un dictionnaire.
        '''
        GVoisin = {}
        for i in range(self.height):
                for j in range(self.width):
                    ensemble = set()
                    if i-1 >=0:
                        ensemble.add((i-1,j))
                    if i+1 < self.height:
                        ensemble.add((i+1,j))
                    if j-1 >=0:
                        ensemble.add((i,j-1))
                    if j+1 < self.width:
                        ensemble.add((i,j+1))
                    GVoisin[i,j]= ensemble
        return GVoisin

    def fill(self):
        '''
        méthode qui permet d'ajouter tout les murs posible du labyrinthe.
        retourne rien
        '''
        for i in range(self.height):
            for j in range(self.width):
                self.neighbors[i,j] = set()
        return None


    def empty(self):
        '''
        méthode qui permet d'enlever tout les murs possible du labyrinthe.
        retourne rien
        '''
        GVoisin = self.get_cells()
        for i in range(self.height):
            for j in range(self.width): 
                self.neighbors[i,j]= GVoisin[i,j]
                    
        return None

    def get_contiguous_cells(self, c):
        '''
        méthode qui permet de lister les cases voisines d'une coordonné pris en paramètre.
        retourne une liste
        '''
        GVoisin = self.get_cells()
        lst = []
        for i in GVoisin[c]:
            lst.append(i)
        return lst

    def get_reachable_cells(self,c):
        '''
        méthode qui permet de lister les cases accessibles d'une coordonné pris en paramètre.
        retourne une liste
        '''
        lst = []
        for i in self.neighbors[c]:
            lst.append(i)
        return lst

    
    @classmethod
    def gen_btree(cls,h, w):
        '''
        méthode de classe qui permet de génerer un labyrinthe sous forme d'arbre binaire.
        retourne un objet de la classe 
        '''
        mazeb = cls(h,w, False)
        for i in range(h):
            for j in range(w):
                val = randint(1,2)
                if val == 1:
                    if (i+1,j) in cls.get_contiguous_cells(mazeb,(i,j)):
                        cls.remove_wall(mazeb,(i,j),(i+1,j))
                    elif (i,j+1) in cls.get_contiguous_cells(mazeb,(i,j)):
                        cls.remove_wall(mazeb,(i,j),(i,j+1))
                elif val == 2:
                    if (i,j+1) in cls.get_contiguous_cells(mazeb,(i,j)):
                        cls.remove_wall(mazeb,(i,j),(i,j+1))
                    elif (i+1,j) in cls.get_contiguous_cells(mazeb,(i,j)):
                        cls.remove_wall(mazeb,(i,j),(i+1,j))
        return mazeb