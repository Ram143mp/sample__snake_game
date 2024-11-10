
Skip to content
All gists
Back to GitHub
Sign in
Sign up

Instantly share code, notes, and snippets.
@wynand1004
wynand1004/snake_game.py
Created September 2, 2018 08:56

Code
Revisions 1
Stars 107
Forks 79
Clone this repository at &lt;script src=&quot;https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900.js&quot;&gt;&lt;/script&gt;
A Simple Snake Game made in Python 3
snake_game.py
# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
@TinyHaitch
TinyHaitch commented Aug 12, 2022

nice game
@Olexandr-Andriyenko
Olexandr-Andriyenko commented Sep 9, 2022

Nice game, you can create classes for the snake body, scoreboard, food and maybe wall. Then the code will be more structured :)
@SohamRoy20Gaming
SohamRoy20Gaming commented Jan 17, 2023

 /bin/python3 "/home/devil/Code/Python/Turtle/Snake Game/snake_game.py"
Traceback (most recent call last):
  File "/home/devil/Code/Python/Turtle/Snake Game/snake_game.py", line 4, in <module>
    import turtle
  File "/usr/lib/python3.10/turtle.py", line 107, in <module>
    import tkinter as TK
ModuleNotFoundError: No module named 'tkinter'

@wynand1004
Author
wynand1004 commented Jan 20, 2023 via email
Heya. Probably you need to install tkinter for ubuntu. To do so, go to the
terminal and type: sudo apt-get install python3-tk


Here is a link to my free Intro to Python e-book - you may find  it
helpful:
https://drive.google.com/file/d/1ajYJZLGUaVmNbuG98LnRfHMTzvnZx9el/view?usp=share_link

Keep on coding!

TokyoEdtech
…
@sweir66
sweir66 commented Feb 9, 2023

how would one add a border around the playable area, as i would like to enlarge the game screen but a border around the playable are would make it easier to play
@wynand1004
Author
wynand1004 commented Feb 9, 2023 via email
You can draw lines like so:

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
…
@Angus-Developer
Angus-Developer commented Apr 14, 2023

How to play?
@wynand1004
Author
wynand1004 commented Apr 14, 2023 via email
Hiya,

Download the python file. Open it in  your preferred IDE, and run the
program. Use the arrows to move the snake around.
…
@sajjad-salam
sajjad-salam commented Jun 2, 2023

module 'turtle' has no attribute 'Screen'
@zohaibpy7
zohaibpy7 commented Jun 8, 2023

how to fix it when the snake hits the borders the game overs can you provide me some code for that?
@bruno889972
bruno889972 commented Jul 13, 2023

foto do perfil
O que você consiga fazer

Eu sou um grande modelo de linguagem, também conhecido como IA conversacional ou chatbot treinado para ser informativo e abrangente. Sou treinado em uma enorme quantidade de dados de texto e sou capaz de comunicar e gerar texto semelhante ao humano em resposta a uma ampla gama de prompts e perguntas. Por exemplo, posso fornecer resumos de tópicos factuais ou criar histórias.

Aqui estão algumas coisas que posso fazer:

Vou tentar o meu melhor para seguir suas instruções e completar seus pedidos de forma atenciosa.
Usarei meu conhecimento para responder às suas perguntas de forma abrangente e informativa, mesmo que sejam abertas, desafiadoras ou estranhas.
Vou gerar diferentes formatos de texto criativo de conteúdo de texto, como poemas, código, scripts, peças musicais, e-mail, cartas, etc. Vou tentar o meu melhor para cumprir todos os seus requisitos.
Ainda estou em desenvolvimento e estou sempre aprendendo coisas novas. Estou animado para ver o que posso fazer no futuro!

foto do perfil
Gerar um código de aplicativo

Claro, eu posso te ajudar com isso. O que você gostaria de fazer? Você pode me dar mais detalhes sobre o seu aplicativo?

foto do perfil
Gerar um código para aplicativo de jogo da cobrinha

Claro, aqui está um código para um aplicativo de jogo da cobrinha em Python:

Python
import pygame
Define as dimensões da tela

WIDTH = 400
HEIGHT = 400
Cria uma janela pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))
Define as cores

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
Cria a cobra

