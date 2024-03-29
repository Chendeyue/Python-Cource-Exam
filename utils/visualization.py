#可视化
import turtle as t
import numpy as np
from PIL import Image
#input:数组，4行5列，每行依次对应右、上、左、下方向，任意一行的每列依次为(0/1)：道路是否存在/角度，是否调头，是否左转，是否直行，是否右转

def DrawRoad(angle):
    t.tracer(False)
    t.penup()
    t.goto(0, 0)
    t.seth(angle)
    t.fd(width/2)
    t.right(90)
    t.fd(width/2)
    t.left(90)
    t.pd()
    t.fd(length)
    t.left(90)
    t.penup()
    t.fd(width)
    t.left(90)
    t.pd()
    t.fd(length)
    t.penup()

def Drawline(angle):
    t.tracer(False)
    t.penup()
    t.goto(0, 0)
    t.seth(angle)
    t.fd(width/2)
    t.right(90)
    t.fd(width/2)
    t.left(180)
    t.pd()
    t.fd(width)
    t.penup()

#右转
def GoRight(a,b):
#依据路口设置颜色
    if a == 0:
      t.color("white","red")
    elif a == 1:
      t.color("white","yellow")
    elif a == 2:
      t.color("white","blue")
    elif a == 3:
      t.color("white","green")
    t.pensize(2)
    # 设置起点为矩形边框左上角
    t.penup()
    t.forward(118)
    t.lt(90)
    t.fd(b/6)
    # 绘制箭头
    t.pendown()
    t.begin_fill()
    t.rt(90)
    t.forward(15)
    t.lt(90)
    t.forward(30)
    t.rt(90)
    t.forward(15)
    t.rt(225)
    t.forward(33)
    t.rt(270)
    t.forward(33)
    t.rt(225)
    t.forward(18)
    t.rt(90)
    t.forward(30)
    t.end_fill()
    # 返回矩形左上角
    t.penup()
    t.fd(b/5)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    #t.exitonclick()
#直行
def GoStraight(a,b):
#依据路口设置颜色
    if a == 0:
      t.color("white","red")
    elif a == 1:
      t.color("white","yellow")
    elif a == 2:
      t.color("white","blue")
    elif a == 3:
      t.color("white","green")
# 设置起点为矩形边框左上角
    t.penup()
    t.forward(140)
    t.lt(90)
    t.fd(b/3)
    # 绘制箭头
    t.pendown()
    t.begin_fill()
    t.lt(90)
    t.pensize(2)
    t.rt(90)
    t.forward(15)
    t.lt(90)
    t.forward(30)
    t.rt(90)
    t.forward(15)
    t.rt(225)
    t.forward(33)
    t.rt(270)
    t.forward(33)
    t.rt(225)
    t.forward(18)
    t.rt(90)
    t.forward(30)
    t.end_fill()
# 返回矩形左上角
    t.penup()
    t.rt(90)
    t.fd(b/3)
    t.rt(90)
    t.fd(150)
    t.rt(90)
#左转
def GoLeft(a,b):
# 依据路口设置颜色
    if a == 0:
        t.color("white","red")
    elif a == 1:
        t.color("white","yellow")
    elif a == 2:
        t.color("white","blue")
    elif a == 3:
        t.color("white","green")
    t.pensize(2)
    # 设置起点为矩形边框左上角
    t.penup()
    t.forward(134)
    t.lt(90)
    t.fd(4*b/5)
    # 绘制箭头
    t.pendown()
    t.begin_fill()
    t.lt(90)
    t.forward(15)
    t.lt(90)
    t.forward(30)
    t.rt(90)
    t.forward(15)
    t.rt(225)
    t.forward(33)
    t.rt(270)
    t.forward(33)
    t.rt(225)
    t.forward(18)
    t.rt(90)
    t.forward(30)
    t.end_fill()
    # 返回矩形左上角
    t.penup()
    t.lt(180)
    t.fd(4*b/5)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    #t.exitonclick()
#掉头
def GoBack(a,b):
# 依据路口设置颜色
    if a == 0:
        t.color("white","red")
    elif a == 1:
        t.color("white","yellow")
    elif a == 2:
        t.color("white","blue")
    elif a == 3:
        t.color("white","green")
    t.pensize(2)
#设置起点为矩形边框左上角
    t.penup()
    t.forward(142)
    t.lt(90)
    t.fd(b/6)
#绘制箭头
    t.pendown()
    t.begin_fill()
    t.lt(90)
    t.fd(18)
    t.rt(180)
    t.circle(15, -180)
    t.rt(180)
    t.fd(18)
    t.lt(90)
    t.fd(6)
    t.rt(135)
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.rt(135)
    t.fd(8)
    t.lt(90)
    t.fd(18)
    t.circle(8, 180)
    t.fd(18)
    t.rt(90)
    t.fd(7)
    t.end_fill()
#返回矩形左上角
    t.penup()
    t.fd(b/3)
    t.rt(90)
    t.fd(142)
    t.rt(90)


if __name__ == '__main__':
    test = [[0, 1, 1, 1, 1], [-1, 1, 1, 1, 1], [180, 1, 1, 1, 1], [270, 1, 1, 1, 1]]
    n = np.array(test)
    window = t.Screen()  # 获得一个窗口句柄
    window.bgcolor("darkorange")  # 把背景设为蓝色
    # 画布
    t.setup(1000, 1000)
    t.tracer(False)
    # 画笔
    t.pensize(5)
    t.color("black")
    # 画路口
    width = 300
    length = 500

    t.tracer(False)
    t.penup()
    ang = 0
    m = 0
    for i in range(4):
        if n[i][0] >= 0:
            ang += n[i][0] - 90 * i
            m += 1
    MeanAng = int(ang / m)
    # MeanAng = 60
    CurAug = MeanAng
    for i in range(4):
        if n[i][0] >= 0:
            DrawRoad(CurAug)
        else:
            Drawline(CurAug)
        CurAug += 90
    #绘制每条道路的转向标志
    t.penup()
    t.goto(0, 0)
    t.seth(MeanAng)
    for i in range(4):
        k=0
        if n[i][0]>=0:
            for j in range(1,5):
                if n[i][j]==1:
                    k+=1
            SignPosW=width/k
            t.penup()
            t.fd(width/2)
            t.right(90)
            t.fd(width/2)
            t.left(90)
            if n[i][1]==1:
                GoBack(i,SignPosW)
                t.penup()
                t.fd(SignPosW)
                t.right(90)
            if n[i][2]==1:
                GoLeft(i,SignPosW)
                t.penup()
                t.fd(SignPosW)
                t.right(90)
            if n[i][3]==1:
                GoStraight(i,SignPosW)
                t.penup()
                t.fd(SignPosW)
                t.right(90)
            if n[i][4]==1:
                GoRight(i,SignPosW)
                t.penup()
                t.fd(SignPosW)
                t.right(90)
        t.penup()
        t.goto(0, 0)
        t.seth(MeanAng+90*i+90)

    # t.exitonclick()
    ts = t.getscreen()

    ts.getcanvas().postscript(file="duck.eps")

    im = Image.open("duck.eps")
    im.save("pic.png")




