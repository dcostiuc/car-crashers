#Car Crashers Game
import pygame
import time
import random

#Initializing Pygame
pygame.init()

#Setting variables for convenience
displayWidth = 1100
displayHeight = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
darkRed = (200,0,0)
green = (0,255,0)
darkGreen  = (0,200,0)
blue = (0,0,255)
darkBlue = (0,0,200)


blockColor = (53,115,255)

carWidth = 191

#Creates Pygame window
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Car Crashers')
clock = pygame.time.Clock()

carPic = 'car.png'
carImage = pygame.image.load(carPic)
 
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)



#Defining Functions

def highScoreViewer(scores, gameScore, cheats):
    
    gameDisplay.fill(white)
    back = False
    
    largeTxt = pygame.font.Font ('freesansbold.ttf', 70)
    textSurf, textRect = textObjects ("Highscores:", largeTxt, blockColor)
    textRect.center = ((displayWidth/2 , (displayHeight/2) - 200))
    gameDisplay.blit (textSurf, textRect)

    smallTxt = pygame.font.Font ('freesansbold.ttf', 40)
    height = 0
    #print("High Score Viewer:")
    #print(cheats)
    for score in scores:
        if cheats.get(score) == 'y':
            msg = "(With Cheats)"
        else:
            msg = "(Without Cheats)"
        if score == gameScore:
            colour = darkRed
        else:
            colour = darkGreen
        textSurf2, textRect2 = textObjects (str(score), largeTxt, colour)
        textRect2.center = ((displayWidth/2 - 130 , (displayHeight/2) - 120 + height))
        gameDisplay.blit (textSurf2, textRect2)
        #pygame.display.update()

        textSurf3, textRect3 = textObjects (msg, smallTxt, colour)
        textRect3.center = ((displayWidth/2 + 120, (displayHeight/2) - 120 + height))
        gameDisplay.blit (textSurf3, textRect3)
        
        pygame.display.update()
        height += 80

    while back == False:
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    back = True

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            button("Back",0,displayHeight - 75,150,75,darkRed,red, backThing)
            
            if 150 >  mouse [0] > 0 and displayHeight > mouse [1] > 75:
                if click [0] == 1:
                    back = True
            
    
    gameDisplay.fill(white)
        
def highScoreAdder(gameScore, cheated):
    cheatsDict  = {}
    newScores = []
    cheater = 'n'

    if cheated:
        cheater = 'y'

    file = open('highscores.txt', 'r')
    scores = file.readline().split(',')
    scores.pop()
    #print(scores)
    for each in scores:
        scores[scores.index(each)] = int(each.strip())
        #print(each)
    #print(scores)
    cheats = file.readline().split(',')
    #print(cheats)
    
    i= -1
    for each in scores:
        i += 1
        cheatsDict [each] = cheats [i]
    
    cheatsDict [gameScore] = cheater
    if gameScore >= min(scores) and gameScore not in scores:
        scores.append(gameScore)
        #print("Right before while loop:",scores)
        while len(scores) > 0:
            target = int(max(scores))
            newScores.append(target)
            scores.remove(target)
        newScores.pop()
    else:
        newScores = scores
    #print(newScores)
    #print(scores)
    file.close()

    
    file = open('highscores.txt', 'w')
    for each in newScores:
        file.write(str(each) + ",")
    file.write('\n')
    for each in newScores:
        file.write(cheatsDict.get(each) + ",")
    file.close()
    return newScores, cheatsDict

#Pseudo-function, doesn't actually do anything    
def backThing():
    pygame.display.update
    ()

def carSelect(carWidth):
    time.sleep(0.3)
    gameDisplay.fill(white)
    carSelected = False
    bestCar = False
    largeTxt = pygame.font.Font ('freesansbold.ttf', 70)
    textSurf, textRect = textObjects ("Select your Car: ", largeTxt, blue)
    textRect.center = ((displayWidth/2 , (displayHeight/2) - 100))
    gameDisplay.blit (textSurf, textRect)


    car1X = displayWidth/2 - 300
    car1Y = displayHeight/2 + 70
 
    car2X = displayWidth/2 + 50
    car2Y = displayHeight/2 + 75

    car3X = displayWidth/2 - 110
    car3Y = displayHeight/2

    while carSelected == False:
        gameDisplay.blit (textSurf, textRect)
        
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    bestCar = not bestCar
                    if bestCar == False:
                        gameDisplay.fill(white)


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #gameDisplay.blit(pygame.image.load('car2.png'), (car2X, car2Y))

        if car1X + carWidth > mouse [0] > car1X and car1Y + 79 > mouse [1] > car1Y:    
            gameDisplay.blit(pygame.image.load('carINVINCIBLE.png'), (car1X, car1Y))
            
            if click [0] == 1:
                carPic = 'car.png'
                carInv = 'carINVINCIBLE.png'
                carSelected = True
                return carPic, carInv
                            
        else:
            gameDisplay.blit(pygame.image.load('car.png'), (car1X, car1Y))



        
        if car2X + carWidth > mouse [0] > car2X and car2Y + 72 > mouse [1] > car2Y:    
            gameDisplay.blit(pygame.image.load('car2INVINCIBLE.png'), (car2X, car2Y))
           
            if click [0] == 1:
                carPic = 'car2.png'
                carInv = 'car2INVINCIBLE.png'
                carSelected = True
                return carPic, carInv
                          
        else:
            gameDisplay.blit(pygame.image.load('car2.png'), (car2X, car2Y))
        
        if bestCar == True:
            carWidth = 170
            if car3X + carWidth > mouse [0] > car3X and car3Y + 52 > mouse [1] > car3Y:    
                gameDisplay.blit(pygame.image.load('car3INVINCIBLE.png'), (car3X, car3Y))
                
                if click [0] == 1:
                    carPic = 'car3.png'
                    carInv = 'car3INVINCIBLE.png'
                    carSelected = True
                    return carPic, carInv
                                
            else:
                gameDisplay.blit(pygame.image.load('car3.png'), (car3X, car3Y))

            
        pygame.display.update()
        clock.tick(15) 

