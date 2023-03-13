import sys, pygame
from Maze import Maze
from random import *

#dessin labyrinthe
def constuct_laby(screen,laby,x,y):
    pygame.draw.rect(screen,pygame.Color('black'),[0,0,700,700])

    pygame.draw.line(screen,pygame.Color('white'),(10,10),(x*50+10,10))
    pygame.draw.line(screen,pygame.Color('white'),(10,10),(10,y*50+10))
    pygame.draw.line(screen,pygame.Color('white'),(10,y*50+10),(x*50+10,y*50+10))
    pygame.draw.line(screen,pygame.Color('white'),(x*50+10,10),(x*50+10,y*50+10))
    for i in laby.get_walls():
        start=i[0]
        end=i[1]
        if start[0]==end[0] :

            if start[1]<end[1]:
                pos_start=(end[1]*50+10,start[0]*50+10)
                pos_end=(end[1]*50+10,50*(start[0]+1)+10)
            else:
                pos_start=(start[1]*50+10,end[0]*50+10)
                pos_end=(start[1]*50+10,50*(end[0]+1)+10)
        else :

            if start[0]<end[0]:
                pos_start=(end[1]*50+10,end[0]*50+10)
                pos_end=((end[1]+1)*50+10,end[0]*50+10)
            else:
                pos_start=(start[1]*50+10,start[0]*50+10)
                pos_end=((start[1]+1)*50+10,start[0]*50+10)
        pygame.draw.line(screen,pygame.Color('white'),pos_start,pos_end)





pygame.init()
pygame.font.init()

size = width, height = 700, 700

screen = pygame.display.set_mode(size)

x=4
y=4
laby=Maze.gen_exploration(x,y)


perso = pygame.transform.scale(pygame.image.load("imgPygame/tickeyBoy.png"),(40,40))
door = pygame.transform.scale(pygame.image.load("imgPygame/door.png"),(40,40))
levelName = pygame.transform.scale(pygame.image.load("imgPygame/levelName.png"),(40,40))
pierreTp =  pygame.transform.scale(pygame.image.load("imgPygame/pierreTp.png"),(40,40))
malusSwitch= pygame.transform.scale(pygame.image.load("imgPygame/malusswitch.png"),(40,40))
cle = pygame.transform.scale(pygame.image.load("imgPygame/cle.png"),(30,30))
serrure = pygame.transform.scale(pygame.image.load("imgPygame/serrure.png"),(40,40))
succes = pygame.transform.scale(pygame.image.load("imgPygame/sucees50l.png"),(300,200))
succescle = pygame.transform.scale(pygame.image.load("imgPygame/suceescle.png"),(300,200))
succestourne = pygame.transform.scale(pygame.image.load("imgPygame/suceestourne.png"),(300,200))

