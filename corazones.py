import turtle
import random

# Screen configuration
window = turtle.Screen()
window.title("Instant Hearts on Click!")
window.bgcolor("white")
window.setup(width=800, height=600)

# Turn off automatic animation for instant drawing
window.tracer(0)

# List of bright colors for the hearts
colors = ["#FF3366", "#FF3399", "#FF0055", "#FF66B2", "#E60073", "#FF1A75", "#FF0000"]

def create_heart(x, y):
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.speed(0)
    heart.penup()
    
    # Random scale factor to vary sizes
    scale = random.uniform(0.6, 1.5)
    
    # Adjust position based on scale to center it on the click
    heart.goto(x, y - (15 * scale))
    heart.pendown()
    
    # Choose a random color and start filling
    random_color = random.choice(colors)
    heart.color(random_color)
    heart.begin_fill()
    
    # Draw the heart shape (multiplied by scale)
    heart.left(140)
    heart.forward(40 * scale)
    
    # Left curve
    for _ in range(200):
        heart.right(1)
        heart.forward(0.3 * scale)
        
    heart.left(120)
    
    # Right curve
    for _ in range(200):
        heart.right(1)
        heart.forward(0.3 * scale)
        
    heart.forward(40 * scale)
    heart.end_fill()
    window.update()

# Listen for mouse clicks on the screen
window.onclick(create_heart)
window.listen()

# Initial screen update
window.update()
window.mainloop()
