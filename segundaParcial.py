import pygame
import sys

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Tic Tac Toe")

# Carga y escalado de imágenes
fondo = pygame.image.load("fondo_juego.png")
circulo = pygame.image.load("circle.png")
equis = pygame.image.load("x.png")

fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (110, 100))  # Escalamos al tamaño adecuado
equis = pygame.transform.scale(equis, (110, 100))      # Escalamos al tamaño adecuado

# Cargar y escalar la imagen de fondo para la pantalla de inicio
fondo_inicio = pygame.image.load("fondo_inicio1.png")
fondo_inicio = pygame.transform.scale(fondo_inicio, (450, 450))

# Coordenadas para dibujar las piezas
coor = [[(40, 50), (165, 50), (290, 50)],
        [(40, 175), (165, 175), (290, 175)],
        [(40, 300), (165, 300), (290, 300)]]

# Tablero de juego
tablero = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

# Variables de juego
turno = 'x'
game_over = False
clock = pygame.time.Clock()

# Función para dibujar el tablero
def graficar_board():
    screen.blit(fondo, (0, 0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'x':
                dibujar_x(fila, col)
            elif tablero[fila][col] == 'o':
                dibujar_o(fila, col)
    mostrar_turno()

def dibujar_x(fila, col):
    screen.blit(equis, coor[fila][col])

def dibujar_o(fila, col):
    screen.blit(circulo, coor[fila][col])

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return True
    return False

def mostrar_ganador(turno):
    font = pygame.font.Font(None, 74)
    text = font.render(f"{turno.upper()} ha ganado!", True, (255, 0, 0))
    screen.blit(text, (75, 200))
    pygame.display.flip()
    pygame.time.delay(2000)

def mostrar_turno():
    font = pygame.font.Font(None, 50)
    text = font.render(f"Turno: {turno.upper()}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

def main_menu():
    menu = True
    while menu:
        screen.blit(fondo_inicio, (0, 0))
        font = pygame.font.Font(None, 74)
        title = font.render("", True, (255, 255, 255))
        screen.blit(title, (75, 50))

        font = pygame.font.Font(None, 50)
        start_button = font.render("Jugar", True, (255, 255, 255))
        exit_button = font.render("Salir", True, (255, 255, 255))
        
        start_button_rect = start_button.get_rect(center=(225, 200))
        exit_button_rect = exit_button.get_rect(center=(225, 300))

        screen.blit(start_button, start_button_rect)
        screen.blit(exit_button, exit_button_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    menu = False
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def reset_game():
    global tablero, turno, game_over
    tablero = [['', '', ''],
               ['', '', ''],
               ['', '', '']]
    turno = 'x'
    game_over = False

# Bucle principal del juego
main_menu()
reset_game()
while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (40 <= mouseX < 415) and (50 <= mouseY < 425):
                fila = (mouseY - 50) // 125
                col = (mouseX - 40) // 125
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    if verificar_ganador():
                        print(f"El jugador {turno} ha ganado!!")
                        mostrar_ganador(turno)
                        game_over = True
                    turno = 'o' if turno == 'x' else 'x'

    graficar_board()
    pygame.display.update()

pygame.quit()
