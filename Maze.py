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
    
    @classmethod
    def gen_sidewinder(cls,h, w):
        '''
        méthode de classe qui permet de générer un labyrinthe
        en utilisant l'algorithme de génération sidewinder.
        '''
        mazeS = cls(h,w,False)

        for i in range(h-1):
            seq = []
            for j in range(w-1):
                seq.append((i,j))
                val = randint(1,2)
                if val == 1:
                    cls.remove_wall(mazeS,(i,j),(i,j+1))
                elif val==2:
                    coordIndex = randrange(len(seq))
                    cls.remove_wall(mazeS,seq[coordIndex],(seq[coordIndex][0]+1,seq[coordIndex][1]))
                    seq = []
            seq.append((i,w-1))
            coordIndex = randrange(len(seq))
            cls.remove_wall(mazeS,seq[coordIndex],(seq[coordIndex][0]+1,seq[coordIndex][1]))

        for k in range(w-1):
            cls.remove_wall(mazeS,(h-1,k),(h-1,k+1))
        return mazeS
    
    @classmethod
    def gen_fusion(cls,h,w):
        '''
        méthode de classe qui permet de construire un labyrinthe
        en utilisant l'algorithme de fusion
        '''
        dictLabel={}
        val=1

        mazeF = cls(h,w,False)
        for i in range(h):
            for j in range(w):
                dictLabel[i,j]=val
                val+=1
        listPossibilite = cls.get_walls(mazeF)
        shuffle(listPossibilite)
        
        for possible in listPossibilite:
            if dictLabel[possible[0]] != dictLabel[possible[1]]:
                cls.remove_wall(mazeF,possible[0],possible[1])
                valuecoor = dictLabel[possible[1]]
                for cle in dictLabel.keys():

                    if dictLabel[cle] == valuecoor:
                        dictLabel[cle] = dictLabel[possible[0]]
        
        return mazeF
    

    @classmethod
    def gen_exploration(cls,h,w):
        '''
        méthode de classe qui permet de générer un labyrinthe
        en utilisant l'algorithme de génération par exploration
        '''
        mazeE=cls(h,w,False)
        x = randint(0,h-1)
        y = randint(0,w-1)
        visibilite = {}
        pile = []
        for i in range(h):
            for j in range(w):
                visibilite[i,j] = False
        visibilite[x,y] = True
        pile.append((x,y))

        while len(pile) !=0:
            cell = pile[0]
            del(pile[0])
            visite = True
            cell_contigue =[]
            for k in cls.get_contiguous_cells(mazeE,cell):
                if not visibilite[k]:
                    visite = False
                    cell_contigue.append(k)
            if not visite:
                pile.insert(0,cell)
                c = choice(cell_contigue)
                cls.remove_wall(mazeE,cell,c)
                visibilite[c] = True
                pile.insert(0,c)
        
        return mazeE
    

    @classmethod
    def gen_wilson(cls,h,w):
        '''
        méthode de classe qui permet de générer un labyrinthe
        en utilisant l'algorithme de wilson
        '''
        mazeW=cls(h,w,False)
        x = randint(0,h-1)
        y = randint(0,w-1)
        marquage = {}
        for i in range(h):
            for j in range(w):
                marquage[i,j] = False
        marquage[x,y] = True


        while False in marquage.values() :
            x = randint(0,h-1)
            y = randint(0,w-1)
            listeM = []
            if not marquage[x,y]:
                valM = (x,y)
                listeM.append(valM)
                while not marquage[valM]:
                    
                    valM = choice(cls.get_contiguous_cells(mazeW,valM))
                    if valM in listeM:

                        listeM = listeM[::-1]
                        while listeM[0]!= valM:
                            del(listeM[0])
                        del(listeM[0]) 
                        listeM= listeM[::-1]

                    listeM.append(valM)

            for l in range(len(listeM)-1):
    
                cls.remove_wall(mazeW,listeM[l],listeM[l+1])
                marquage[listeM[l]] = True

        return mazeW

    def overlay(self, content=None):
        """
        Rendu en mode texte, sur la sortie standard, \
        d'un labyrinthe avec du contenu dans les cellules
        Argument:
            content (dict) : dictionnaire tq content[cell] contient le caractère à afficher au milieu de la cellule
        Retour:
            string
        """
        if content is None:
            content = {(i, j): ' ' for i in range(self.height) for j in range(self.width)}
        else:
            # Python >=3.9
            # content = content | {(i, j): ' ' for i in range(
            #    self.height) for j in range(self.width) if (i,j) not in content}
            # Python <3.9
            new_content = {(i, j): ' ' for i in range(self.height) for j in range(self.width) if (i, j) not in content}
            content = {**content, **new_content}
        txt = r""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += " " + content[(0, j)] + " ┃" if (0, j + 1) not in self.neighbors[(0, j)] else " " + content[
                (0, j)] + "  "
        txt += " " + content[(0, self.width - 1)] + " ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += " " + content[(i + 1, j)] + " ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else " " + \
                                                                                                                 content[
                                                                                                                     (
                                                                                                                     i + 1,
                                                                                                                     j)] + "  "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"
        return txt

    def solve_dfs(self,start,stop):
        pile = [start]
        predecesseur = {}
        predecesseur[start]=start
        marquage = {}
        for i in range(self.height ):
            for j in range(self.width ):
                marquage[(i, j)] = False
        marquage[start]=True
        boucle = True
        while False in marquage.values() and boucle:
            c = pile.pop(0)
            if c == stop:
                boucle = False
            else:
                for i in self.get_reachable_cells(c):
                    if not marquage[i]:
                        marquage[i]= True
                        pile.insert(0,i)
                        predecesseur[i]=c
        c = stop
        res = []
        while c != start:
            res.append(c)
            c = predecesseur[c]

        return res

    def solve_bfs(start, stop):
        pile = [start]
        predecesseur = {}
        predecesseur[start] = start
        marquage = {}
        for i in range(self.height):
            for j in range(self.width):
                marquage[(i, j)] = False
        marquage[start] = True
        boucle = True
        while False in marquage.values() and boucle:
            c = pile.pop(0)
            if c == stop:
                boucle = False
            else:
                for i in self.get_reachable_cells(c):
                    if not marquage[i]:
                        marquage[i] = True
                        pile.append(i)
                        predecesseur[i] = c
        c = stop
        res = []
        while c != start:
            res.append(c)
            c = predecesseur[c]

        return res

    def solve_rhr(self,start, stop):

        predecesseur = {}
        predecesseur[start] = start
        marquage = {}

        for i in range(self.height):
            for j in range(self.width):
                marquage[(i, j)] = False

        boucle = True
        c = start
        while boucle and False in marquage.values():
            marquage[c] = True
            if c == stop:
                boucle = False
            else:
                change = False
                for i in self.get_reachable_cells(c):
                    if not marquage[i]:
                        if i not in predecesseur.keys():
                            predecesseur[i] = c
                        c = i
                        change = True

                if change == False:
                    tmp = c
                    c = predecesseur[c]
                    del predecesseur[tmp]
        c = stop
        res = []
        while c != start:

            res.append(c)
            c = predecesseur[c]

        return res
