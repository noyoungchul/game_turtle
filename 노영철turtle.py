import turtle
import time

screen = turtle.Screen()
screen.title("거북이 따라다니기 게임")
screen.setup(600, 600)
screen.bgcolor("lightblue")

# 플레이어 거북이
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(200, 0) #200으로 위치 이동

# 추적자 거북이
chaser = turtle.Turtle()
chaser.shape("turtle")
chaser.color("red")
chaser.penup()
chaser.goto(-300, 0) #-300으로 위치 이동

# 추가항목! 추적자가 플레이어 쪽으로 이동하며 흔적 남김 
chaser.pendown() 
chaser.pensize(2) 
chaser.color("red")

# 플레이어 이동 함수
def go_up():
    y = player.ycor()
    if y < 280:
        player.sety(y + 20)
def go_down():
    y = player.ycor()
    if y > -280:
        player.sety(y - 20)
def go_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)
def go_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

def is_collision(t1, t2):
    return t1.distance(t2) < 20

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    
    # 추적자가 플레이어 쪽으로 이동
    chaser.setheading(chaser.towards(player))
    chaser.forward(15)
    
    if is_collision(player, chaser):
        game_over = True

screen.textinput("게임 종료", "추적자에게 잡혔습니다! 종료하려면 아무 키나 누르세요.")
screen.bye()