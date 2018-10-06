import pygame,random
pygame.init()
s = pygame.display.set_mode((600, 600))
s.fill((255,255,0))
i=(0,0,0)
clock=pygame.time.Clock()
ax,ay=((random.randint(0,59))*10,random.randint(0,59)*10)
px,py=0,0
sx,sy=0,0
score=0
pygame.display.set_caption("snake")
length=0
snakelist = [[px,py]]
while (1):
    for x in pygame.event.get():
        if x.type==12:
            print(score)
            pygame.quit()
            quit()
        if x.type==pygame.KEYDOWN:
            if x.key==pygame.K_UP:
                sx=0
                sy=-10
            elif x.key==pygame.K_DOWN:
                sx=0
                sy=10
            elif x.key==pygame.K_LEFT:
                sx=-10
                sy=0
            elif x.key==pygame.K_RIGHT:
                sx=10
                sy=0

    px,py=(px+sx)%600,(py+sy)%600
    if score>3:
        for crash in snakelist:
            if crash==[px,py]:
                print("crash")
                score=score-1
                snakelist.pop(0)
    snakelist.append([px,py])
    z=0
    if ax==px and ay==py:
        z=1
        score=score+1
        while(1):
            ax, ay = ((random.randint(0, 59)) * 10, random.randint(0, 59) * 10)
            if ax!=px and ay!=py:
                break
    if z==0:
        snakelist.pop(0)
    s.fill((225,225,225))
    for j in snakelist:
        pygame.draw.rect(s,(0,0,0),(j[0],j[1],10,10))
    pygame.draw.rect(s, (0, 225, 0), (j[0], j[1], 10, 10))
    pygame.draw.rect(s, (225, 0, 0), (ax, ay, 10, 10))
    pygame.display.update()
    clock.tick(15)
