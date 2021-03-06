import pygame
import random
import time

pygame.init()

print("SELECT LEVEL:\n"
      "EASY\n"
      "MEDIUM\n"
      "HARD\n"
      "DIFFICULT\n")
level=input()
if level =="easy" or "EASY":
    fps=35
elif level =="medium" or "MEDIUM":
    fps=50
elif level =="hard" or "HARD":
    fps=80
elif level =="difficult" or "DIFFICULT":
    fps=110

win=pygame.display.set_mode((600,600))
pygame.display.set_caption("SNAKE GAME")
clock=pygame.time.Clock()
x=10
y=10
dim=10
vel=5
snake_pos=[]

def snake(dim,snake_pos):
    for x in snake_pos:
        pygame.draw.rect(win, (255, 0, 0), [x[0], x[1], dim, dim])
def snakegame():
    gameover=False
    gameend=False

    x1=600/2
    y1=600/2

    x1_change=0
    y1_change=0

    snakelist=[]
    length_of_snake=1

    foodx=round(random.randrange(0,600-dim)/10.0)*10.0
    foody=round(random.randrange(0,600-dim)/10.0)*10.0


    while not gameover:
        while gameend==True:
            score=length_of_snake-1
            score_font=pygame.font.SysFont("comimsansms",30)
            value=score_font.render("Your current score is:"+str(score),True,(0,0,255),)
            win.blit(value,[600/5,600/5])
            pygame.display.update()


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameend=False
                    gameover=True

        #win.fill((0,0,0))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-dim
                    y1_change=0
                if event.key == pygame.K_RIGHT:
                    x1_change = dim
                    y1_change = 0
                if event.key==pygame.K_UP:
                    y1_change=-dim
                    x1_change=0
                if event.key==pygame.K_DOWN:
                    y1_change=dim
                    x1_change=0

        if x1>=600 or x1<0 or y1>=600 or y1<0:
            gameend=True
        x1=x1+x1_change
        y1=y1+y1_change
        win.fill((0,0,0))
        pygame.draw.rect(win,(255,255,0),[foodx,foody,dim,dim])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_pos.append(snake_head)

        if len(snake_pos)>length_of_snake:
            del snake_pos[0]

        for x in snake_pos[:-1]:
            if x==snake_head:
                gameend=True
        snake(dim,snake_pos)
        pygame.display.update()
        if x1==foodx and y1==foody:
            foodx = round(random.randrange(0, 600 - dim) / 10.0) * 10.0
            foody = round(random.randrange(0, 600 - dim) / 10.0) * 10.0
            length_of_snake=length_of_snake+1
        clock.tick(fps)
    pygame.quit()


snakegame()