snake = pygame.Rect(10, 10, 10, 10)
snake_color = RED
Cria a comida

food = pygame.Rect(300, 300, 10, 10)
food_color = WHITE
Inicia o contador de pontos

score = 0
Inicia o loop do jogo

running = True
while running:

# Limpa a tela
screen.fill(BLACK)

# Desenha a cobra
pygame.draw.rect(screen, snake_color, snake)

# Desenha a comida
pygame.draw.rect(screen, food_color, food)

# Checa se a cobra comeu a comida
if snake.colliderect(food):
    score += 1
    food.x = random.randint(10, WIDTH - 10)
    food.y = random.randint(10, HEIGHT - 10)

# Checa se a cobra colidiu com a si mesma ou com as bordas da tela
for i in range(1, len(snake)):
    if snake[0].colliderect(snake[i]):
        running = False
        break

if snake.x < 0 or snake.x > WIDTH or snake.y < 0 or snake.y > HEIGHT:
    running = False
    break

# Atualiza a posição da cobra
snake[0].x += snake_direction[0]
snake[0].y += snake_direction[1]

# Remove o último bloco da cobra
snake.pop()

# Adiciona um novo bloco na cabeça da cobra
snake.insert(0, pygame.Rect(snake[0].x, snake[0].y, 10, 10))

# Atualiza a tela
pygame.display.update()

# Checa se o usuário pressionou o botão de fechar
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

Finaliza o pygame

pygame.quit()
@khangaup
khangaup commented Jul 29, 2023
Simple Snake Game in Python 3 for Beginners

import turtle
import time
import random

delay = 0.1
Score

score = 0
high_score = 0
Set up the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates
Snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"
Snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []
Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))
Functions

def go_up():
if head.direction != "down":
head.direction = "up"

def go_down():
if head.direction != "up":
head.direction = "down"

def go_left():
if head.direction != "right":
head.direction = "left"

def go_right():
if head.direction != "left":
head.direction = "right"

def move():
if head.direction == "up"and head.direction != "down":
y = head.ycor()
head.sety(y + 20)

if head.direction == "down" and head.direction != "up":
    y = head.ycor()
    head.sety(y - 20)

if head.direction == "left" and head.direction != "right":
    x = head.xcor()
    head.setx(x - 20)

if head.direction == "right" and head.direction != "left":
    x = head.xcor()
    head.setx(x + 20)

Keyboard bindings

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
Main game loop

while True:
wn.update()

# Check for a collision with the border
if head.xcor()>290:
    time.sleep(0.1)
    head.goto(-290,y)
    # head.direction = "stop" 
if head.xcor()<-290:
    time.sleep(0.1)
    head.goto(290,y)
if head.ycor()>290: 
    time.sleep(0.1)
    head.goto(x,-290)
if head.ycor()<-290:
    time.sleep(0.1)
    head.goto(x,290)

    # Hide the segments
    for segment in segments:
         segment.goto(1000, 1000)
    
    # Clear the segments list
    # segments.clear()

    # Reset the score
    # score = 0

    # Reset the delay
    delay = 0.1

    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


# Check for a collision with the food
if head.distance(food) < 20:
    # Move the food to a random spot
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x,y)

    # Add a segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("red")
    new_segment.penup()
    segments.append(new_segment)

    # Shorten the delay
    delay -= 0.001

    # Increase the score
    score += 10

    if score > high_score:
        high_score = score
    
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

# Move the end segments first in reverse order
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

# Move segment 0 to where the head is
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)

move()    

# Check for head collision with the body segments
for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
    
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1
    
        # Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

time.sleep(delay)

wn.mainloop()
@Aroulis8
Aroulis8 commented Aug 21, 2023

Great i liked it
@wynand1004
Author
wynand1004 commented Aug 21, 2023 via email
Thanks - glad to hear it!
…
@Aroulis8
Aroulis8 commented Sep 11, 2023

😄
@jarvissilva937
jarvissilva937 commented Nov 1, 2023

Great code, here is is tutorial to make fruit ninja game in python
@futureneurologist
futureneurologist commented Nov 3, 2023

