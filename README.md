import pygame
import sys

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Tic Tac Toe")  # Aquí está la corrección

# Cargar y escalar imágenes
fondo = pygame.image.load("fondo_juego.png")
circulo = pygame.image.load("circle.png")
equis = pygame.image.load("x.png")
fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (110, 100))
equis = pygame.transform.scale(equis, (110, 100))

# Cargar y escalar la imagen de fondo para la pantalla de inicio
fondo_inicio = pygame.image.load("fondo_inicio1.png")
fondo_inicio = pygame.transform.scale(fondo_inicio, (450, 450))

# Reproducir música de fondo
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1)  # -1 hace que la música se repita indefinidamente

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

# Nombres de los jugadores
nombre_jugador_x = ""
nombre_jugador_o = ""

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

def verificar_empate():
    for fila in tablero:
        if '' in fila:
            return False
    return True

def mostrar_mensaje(texto):
    font = pygame.font.Font(None, 74)
    text = font.render(texto, True, (255, 0, 0))
    screen.blit(text, (75, 200))
    pygame.display.flip()
    pygame.time.delay(2000)

def mostrar_ganador(turno):
    nombre_ganador = nombre_jugador_x if turno == 'x' else nombre_jugador_o
    mostrar_mensaje(f"{nombre_ganador} ha ganado!")

def mostrar_empate():
    mostrar_mensaje("¡Empate!")

def mostrar_turno():
    font = pygame.font.Font(None, 50)
    current_player = nombre_jugador_x if turno == 'x' else nombre_jugador_o
    text = font.render(f"Turno: {current_player}", True, (255, 255, 255))
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

def input_names():
    global nombre_jugador_x, nombre_jugador_o
    input_active = False
    player = 'x'
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('white')
    color = color_inactive
    font = pygame.font.Font(None, 50)
    input_box = pygame.Rect(100, 250, 250, 50)
    nombre_jugador_x = ""
    nombre_jugador_o = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False
                color = color_active if input_active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if player == 'x':
                            nombre_jugador_x = nombre_jugador_x.strip()
                            player = 'o'
                            input_box = pygame.Rect(100, 350, 250, 50)
                        else:
                            nombre_jugador_o = nombre_jugador_o.strip()
                            return
                    elif event.key == pygame.K_BACKSPACE:
                        if player == 'x':
                            nombre_jugador_x = nombre_jugador_x[:-1]
                        else:
                            nombre_jugador_o = nombre_jugador_o[:-1]
                    else:
                        if player == 'x':
                            nombre_jugador_x += event.unicode
                        else:
                            nombre_jugador_o += event.unicode

        screen.blit(fondo_inicio, (0, 0))
        prompt = font.render("Nombre del jugador O:", True, (255, 255, 255)) if player == 'o' else font.render("Nombre del jugador X:", True, (255, 255, 255))
        screen.blit(prompt, (50, 150))
        
        if player == 'x':
            text_surface = font.render(nombre_jugador_x, True, color)
        else:
            text_surface = font.render(nombre_jugador_o, True, color)
        
        width = max(200, text_surface.get_width() + 10)
        input_box.w = width
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

def reset_game():
    global tablero, turno, game_over
    tablero = [['', '', ''],
               ['', '', ''],
               ['', '', '']]
    turno = 'x'
    game_over = False

# Bucle principal del juego
while True:
    main_menu()
    input_names()
    reset_game()
    while not game_over:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if (40 <= mouseX < 415) and (50 <= mouseY < 425):
                    fila = (mouseY - 50) // 125
                    col = (mouseX - 40) // 125
                    if tablero[fila][col] == '':
                        tablero[fila][col] = turno
                        if verificar_ganador():
                            mostrar_ganador(turno)
                            game_over = True
                        elif verificar_empate():
                            mostrar_empate()
                            pygame.time.delay(2000)  # Esperar antes de reiniciar
                            break  # Salir del bucle interno para reiniciar el juego
                        turno = 'o' if turno == 'x' else 'x'

        graficar_board()
        pygame.display.update()