level = True
nblevel=1
pygame.display.set_caption('infini_labyrinthe')
compteurramcle= 0
montrecleSucces = True
montretneSucces = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    constuct_laby(screen,laby,x,y)
    
    pos_perso=(15,15)
    screen.blit(perso,pos_perso)
    coorPerso=(0,0)

    lis=[]
    screen.blit(door,((x-1)*50+15,(y-1)*50+15))
    screen.blit(levelName,(650,10))
    pygame.display.update()
    coor_tp1=(-1,-1)
    coor_tp2=(-1,-1)
    coorMS = (-1,-1)
    coorcle = (-1,-1)

    isouvert = True
    isMs = False
    iscle = False
    listeMs =[]

    if nblevel <=50:
        montre = True
    else:
        montre = False

    montrecle = False
    aff = False
    if montrecleSucces:
        montrecle = True

    compteurtne =-1
    montretne = False
    if montretneSucces:
        montretne = True
        compteurtne = 0

    smallfont = pygame.font.SysFont('nom',40)
    text=smallfont.render(str(nblevel), True , pygame.Color('white'))
    screen.blit(text ,(660,60))

    lis.append(coorPerso)
    lis.append((x-1,y-1))
    if nblevel >=2:
        valcle = randint(1,2)
        if valcle == 1:
            screen.blit(serrure,((x-1)*50+15,(y-1)*50+15))
            isouvert = False
            coorcle=(randint(0,x-1),randint(0,y-1))
            while coorcle in lis: 
                coorcle=(randint(0,x-1),randint(0,y-1))
            lis.append(coorcle)
            iscle = True
            screen.blit(cle,(coorcle[1]*50+20,coorcle[0]*50+25))

    if nblevel >= 5:
        valTp = randint(1,2)
        if valTp ==1:
            coor_tp1=(randint(0,x-1),randint(0,y-1))
            coor_tp2=(randint(0,x-1),randint(0,y-1))
            while coor_tp1 in lis: 
                coor_tp1=(randint(0,x-1),randint(0,y-1))
            lis.append(coor_tp1)
            while coor_tp2 in lis: 
                coor_tp1=(randint(0,x-1),randint(0,y-1))
            lis.append(coor_tp2)
            screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))
            screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))

    if nblevel >=3:
        valSwitch =randint(1,2)
        if valSwitch ==1:
            if nblevel <10:
                nbSwitch = randint(1,2)
            elif nblevel <= 15:
                nbSwitch = randint(3,5)
            else:
                nbSwitch = randint(5,7)
            for i in range(nbSwitch):
                coorMS = (randint(0,x-1),randint(0,y-1))
                while coorMS in lis:
                    coorMS = (randint(0,x-1),randint(0,y-1))
                lis.append(coorMS)
                screen.blit(malusSwitch,(coorMS[1]*50+15,coorMS[0]*50+15))
                listeMs.append(coorMS)
            
            isMs = True
    pygame.display.update()
    while level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if (coorPerso[0]-1,coorPerso[1]) in laby.get_reachable_cells(coorPerso):
                        pygame.draw.rect(screen,pygame.Color('black'),[pos_perso[0],pos_perso[1],40,40])
                        pos_perso = (pos_perso[0],pos_perso[1]-50)
                        coorPerso = (coorPerso[0]-1, coorPerso[1])
                        screen.blit(perso,pos_perso)
                        screen.blit(door,((x-1)*50+15,(y-1)*50+15))
                        if coor_tp1 != (0,0):
                            screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))   
                            screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))
                        if not isouvert:
                            screen.blit(serrure,((x-1)*50+15,(y-1)*50+15))
                        pygame.display.update()
                
                if event.key == pygame.K_DOWN:
                    if (coorPerso[0]+1,coorPerso[1]) in laby.get_reachable_cells(coorPerso):
                        pygame.draw.rect(screen,pygame.Color('black'),[pos_perso[0],pos_perso[1],40,40])
                        pos_perso = (pos_perso[0],pos_perso[1]+50)
                        coorPerso = (coorPerso[0]+1, coorPerso[1])
                        screen.blit(perso,pos_perso)
                        screen.blit(door,((x-1)*50+15,(y-1)*50+15))
                        if coor_tp1 != (0,0):
                            screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))   
                            screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))
                        if not isouvert:
                            screen.blit(serrure,((x-1)*50+15,(y-1)*50+15))
                        pygame.display.update()
                
                if event.key == pygame.K_LEFT:
                    if (coorPerso[0],coorPerso[1]-1) in laby.get_reachable_cells(coorPerso):
                        pygame.draw.rect(screen,pygame.Color('black'),[pos_perso[0],pos_perso[1],40,40])
                        pos_perso = (pos_perso[0]-50,pos_perso[1])
                        coorPerso = (coorPerso[0], coorPerso[1]-1)
                        screen.blit(perso,pos_perso)
                        screen.blit(door,((x-1)*50+15,(y-1)*50+15))
                        if coor_tp1 != (0,0):
                            screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))   
                            screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))
                        if not isouvert:
                            screen.blit(serrure,((x-1)*50+15,(y-1)*50+15))
                        pygame.display.update()
                
                if event.key == pygame.K_RIGHT:
                    if (coorPerso[0],coorPerso[1]+1) in laby.get_reachable_cells(coorPerso):
                        pygame.draw.rect(screen,pygame.Color('black'),[pos_perso[0],pos_perso[1],40,40])
                        pos_perso = (pos_perso[0]+50,pos_perso[1])
                        coorPerso = (coorPerso[0], coorPerso[1]+1)
                        screen.blit(perso,pos_perso)
                        screen.blit(door,((x-1)*50+15,(y-1)*50+15))
                        if coor_tp1 != (0,0):
                            screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))   
                            screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))
                        if not isouvert:
                            screen.blit(serrure,((x-1)*50+15,(y-1)*50+15))
                        pygame.display.update()

            
                if event.key == pygame.K_TAB and aff :
                    aff = False
                    constuct_laby(screen,laby,x,y)
                    screen.blit(perso,pos_perso)
                    screen.blit(door,((x-1)*50+15,(y-1)*50+15))
                    if coor_tp1 != (0,0):
                            screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))   
                            screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))
                    screen.blit(levelName,(650,10))
                    if iscle:
                        screen.blit(cle,(coorcle[1]*50+20,coorcle[0]*50+25))
                    if not isouvert:
                        screen.blit(serrure,((x-1)*50+15,(y-1)*50+15))
                    screen.blit(text ,(660,60))
                    for i in listeMs:
                        screen.blit(malusSwitch,(i[1]*50+15,i[0]*50+15))
                    pygame.display.update()
                    
                if(coorPerso) == (x-1,y-1) and isouvert:
                    level=False
                    if x != 13:
                        x+=1
                        y+=1
                    nblevel+=1
                
                if(coorPerso)==(coor_tp1):
                    pygame.draw.rect(screen,pygame.Color('black'),[pos_perso[0],pos_perso[1],40,40])
                    coorchoice= choice(laby.get_reachable_cells(coor_tp2))
                    pos_perso=(coorchoice[1]*50+15,coorchoice[0]*50+15)
                    coorPerso=(coorchoice[0],coorchoice[1])
                    screen.blit(perso,pos_perso)
                    screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))
                    pygame.display.update()

                if(coorPerso)==(coor_tp2):
                    pygame.draw.rect(screen,pygame.Color('black'),[pos_perso[0],pos_perso[1],40,40])
                    coorchoice= choice(laby.get_reachable_cells(coor_tp1))
                    pos_perso=(coorchoice[1]*50+15,coorchoice[0]*50+15)
                    coorPerso=(coorchoice[0],coorchoice[1])
                    screen.blit(perso,pos_perso)
                    screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))
                    pygame.display.update()

                if (coorPerso) in listeMs and isMs:
                    v = randint(1,3)
                    compteurtne +=1
                    if v == 1:
                        laby=Maze.gen_exploration(x,y)
                    elif v == 2:
                        laby = Maze.gen_fusion(x,y)
                    else:
                        laby = Maze.gen_wilson(x,y)
                    constuct_laby(screen,laby,x,y)
                    screen.blit(perso,pos_perso)
                    screen.blit(door,((x-1)*50+15,(y-1)*50+15))
                    if coor_tp1 != (0,0):
                            screen.blit(pierreTp,(coor_tp1[1]*50+15,coor_tp1[0]*50+15))   
                            screen.blit(pierreTp,(coor_tp2[1]*50+15,coor_tp2[0]*50+15))
                    screen.blit(levelName,(650,10))
                    if iscle:
                        screen.blit(cle,(coorcle[1]*50+20,coorcle[0]*50+25))
                    if not isouvert:
                        screen.blit(serrure,((x-1)*50+15,(y-1)*50+15))
                    listeMs.remove(coorPerso)
                    screen.blit(text ,(660,60))
                    if len(listeMs)==0:
                        isMs = False
                    else:
                        for i in listeMs:
                            screen.blit(malusSwitch,(i[1]*50+15,i[0]*50+15))
                    pygame.display.update()
                    
                if (coorPerso) == (coorcle) and  iscle:
                    isouvert = True
                    screen.blit(door,((x-1)*50+15,(y-1)*50+15))
                    iscle = False
                    compteurramcle +=1
                    pygame.display.update()

                if nblevel ==50 and montre:
                    screen.blit(succes,(200,540))
                    montre = False
                    aff =True
                    pygame.display.update()

                
                if compteurramcle == 10 and montrecle:
                    aff = True
                    screen.blit(succescle,(200,540))
                    montrecleSucces = False
                    montrecle = False
                    pygame.display.update()
                
                if compteurtne == 5 and montretne:
                    aff = True
                    screen.blit(succestourne,(200,540))
                    montretneSucces = False
                    montretne = False
                    pygame.display.update()
    
    level = True
    if x >= 7:
        laby=Maze.gen_fusion(x,y)
    if x == 13:
        val = randint(1,3)
        if val == 1:
            laby=Maze.gen_exploration(x,y)
        elif val == 2:
            laby = Maze.gen_fusion(x,y)
        else:
            laby = Maze.gen_wilson(x,y)
    else:
        laby=Maze.gen_exploration(x,y)
    
