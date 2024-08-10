import turtle as t
import math

class ProjectileSimulator:
    def __init__(self, v0, angle, g=9.8, scale=1.5, time_passage = 0.1):
        # Initial conditions
        self.v0 = v0
        self.angle = angle
        self.g = g
        self.scale = scale
        self.time_passage = time_passage

        # Convert angle to radians
        self.angle_rad = math.radians(angle)
        
        # Time of flight
        self.T = (2 * v0 * math.sin(self.angle_rad)) / g

        # Create turtle screen
        self.screen = t.Screen()
        self.screen.title("Projectile Motion Simulation")

        # Create turtle for projectile
        self.projectile = t.Turtle()
        self.projectile.shape("circle")
        self.projectile.color("blue")
        self.projectile.penup()
        self.projectile.goto(-300, -100)
        self.projectile.pendown()
        self.projectile.speed(1)

        # Create turtle for reference points
        self.ball1 = t.Turtle()
        self.ball2 = t.Turtle()
        self.ball1.penup()
        self.ball2.penup()
        self.ball1.goto(-300, -100)
        self.ball2.goto(-300, -100)
        self.ball1.pendown()
        self.ball2.pendown()
        self.ball1.speed(1)
        self.ball2.speed(1)

    def calculate_range_and_height(self):
        R = ((self.v0 ** 2) * math.sin(math.radians(2 * self.angle)) / self.g) * self.scale
        H = ((self.v0 ** 2) * (math.sin(math.radians(self.angle)) ** 2) / (2 * self.g)) * self.scale
        return R, H

    def simulate_projectile(self):
        dt = self.time_passage # Time step
        t = 0

        while t <= self.T:
            x = (self.v0 * math.cos(self.angle_rad) * t) * self.scale
            y = (self.v0 * math.sin(self.angle_rad) * t - 0.5 * self.g * t ** 2) * self.scale

            # Set the projectile's new position
            self.projectile.goto(-300 + x, -100 + y)

            # Increment the time by the small interval
            t += dt

    def draw_reference_points(self):
        R, H = self.calculate_range_and_height()
        self.ball1.forward(R)
        self.ball2.forward(R / 2)
        self.ball2.left(90)
        self.ball2.forward(H)

    def run_simulation(self):
        # Draw the reference points for range and height
        self.draw_reference_points()

        # Simulate the projectile motion
        self.simulate_projectile()

        # Keep the window open until closed by the user
        self.screen.exitonclick()


# simulator = ProjectileSimulator(v0=80, angle=70)
# simulator.run_simulation()