import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(t, order, length):
    for _ in range(3):
        koch_curve(t, order, length)
        t.right(120)

def main():
    window = turtle.Screen() 
    window.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.color('white')

    request = None
    while request is None: 
        user_input = input("Enter number from 1 to 4: ")
        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            request = int(user_input)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    koch_snowflake(t, request, 300)

    input("Press Enter to close the window...")

    window.bye()

if __name__ == "__main__":
    main()
