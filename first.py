import pygame
import time
pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Eagle-Warrior Created By ANAN")
clock=pygame.time.Clock()
walkright=[pygame.image.load("assets/R1.png"),pygame.image.load("assets/R2.png"),pygame.image.load("assets/R3.png"),pygame.image.load("assets/R4.png"),pygame.image.load("assets/R5.png"),pygame.image.load("assets/R6.png"),pygame.image.load("assets/R7.png"),pygame.image.load("assets/R8.png"),pygame.image.load("assets/R9.png")]
walkleft=[pygame.image.load("assets/L1.png"),pygame.image.load("assets/L2.png"),pygame.image.load("assets/L3.png"),pygame.image.load("assets/L4.png"),pygame.image.load("assets/L5.png"),pygame.image.load("assets/L6.png"),pygame.image.load("assets/L7.png"),pygame.image.load("assets/L8.png"),pygame.image.load("assets/L9.png")]
bg=pygame.image.load("assets/bg2.jpg")
stand=pygame.image.load("assets/standing.png")
hitsound=pygame.mixer.Sound("assets/hit.wav")
bulletsound=pygame.mixer.Sound("assets/bullet.wav")
backsound=pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.play(-1)
score=0
class player:
    def __init__(self):
        self.x = 0
        self.y = 420
        self.width = 65
        self.height = 65
        self.velocity = 8
        self.walkcount = 0
        self.jumpcount = 8
        self.isjump = False
        self.left = False
        self.right = False
        self.stand=True
        self.hitbox = (self.x + 15, self.y + 11, 29, 52)
    def draw(self):
        if self.walkcount > 9:
            self.walkcount = 0
        if self.stand == False:
            if self.left == True:
                win.blit(walkleft[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
            elif self.right == True:
                win.blit(walkright[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
        else:
            if self.left == True:
                win.blit(walkleft[0], (self.x, self.y))

            else:
                win.blit(walkright[0], (self.x, self.y))
        self.hitbox=(self.x+17,self.y+11,29,52)
        #pygame.draw.rect(win,(0,255,255),self.hitbox,1)
    def hit(self):
        if self.left==True:
            self.x=340
            self.y=self.y
        else:
            self.x = 60
            self.y = self.y
        hitshot=pygame.font.SysFont("comiscus",100)
        hitshot2=hitshot.render("-1",-1,(255,0,0))
        win.blit(hitshot2,(250-int((hitshot2.get_width()/2)),200))
        pygame.display.update()
        time.sleep(0.2)




class projectile:
    def __init__(self):
        self.x=round(soldier.x+soldier.width/2)
        self.y=round(soldier.y+soldier.height/2)
        self.radius=6
        self.color=(255,0,0)
        if soldier.left:
            self.face = -1
        else:
            self.face = 1
        self.velocity=8*self.face
    def draw(self):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
class enemy:
    walkright=[pygame.image.load("assets/R1E.png"),pygame.image.load("assets/R2E.png"),pygame.image.load("assets/R3E.png"),pygame.image.load("assets/R4E.png"),pygame.image.load("assets/R5E.png"),pygame.image.load("assets/R6E.png"),pygame.image.load("assets/R7E.png"),pygame.image.load("assets/R8E.png"),pygame.image.load("assets/R9E.png")]
    walkleft=[pygame.image.load("assets/L1E.png"),pygame.image.load("assets/L2E.png"),pygame.image.load("assets/L3E.png"),pygame.image.load("assets/L4E.png"),pygame.image.load("assets/L5E.png"),pygame.image.load("assets/L6E.png"),pygame.image.load("assets/L7E.png"),pygame.image.load("assets/L8E.png"),pygame.image.load("assets/L9E.png")]
    def __init__(self):
        self.x = 150
        self.y = 420
        self.width = 65
        self.height = 65
        self.end = 300
        self.walkcount = 0
        self.velocity = 4
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health=5
        self.visible=True
    def draw(self):
        self.move()
        if self.visible==True:
            if self.walkcount>9:
                self.walkcount=0
            if self.velocity>0:
                win.blit(self.walkright[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            else:
                win.blit(self.walkleft[self.walkcount // 3],(self.x,self.y))
                self.walkcount += 1
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255,0, 0), (self.x, self.y - 10, 50, 8))
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - 10, 50 - (10*(5-self.health)), 8))



            #pygame.draw.rect(win,(0,255,255),(self.x + 17, self.y + 2, 31, 57),1)
    def move(self):
        if self.velocity>0:
            if self.end > self.x:
                self.x+=self.velocity
            else:
                self.velocity*=-1
                self.walkcount=0
        else:
            if self.x!=150:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walkcount = 0

def redrawgamewindow():
    win.blit(bg, (0, 0))
    sfont=fs.render("Score:"+str(score),1,(255,255,255))
    win.blit(sfont,(400,10))
    intro = pygame.font.SysFont("calibri", 16, True)
    mainintro = intro.render("Eagle-Warrior Created By ANAN", 1, (250, 128, 114))
    win.blit(mainintro, (0, 0))
    soldier.draw()
    foe.draw()
    for bullet in bullets:
        bullet.draw()
    pygame.display.update()
foe=enemy()
soldier=player()
bulletloop=0
bullets=[]
fs=pygame.font.SysFont("vijaya",30)
run = True
while run:
    clock.tick(27)
    if soldier.hitbox[1] < foe.hitbox[1] + foe.hitbox[3] -5 and soldier.hitbox[1] + soldier.hitbox[3] > foe.hitbox[1] -5 :
        if soldier.hitbox[0] + soldier.hitbox[2] -15> foe.hitbox[0] and  soldier.hitbox[0]+10< foe.hitbox[0] + foe.hitbox[2]:
            if foe.visible == True:
                soldier.hit()
                hitsound.play()
                score -= 1
    if bulletloop>0:
        bulletloop+=1
    if bulletloop>3:
        bulletloop=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
    if foe.health==0:
        foe.visible=False
    for bullet in bullets:
        if bullet.y - bullet.radius < foe.hitbox[1] + foe.hitbox[3] and bullet.y + bullet.radius > foe.hitbox[1]:
            if bullet.x + bullet.radius > foe.hitbox[0] and bullet.x - bullet.radius < foe.hitbox[0] + foe.hitbox[2]:
                if foe.visible==True:
                    hitsound.play()
                    score += 1
                    foe.health -= 1
                    bullets.pop(bullets.index(bullet))

        if bullet.x<500 and bullet.x > 0:
            bullet.x+=bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and bulletloop==0:
        bulletsound.play()
        if len(bullets)<3:
            bullets.append(projectile())
        bulletloop=1
    if keys[pygame.K_LEFT] and soldier.x>0:
        soldier.x-=soldier.velocity
        soldier.left=True
        soldier.right=False
        soldier.stand=False
    elif keys[pygame.K_RIGHT] and soldier.x+soldier.width<500:

        soldier.x+=soldier.velocity
        soldier.left=False
        soldier.right=True
        soldier.stand=False
    else:
        soldier.stand=True
        soldier.walkcount=0
    if soldier.isjump==False:
        if keys[pygame.K_UP]:
            soldier.isjump = True
            soldier.standing=True
            soldier.walkcount=0
    else:
        if soldier.jumpcount>=-8:
             neg=1
             if soldier.jumpcount<0:
                neg=-1
             soldier.y-=int((soldier.jumpcount**2)*0.5*neg)
             soldier.jumpcount-=1
        else:
            soldier.isjump = False
            soldier.jumpcount=8

    redrawgamewindow()
pygame.quit()