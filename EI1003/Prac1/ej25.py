from turtle import Screen, Turtle
x=int(input("Dame un valor para X: "))
pantalla = Screen()
pantalla.setup (425,225)
pantalla.screensize (x,x)
tortuga=Turtle()
tortuga.goto(x,x)
tortuga.dot(8)
tortuga.goto(x,x-48)
tortuga.circle(50)

pantalla.exitonclick()
