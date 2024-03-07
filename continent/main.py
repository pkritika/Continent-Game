import turtle
import pandas


screen = turtle.Screen()
screen.setup(width=1100, height=1100)
screen.title("Continent Game")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("data.csv")
all_continent = data.continent.to_list()
guessed_continents= []





# def get_mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
while len(guessed_continents)<7:
    answer_continent = str(screen.textinput(title=f"{len(guessed_continents)}/07 the Continents",
                                            prompt = "What's another state's name?")).title()
    print(answer_continent)

    if answer_continent in all_continent:
        guessed_continents.append(answer_continent)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        continent_data = data[data.continent == answer_continent]
        t.goto(int(continent_data.x), int(continent_data.y))
        t.write(answer_continent)





screen.exitonclick()







