import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Definir dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Definir la velocidad de la bola
VELOCIDAD = 5

# Definir la clase de la bola (personaje)
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20], pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLANCO, (10, 10), 10) # Dibujar la bolita (círculo)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= VELOCIDAD
        if keys[pygame.K_RIGHT]:
            self.rect.x += VELOCIDAD
        if keys[pygame.K_UP]:
            self.rect.y -= VELOCIDAD
        if keys[pygame.K_DOWN]:
            self.rect.y += VELOCIDAD

        # Si la bolita sale por un lado de la pantalla, aparece en el lado opuesto
        if self.rect.left > ANCHO:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = ANCHO
        if self.rect.top > ALTO:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = ALTO

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Bola")

# Crear bola
bola = Bola()

# Crear grupo de sprites y añadir la bola
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(bola)

# Bucle principal del juego
jugando = True
reloj = pygame.time.Clock()

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar
    todos_los_sprites.update()

    # Renderizar
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

    # Controlar la velocidad del bucle
    reloj.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
