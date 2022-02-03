from turtle import *
from random import randint

setup_run = False
w = 0


def auto(color, y_offset, rando, first_run_finish):
	penup()
	if (first_run_finish == False):
		setx(600)
	else:
		forward(rando)
	print(rando)
	fillcolor(color)
	sety(y_offset)
	pendown()
	left(90)
	forward(50)
	left(90)
	forward(50)
	right(45)
	forward(50)
	left(45)
	forward(50)
	left(45)
	forward(50)
	right(45)
	forward(50)
	left(90)
	forward(50)
	left(90)
	forward(220.71)
	penup()
	x = (xcor() - 30)
	y = (ycor() - 20)
	setx(x)
	sety(y)
	# setpos(-30, -20)
	pendown()
	begin_fill()
	circle(20)
	end_fill()
	penup()
	x = (xcor() - 160)
	y = (ycor())
	setx(x)
	sety(y)
	# setpos(-190,-20)
	pendown()
	begin_fill()
	circle(20)
	end_fill()
	penup()


resizemode("auto")
setup(width=.99, height=.99, startx=0, starty=0)
while (w <= 10):
	print("GO")
	auto(color="green", y_offset=0, rando=(randint(0, 100)),first_run_finish=setup_run)
	
	auto(color="red", y_offset=100, rando=(randint(0, 100)),first_run_finish=setup_run)
	clear()
	setup_run = True
	w = w + 1
	

print("END")
input()
