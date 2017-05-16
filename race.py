
# import 
import pygame
import random
import time

pygame.init()

#colors

white = (255,255,255)
black = (0,0,0)
red = (200,0,0,100)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)
blue = (53,115,255)

# width and height

width = 800
height = 600
# score
scores = 0

#set width and height of display

screen = pygame.display.set_mode((width ,height))
#define clock
clock = pygame.time.Clock()

#fonts

bigfont = pygame.font.Font("font/fill.ttf",50)
smallfont = pygame.font.Font("font/fill.ttf", 40)
medfont = pygame.font.Font("font/fill.ttf", 200)
largefont = pygame.font.Font("font/fill.ttf", 90)
largefont1 = pygame.font.Font("font/fill.ttf", 120)

#loading images
car = pygame.image.load("image/race.png")

#def fonts

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "big":
        textSurface = bigfont.render(text, True, color)

    return textSurface, textSurface.get_rect()
#def message to screen

def message_to_screen(msg,color,y_displace=0,size = "b"):
    textSurf, textRect = text_objects(msg,color,size)
  
    textRect.center = (int(width/2),int(height/2)+y_displace)
    screen.blit(textSurf, textRect)
    
def text_to_button1(msg,color,buttonx,buttony,buttonwidth,buttonheight,x_displace = 0,size = "big"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
    screen.blit(textSurf , textRect) 

def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size = "small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
    screen.blit(textSurf , textRect)
#defining timer

def timer():    
    screen.fill(white)
    gm_msg = ["Go", "Steady", "Ready"] 
    for i in range(3, 0, -1):
        message_to_screen(str(i), black, size="large")

        message_to_screen(gm_msg[i - 1],red,y_displace = -100,size="large")

        pygame.display.update()
        screen.fill(white)
        time.sleep(1)
    gameLoop()

font = pygame.font.SysFont(None, 25)
#def button
def button(text, x, y, width, height, inactive_color, active_color,action = None):
    global game_cont
    global game_mode
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    


    if x + width > cur[0] > x and y + height > cur[1] > y:
    
        pygame.draw.rect(screen, active_color, (x,y,width,height))

        text_to_button1(text,black,x,y,width,height,x_displace = 20,size="big")
          

        



        if click[0] == 1 and action != None:
            if action == "Quit":
                
                
                pygame.quit()
               

            if action == "Modes":
                
                game_cont = True
                
            if action == "play":
                
          

                

                timer()
              
            if action == "menu":
                
               
                game_intro()
            if action == "c":
                gameLoop()           

    else:
        pygame.draw.rect(screen, inactive_color, (x,y,width,height))
        text_to_button1(text,black,x,y,width,height,x_displace = 20,size="big")

def things(x,y,w,h):
    pygame.draw.rect(screen,white,[x,y,w,h])

    
#def car(race_x,race_y):
     
  
    
def score():
    global scores, text
    scores += 5
def pause():
    paused = True
    message_to_screen("paused",red,-100,size="medium")
  
    
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event .key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
      

        
        clock.tick(5)
                

def game_intro1():

    intro = True
    race_x = 35
    race_y = 361
    speed = 5
    
    while intro:
        for event in pygame.event.get():
            print event             
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameLoop()        

        screen.fill(green)
        screen.blit(car,(race_x,race_y))
        race_x += speed 
        if race_x >= width:
           race_x = 35 
     
        message_to_screen("welcome to Car run",black,-100,"large")
        message_to_screen("Press c to continue",black,220,"big")
        
  
  
        pygame.display.update()
                        

def game_intro():

    intro = True
    
    while intro:
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        message_to_screen("You crashed",red,10,"large")

              
        button("play", 250,500,100,50, green, light_green,action="play" )
        
        button("Quit", 500,500,100,50, red, light_red,action="Quit") 
        pygame.display.update()
                        



def gameLoop():
    global scores,text
    gameExit = False
    gameOver = True
    speed = 5
    y = -600
    x = random.randrange(0,width-100)
    car_x = (276)
    wheel_x = 346
    wheel_y = 568
    car_y = (523)
    car_x_change=0
    wheel_x_change=0

  
    w = 100
    h = 100
    while not gameExit:
        for event in pygame.event.get():
    
            if event.type ==  pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                    wheel_x_change = -5
                elif event.key == pygame.K_RIGHT:
                    car_x_change = 5
                    wheel_x_change = 5
                if event.key == pygame.K_p:
                    pause()    
                 

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    car_x_change = 0
                    wheel_x_change = 0
                if event.key == pygame.K_RIGHT:
                    car_x_change = 0
                    wheel_x_change = 0               
        car_x += car_x_change
        wheel_x += wheel_x_change

        screen.fill(black)
        text = smallfont.render("score: "+str(scores),True,white)
        screen.blit(text, [0,0])
        screen.blit(car,(car_x,car_y))
 
        things(x,y,w,h)
        y += speed
        if y > width:
            score()
            y = 0
            x = random.randrange(0,width-100)
            speed += 1
            w += 1
        if  car_x >= width:
            car_x = 25
            car_y = 523
        if  car_x < 0:
            car_x = 795
            car_y = 523
        if car_y < y+h and car_x > x and car_x < x+w or car_x+100>x and car_x + 100 < x+100:
            scores = 0
          

               
            game_intro()
                
               





            
        pygame.display.update()
        clock.tick(60)
game_intro1()        
game_intro()              
gameLoop()                    




