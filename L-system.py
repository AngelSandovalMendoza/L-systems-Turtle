import turtle

def apply_rule(symbol, reglas):
    """Aplica una regla a los simbolos.""" 
    return reglas.get(symbol, symbol)

def process_string(axioma, reglas, iteraciones):
    """Procesa la cadena inicial (axioma) segun las reglas dadas y el numero de iteraciones."""
    current_string = axioma
    for _ in range(iteraciones):
        next_string = ''.join(apply_rule(symbol, reglas) for symbol in current_string)
        current_string = next_string
    return current_string

def draw_l_system(t, instrucciones, angulo, distancia):
    """Dibuja el sistema de Lindenmayer ."""
    stack = []
    for paso in instrucciones:
        if paso == 'F':
            t.forward(distancia)
        elif paso == '+':
            t.left(angulo)
        elif paso == '-':
            t.right(angulo)
        elif paso == '[':
            stack.append((t.position(), t.heading()))
        elif paso == ']':
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()

def main():
    #parametros del sistema de Lindenmayer
    axioma = 'F'
    reglas = {'F': 'C0FF-[C1-F+F+F]+[C2+F-F-F]'}
    iteraciones = 5
    angulo = 22
    distancia = 10

    resultado = process_string(axioma, reglas, iteraciones)

    screen = turtle.Screen()
    screen.bgcolor('white')

    t = turtle.Turtle()
    t.speed(100)
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    draw_l_system(t, resultado, angulo, distancia)

    screen.mainloop()

if __name__ == "__main__":
    main()