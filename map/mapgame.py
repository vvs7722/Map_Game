from turtle import Turtle,Screen
import turtle
import pandas
sc=Screen()
sc.title("India map")
sc.setup(800,800)
img="India_map.gif"
sc.addshape(img)
turtle.shape(img)
data=pandas.read_csv("map.csv")
state=data["state"].to_list()
x=data["x"].to_list()
y=data["y"].to_list()
x1=data["x1"].to_list()
y1=data["y1"].to_list()
#print(state,x,y,x1,y1)
count=0
con=True
c=[]
tim=Turtle()
tim.penup()
tim.color("black")
def go(tim,a,gus):
    tim.penup()
    tim.goto(int(a.x),int(a.y))
    tim.pd()
    tim.goto(int(a.x1),int(a.y1))
    tim.write(gus)
    tim.penup()
def reveal(state,data):
    for i in range (len(state)):
        gus=state[i]
        a=data[data.state==gus]
        go(tim,a,gus)

while con:
    gus=turtle.textinput("state name","enter")
    if gus in state:
        a=data[data.state==gus]
        #print(a.x)
        #num=state.index(gus)
        go(tim,a,gus)
        count+=1
        
    if gus=="reveal":
        reveal(state,data)
        
    if gus=="exit" or count==36:
        con=False
#turtle.mainloop()
turtle.exitonclick()

# def get_mouse_click_coo(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coo)
# turtle.mainloop() 