Traceback (most recent call last):
File "C:/Users/INDIA/AppData/Local/Programs/Python/Python311/Lovely game.py", line 90, in
wn.update()
File "C:\Users\INDIA\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1304, in update
t._update_data()
File "C:\Users\INDIA\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
self.screen._incrementudc()
File "C:\Users\INDIA\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
raise Terminator
turtle.Terminator
"What to do with this now??"
@wynand1004
Author
wynand1004 commented Nov 5, 2023 via email
You can just ignore that. It happens when you close the window. There is a
way to stop it. I have a video on my channel about this.
…
@futureneurologist
futureneurologist commented Nov 5, 2023 via email
Hello sir,
Thank you for replying to my email,
But the game is not starting also 😕
The window appears and when we click or try to start the game it is not
responding.
So I would like to know how can I solve it.
Thank you so much for your support.
I hope to hear from you soon.



On Sun, 5 Nov 2023, 6:50 am Christian Thompson, ***@***.***>
wrote:
…
@wynand1004
Author
wynand1004 commented Nov 5, 2023 via email
Ahh gotcha. Can you share the code?

On Sun, Nov 5, 2023, 12:17 futureneurologist ***@***.***>
wrote:
…
@ShantanuPandeyGit
ShantanuPandeyGit commented Dec 8, 2023 •

Getting below error while running in Ubuntu terminal

Traceback (most recent call last):
File "/home/ubuntu/python/snake.py", line 12, in
wn = turtle.Screen()
File "/usr/lib/python3.10/turtle.py", line 3664, in Screen
Turtle._screen = _Screen()
File "/usr/lib/python3.10/turtle.py", line 3680, in init
_Screen._root = self._root = _Root()
File "/usr/lib/python3.10/turtle.py", line 435, in init
TK.Tk.init(self)
File "/usr/lib/python3.10/tkinter/init.py", line 2299, in init
self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
ubuntu@ip-172-31-22-55:~/python$ nano snake.py
@wynand1004
Author
wynand1004 commented Dec 8, 2023 via email
Are you running it remotely? If so there may be no graphics just the
terminal.
…
@NaxUnknown
NaxUnknown commented Mar 16, 2024

        Thank you for the code! The snake game was amazing.

    I think you're commenting to the wrong person, just saying

Wdym it works
@AshfaqueAhmed123
AshfaqueAhmed123 commented Apr 7, 2024

arrow keys are not working in ubuntu how to play the game
@wynand1004
Author
wynand1004 commented Apr 7, 2024 via email
The game uses w, a, s, d. Make sure caps lock is off. Also make sure you
click inside the window after running so it has focus.
…
@misakik4
misakik4 commented Jun 22, 2024

its amazing game nice! I'm still learning how to code python thanks for sharing this!
@Raghav2013R
Raghav2013R commented Jul 28, 2024

    Hey! I was wondering is there a way I can change the background from green to checkers?

You can
@naqiiabbas
naqiiabbas commented Aug 9, 2024

     /bin/python3 "/home/devil/Code/Python/Turtle/Snake Game/snake_game.py"
    Traceback (most recent call last):
      File "/home/devil/Code/Python/Turtle/Snake Game/snake_game.py", line 4, in <module>
        import turtle
      File "/usr/lib/python3.10/turtle.py", line 107, in <module>
        import tkinter as TK
    ModuleNotFoundError: No module named 'tkinter'

go to terminal and type pip install tkinter, i hope it will work
@W1zarDddD
W1zarDddD commented Aug 14, 2024 •

Everything is thought out very cool. I am just learning to write games on Fiton and not only. In the future, I would like to create something with online games. I always have holandia kasyna as an example, I read about it https://pl.bestcasinos-pl.com/holandia-kasyna/ here. This would already be an achievement for me. But I can’t imagine how much more effort I will need to spend on this.
@beResonant
beResonant commented Oct 10, 2024

    arrow keys are not working in ubuntu how to play the game

Change each of the letters for up, down, etc in the "onkeypress" statements to correspond to the literal words "Up" "Down" "Left" and "Right" in place of the 'wsad' options, and you'll get keyboard arrow functionality.
to join this conversation on GitHub. Already have an account? Sign in to comment
Footer
© 2024 GitHub, Inc.
Footer navigation

    Terms
    Privacy
    Security
    Status
    Docs
    Contact

