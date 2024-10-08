import turtle as t
import math

screen = t.Screen()
# screen.bgcolor("green")
screen.title("Projectile Motion Simulation")


scale = 1.5

projectile = t.Turtle()
projectile.shape("circle")
projectile.color("blue")
projectile.penup()
projectile.goto(-300, -100)


def simulate_projectile(v0, angle, g=9.8):
    angle_rad = math.radians(angle)

    # Time of FLight
    T = (2 * v0 * math.sin(angle_rad)) / g
    
    # time chanfges in interval
    dt = 0.09 
    
    t = 0
    while t <= T:
        x = (v0 * math.cos(angle_rad) * t )* scale
        y = (v0 * math.sin(angle_rad) * t - 0.5 * g * t**2) * scale
        
        # Set the projectile new postiton
        projectile.goto(-300 + x , -100+ y )
        
        # Increment the time by the small interval
        t += dt
    
    # projectile.hideturtle()






# Set initial conditions
u0 = 70  # m/s
theta = 70  # degrees
g = 9.8

R = ((u0 ** 2) * math.sin(math.radians(2 * theta)) / g) * scale
H = ((u0 ** 2) * (math.sin(math.radians(theta)) ** 2) / (2 * g) ) * scale

# Set up t speed
projectile.speed(1)
projectile.penup()
# projectile.goto(0, 0)
projectile.pendown()





ball1 = t.Turtle()
ball2 = t.Turtle()

ball1.penup()
ball2.penup()
ball1.goto(-300, -100)
ball2.goto(-300, -100)
ball1.pendown()
ball2.pendown()
ball1.speed(1)
ball2.speed(1)

ball1.forward(R)
ball2.forward(R/2)

ball2.left(90)
ball2.forward(H)


# Simulate the projectile
simulate_projectile(u0, theta)

# Keep the window open until closed by the user
screen.exitonclick()
