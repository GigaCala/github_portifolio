import turtle
t= turtle.Pen()


t.begin_fill()
t.color('Blue')
t.forward(90)
t.left(90)
t.forward(30)
t.left(30)
t.forward(30)
t.left(60)
t.forward(76)
t.left(90)
t.forward(56)
t.right(90)
t.forward(55)
t.right(90)
t.forward(20)
t.right(90)
t.forward(55)
t.right(90)
t.forward(20)
t.up()
t.forward(1)
t.right(90)
t.forward(1)
t.down()
t.end_fill()

t.begin_fill()
t.color('red')
t.circle(15)
t.end_fill()

t.right(180)
t.up()
t.forward(55)
t.right(90)
t.forward(15)
t.down()

t.begin_fill()
t.color('red')
t.circle(15)
t.end_fill()

t.up()
t.right(180)
t.backward(150)
t.right(90)
t.backward(150)

t.down()


while True:
    t.begin_fill()
    t.color('green')
    t.circle(20)
    t.forward(60)
    t.right(30)
    t.forward(60)
    t.left(60)
    t.end_fill()



    
