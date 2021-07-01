from turtle import *
hideturtle()
color('blue')

def draw_snowflake_side(size, levels):
    if levels == 0:
        forward(size)
        return
    size /= 3.0
    draw_snowflake_side(size, levels - 1)
    left(60)
    draw_snowflake_side(size, levels - 1)
    right(120)
    draw_snowflake_side(size, levels - 1)
    left(60)
    draw_snowflake_side(size, levels - 1)

def draw_snowflakes(size, levels, sides):
    for i in range(sides):
        draw_snowflake_side(size, levels)
        right(360 / sides)

if __name__ == '__main__':  
    speed(0)
    size = 400.0
    levels = 4
    sides = 3
    
    penup()
    goto(-size / 2.0, size / 3.0)
    pendown()

    draw_snowflakes(size, levels, sides)
    
    mainloop()