def scoreDisplay(dodged):
    largeTxt = pygame.font.Font ('freesansbold.ttf', 70)
    textSurf, textRect = textObjects ("Score: " + str(dodged), largeTxt, blockColor)
    textRect.center = ((displayWidth/2 , (displayHeight/2) - 100))
    gameDisplay.blit (textSurf, textRect)

    pygame.display.update()

def thingsDodged (count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things (thingX, thingY, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])
    

def car(x,y, carImage):
    gameDisplay.blit(carImage, (x,y) )

def textObjects (text,font, color = black):
    textSurface = font.render (text, True, color)
    return textSurface, textSurface.get_rect()

def msgDisplay (text, color):
    largeTxt = pygame.font.Font ('freesansbold.ttf', 115)
    textSurf, textRect = textObjects (text, largeTxt, color)
    textRect.center = ((displayWidth/2, (displayHeight/2)))
    gameDisplay.blit (textSurf, textRect)

    pygame.display.update()

def crash(score, cheater):
    time.sleep(0.10)
    gameDisplay.fill(white)
 

    scoresList, cheats = highScoreAdder(score, cheater)

    while True:
        msgDisplay('You Crashed!', (255,150,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    

        

        button("Play Again",0.8*displayWidth/4,400,195,75,darkGreen,green,gameLoop, carImage)
        button("Quit",4.9*displayWidth/8,400,150,75,darkRed,red, gameExit)
        button("View Scores",3.2*displayWidth/8,400,210,75,darkBlue,blue, highScoreViewer, scoresList, score, cheats)

        scoreDisplay(score)
    
     #time.sleep(1.5)

    

def button (msg, x, y, w, h, ic, ac, action = None, parameter = None, secParam = None, thirdParam = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print (click)

    if x+w >  mouse [0] > x and y+h > mouse [1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click [0] == 1 and action != None:
            if parameter != None:
                if secParam != None:
                    if thirdParam != None:
                        action(parameter, secParam, thirdParam)
                    elif thirdParam == None:
                        action(parameter, secParam)
                elif secParam == None:
                    action(parameter)
            elif parameter == None:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        
    smallText = pygame.font.Font('freesansbold.ttf',35)
    textSurf, textRect = textObjects(msg,smallText)
    textRect.center = ( (x +(w/2)), (y+(h/2)) + 3)
    gameDisplay.blit(textSurf, textRect)

def gameExit ():
    pygame.quit()
    quit()

def pause(paused):
    largeText = pygame.font.SysFont("freesansbold.ttf",115)
    textSurf, textRect = textObjects("Paused", largeText)
    textRect.center = ((displayWidth/2),(displayHeight/2))
    gameDisplay.blit(textSurf, textRect)

    
    #print ("Inside Function:",paused)
    while paused:
        #print ("Inside Loop:", paused)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        #gameDisplay.fill(white)
        

        button("Continue",1*displayWidth/4,400,170,75,darkGreen,green,unpause)

        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print (click)

        if 1*displayWidth/4+150 >  mouse [0] > 1*displayWidth/4 and 400+75 > mouse [1] > 400:
            if click [0] == 1:
                paused = False
        

                
        button("Quit",4.7*displayWidth/8,400,150,75,darkRed,red,gameExit)

        pygame.display.update()
        clock.tick(15)  

def unpause():
    #print ("After unpause function:", paused)
    global paused
    paused = False
    #print ("After changing paused:",paused)
    #return paused
    
    
def gameIntro ():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        textSurf, textRect = textObjects ("Car Crashers", largeText)
        textRect.center = ((displayWidth/2),(displayHeight/2))
        gameDisplay.blit (textSurf, textRect)


        button ("START", 1*displayWidth/4, 400, 150, 75, darkGreen, green, gameLoop,carImage)
        button ("QUIT", 4.7*displayWidth/8, 400, 150, 75, darkRed, red, gameExit)
        
        pygame.display.update()
        clock.tick(15)

def gameLoop(nothing):
    carPic, carInv = carSelect(carWidth)
    carImage = pygame.image.load(carPic)

    x = (displayWidth * 0.4)
    y = (displayHeight * 0.85)
    
    xChange = 0
    carSpeed = 0

    thingStartX = random.randrange(0,displayWidth)
    thingStartY = -600
    thingSpeed = 4
    thingWidth = 195
    thingHeight = 200

    thingCount = 1

    dodged = 0

    col = 0

    xChange = 0

    godMode = False

    blue = False

    normal = True
    
    cheater = False
    
    carImageTransformed = carImage


    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if keys [pygame.K_q]:
                    pygame.quit()
                    quit()

            if keys [pygame.K_p]:
                    paused = True
                    pause(paused)


            if keys [pygame.K_g]:
                    godMode = not godMode
                    if normal == False:
                        normal = True
                    if blue == False:
                        blue = True
                    if normal == True:
                        carImage = pygame.image.load(carPic)
                        carImageTransformed = pygame.image.load(carPic)
                        normal = False
                    
            if keys [pygame.K_LEFT]:
                xChange = -5
                if carImageTransformed == carImage:
                    carImageTransformed = pygame.transform.flip(carImage, True, False)

            elif keys [pygame.K_RIGHT]:
                xChange = 5
                if carImageTransformed != carImage:
                    carImageTransformed = carImage
            else:
                xChange = 0

            if keys [pygame.K_LSHIFT] or keys [pygame.K_RSHIFT]:
                xChange *= 3    

    

                ''' 
                if event.key == pygame.K_g:
                    godMode = not godMode
                    if normal == False:
                        normal = True
                    if blue == False:
                        blue = True
                    if normal == True:
                        carImage = pygame.image.load(carPic)
                        carImageTransformed = pygame.image.load(carPic)
                        normal = False
                '''
                
        x += xChange       
        
        gameDisplay.fill(white)

        things (thingStartX, thingStartY, thingWidth, thingHeight, (col,0,0))
        thingStartY += thingSpeed
        car (x,y, carImageTransformed)
        thingsDodged (dodged)

        if x > displayWidth - carWidth or x < 0:
            crash(dodged, cheater)

        if thingStartY > displayHeight:
            thingStartY = 0 - thingHeight
            thingStartX = random.randrange (0,int (displayWidth - thingWidth))
            dodged += 1
            thingSpeed += 0.5
            thingWidth += (dodged * 1.2)
            if col < 255:
                col += 15

        if y < thingStartY + thingHeight - 7:
            #print ('y crossover')

            if x > thingStartX  and x < thingStartX + thingWidth or x + carWidth > thingStartX and x + carWidth < thingStartX + thingWidth:
                #print ('x crossover')
                crash(dodged, cheater)


        if godMode == True:
            cheater = True
            if blue == True:  
                carImage = pygame.image.load(carInv)
                carImageTransformed = pygame.image.load(carInv)
                blue = False
            if y < thingStartY + thingHeight + 200:
                #print ('y cheat')
                
                #+ (thingSpeed)
                if x + carWidth + 30  >=displayWidth:
                    xChange = - (thingWidth) - 20
                    #print ('RIGHT CRASH AVOIDED')\
                #- (thingSpeed)
                elif x - 30  <= 0:
                    xChange = thingWidth + 20
                    #print ('LEFT CRASH AVOIDED')
                
                elif  x > thingStartX  and x <= thingStartX + (thingWidth/2) - carWidth or x + carWidth > thingStartX and x + carWidth <= thingStartX + (thingWidth/2) or x + (carWidth/2) > thingStartX and x + (carWidth/2) <= thingStartX + (thingWidth/2):
                    #print ('x cheat left')
                    xChange = -30 #- (thingSpeed)
                    if carImageTransformed == carImage:
                        carImageTransformed = pygame.transform.flip(carImage, True, False)
                elif x > thingStartX + (thingWidth/2)  and x <= thingStartX + thingWidth or  x + (carWidth/2) > thingStartX + (thingWidth/2)and x + (carWidth/2) <= thingStartX + thingWidth:
                    xChange = 30 #+ (thingSpeed)
                    
                    #print ('Car Left Position:',x)
                    #print ('Car Width:',carWidth)
                    #print ('Car Right Position:',x+carWidth)
                    #print ('Thing Left Position:',thingStartX)
                    #print ('Thing Width',thingWidth)
                    #print ('Thing Right Position:',thingStartX+thingWidth)
                    #print ('Thing Half-way Position:',(thingStartX + thingWidth)/2)
                    
                    #print ('x cheat right')
                    if carImageTransformed != carImage:
                        carImageTransformed = carImage

                else:
                    xChange = 0
                
            
        pygame.display.update()
        clock.tick(60)

#Starts the game        
gameIntro()
#gameLoop(carImage)
pygame.quit()
quit()

    
