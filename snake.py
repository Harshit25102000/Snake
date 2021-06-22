



"""we'll decide height , width of game , position and velocity of snake in x and y
also on touching boundary i.e. when position equals to width then gameover and also to update scores
and increasse the size of snake """

#code by Harshit Singh

#import and initilize all functions of modules
import pygame
import random
import os
pygame.mixer.init()   #music library
pygame.init()


#colors define
#every color has a rgb value of 3 numbers as every color consists of red , green , blue
white = (255,255,255)
Black = [0,0,0]
Red = [255,0,0]
Green = [0,255,0]
Blue = [0,0,255]

#window size variables
screen_width = 900
screen_height = 600

#background image
bgimg = pygame.image.load("snkimg.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height))
intro = pygame.image.load("intro.png")
intro = pygame.transform.scale(intro , (screen_width, screen_height))
end = pygame.image.load("end.png")
end = pygame.transform.scale(end , (screen_width, screen_height))



#creating window
gameWindow= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes by Harshit Singh")
pygame.display.update()    #updates all display settings




#function for displaying score
font = pygame.font.SysFont(None,55)  #using system font , none as no name i.e. system font else font name then size
def screen_score(text, color, x, y):
    score_text = font.render(text, True , color)
    gameWindow.blit(score_text, [x,y])  #it will update

def draw_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color, [x,y, snake_size, snake_size])


#welcome screen
clock = pygame.time.Clock()
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(intro, (0,0))
        #gameWindow.fill((233,210,229))
        #screen_score("Welcome to Snakes by Harshit", Black, 150, 250)
        #screen_score("Press Space Bar To Play", Black, 220, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    gameloop()

        pygame.display.update()
        clock.tick(60)


#Game Loop
def gameloop():

    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 200  # initial position of snake in x and y co-ord
    snake_y = 50
    snake_size = 15  # size of snake
    fps = 30
    clock = pygame.time.Clock()
    velocity_x = 0
    velocity = 5
    velocity_y = 0
    score = 0

    food_x = random.randint(20,  screen_width )  # food x me 0 se lekar screen width tk me se kam ek random value hogi but fir corner me jata to 20 se quarter tk
    food_y = random.randint(20, screen_height /2)

    snake_list = []
    snake_length = 1

    pygame.mixer.music.load('back.mp3')
    pygame.mixer.music.play()

    # managing highscore
    #first check  if hiscore file exists or not
    if (not os.path.exists("hiscore.txt")):  #if file don't exist then create one
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:   #game over true hone pe screen white filled and print
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
                gameWindow.blit(end, (0, 0))
            #gameWindow.fill(white)
            screen_score(str(score), Black, 600, 380)
            screen_score(str(hiscore), Black ,600 , 440)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                #snake movements
                if event.type == pygame.KEYDOWN:   #positive inc. x value on right keystroke so that snake can move right on pressing right
                    if event.key == pygame.K_RIGHT:    #for simple movement x = x+ 70 so on right stroke shit hoga but for continuous movement loop me velocity x kuch kardo  vel y 0 kardo
                        velocity_x = velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -velocity
                        velocity_y =  0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -velocity
                        velocity_x =  0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y =  velocity
                        velocity_x =  0

                     #to activate cheat code and increasing score by pressing c
                     #if event.key == pygame.K_c:
                      #score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            #to decide score
            if abs(snake_x - food_x) < 14 and abs(snake_y - food_y) < 14:  #we used absolute function so if passes even close by then it will be a win
               # pygame.mixer.music.load('beep.mp3')
                #pygame.mixer.music.play()

                score += 10


                food_x = random.randint(20, screen_width)
                food_y = random.randint(20, screen_height/2)
                snake_length += 5

                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))

            #drawing snake head on that time co ordinates4
            #pygame.draw.rect(gameWindow, White, [snake_x, snake_y, snake_size, snake_size]) #in game window, color, x and y position and length and breadth
            pygame.draw.circle(gameWindow, Red, (food_x, food_y), 8)  #food drawing screen, color ,co ord, radius , thickness(optional)
            screen_score("Score:" + str(score) + " High Score:" + str(hiscore), Blue, 5, 5)  # calling function to print score


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            """ek empty snake list banayi usme or empty head , start k liye initial me random x and y daale wo snake list me dala fir game shurur , har movement k sath x and y 
            increase hoga wo head me jaata rhega or wo list me jayega, snake list me kyi x and y ki list jayega as one list for example [ [x1,y1],[ x2,y2]] to continuously plot hota jayega
             par humne condition laga di ki agar snake length se bada hua to initial element hata do ,to starting me snake length one thi to ek se zada co ordinate nhi le sakta 
             or jase hi food  khayega to snake length increasse ho jayegi to ab 1+5 i.e. 6 se zada nhi co ord lega ,ye co ord moving co ord ha to continuous hai or in cont co ord.
             pe draw hoga to continuous line i.e. snake banega"""

            #if snake eat himself
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            """logic ye tha ki snake ka head co ord baki snake k kisi co ord se match hua to over so snake list me except last element [:-1] means except last element, 
                                      agar head i.e. head ka co ord hai snake list me to over but why not last elemnt because last elemtn of list is head only to head to head se match hoga hi  """


            # if snake touches the boundaries then game over
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()


            draw_snake(gameWindow, white , snake_list, snake_size)
        pygame.display.update() #use this at last to update all the things on display
        clock.tick(fps) #one tick i.e. 1 sec me 30 baar chalega as fps = 30


    pygame.quit()
    quit()
welcome()



