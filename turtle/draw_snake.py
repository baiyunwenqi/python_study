import turtle
# 小乌龟移动的轨迹绘制成了曲线

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)    #rad 爬行的半径 angle圆弧的角度值
        turtle.circle(-rad, angle)   #rad为负 右侧爬行
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)                  # forward 直线爬行
    turtle.circle(neckrad + 1, 180)  # neckrad 小蛇的颈部半径  
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(1300, 800, 0, 0)  # 设置绘图窗口的大小，左边两个为窗口的宽高，右边两个参数为坐标原点
    pythonsize = 40
    turtle.pensize(pythonsize)
    turtle.pencolor("blue") 
    turtle.seth(-40) #启动时运行的方向
    drawSnake(40, 80, 3, pythonsize / 2)


main()
