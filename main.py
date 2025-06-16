import pygame
import random
from genetic_algorithm import GeneticAlgorithm

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURAÇÕES GERAIS E DE TELA ---
# Tela mais larga para acomodar o gráfico ao lado
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 600
TARGET_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# --- PARÂMETROS DO ALGORITMO GENÉTICO ---
POPULATION_SIZE = 50
MUTATION_RATE = 0.02

def draw_info(screen, font, generation, best_individual, best_fitness):
    """Renderiza as informações de texto na tela, agora posicionadas na coluna da esquerda."""
    WHITE = (255, 255, 255)
    LIGHT_GRAY = (200, 200, 200)

    # Informações da Geração (centralizada no topo)
    gen_text = font.render(f"Geração: {generation}", True, WHITE)
    screen.blit(gen_text, (SCREEN_WIDTH // 2 - gen_text.get_width() // 2, 10))

    # Textos da Cor Alvo (abaixo do primeiro quadrado)
    target_title_text = font.render("Cor Alvo", True, WHITE)
    screen.blit(target_title_text, (150, 260))
    target_rgb_text = font.render(f"RGB: {TARGET_COLOR}", True, LIGHT_GRAY)
    screen.blit(target_rgb_text, (120, 290))

    # Textos do Melhor Indivíduo (abaixo do segundo quadrado)
    best_title_text = font.render("Melhor da Geração", True, WHITE)
    screen.blit(best_title_text, (150, 510))
    best_rgb_text = font.render(f"RGB: {tuple(best_individual)}", True, LIGHT_GRAY)
    screen.blit(best_rgb_text, (120, 540))
    fitness_text = font.render(f"Fitness: {best_fitness:.4f}", True, LIGHT_GRAY)
    screen.blit(fitness_text, (300, 540))


def draw_fitness_graph(surface, history):
    """
    Desenha o gráfico de fitness, agora maior e posicionado na coluna da direita.
    """
    if len(history) < 2: return

    # Ajusta o tamanho da figura do gráfico para o novo layout
    fig, ax = plt.subplots(figsize=(7, 5), dpi=100, facecolor='#282828')
    ax.set_facecolor('#1c1c1c')
    
    ax.plot(history, color='#00aaff', linewidth=2)
    
    ax.set_title("Evolução do Melhor Fitness", color='white', fontsize=16)
    ax.set_xlabel("Geração", color='white')
    ax.set_ylabel("Fitness", color='white')
    
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_ylim(0, 1)
    ax.set_xlim(left=0, right=max(20, len(history))) # Evita que o gráfico fique "apertado" no início

    fig.tight_layout()
    
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = fig.canvas.get_width_height()

    graph_surface = pygame.image.fromstring(raw_data, size, "RGB")
    
    # Nova posição do gráfico, na coluna da direita
    surface.blit(graph_surface, (450, 50))
    
    plt.close(fig)

def main():
    """Função principal que roda a simulação e a visualização."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Painel de Controle - Algoritmo Genético")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    ga = GeneticAlgorithm(
        target_color=TARGET_COLOR,
        population_size=POPULATION_SIZE,
        mutation_rate=MUTATION_RATE
    )

    generation = 0
    fitness_history = []
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        best_individual, best_fitness = ga.run_generation()
        generation += 1
        fitness_history.append(best_fitness)
        
        # --- Seção de Desenho ---
        screen.fill((40, 40, 40))

        # --- Coluna da Esquerda (Cores) ---
        # Cor Alvo (em cima)
        pygame.draw.rect(screen, TARGET_COLOR, (50, 50, 350, 200))
        # Melhor Cor (em baixo)
        pygame.draw.rect(screen, best_individual, (50, 300, 350, 200))
        
        # --- Coluna da Direita (Gráfico) ---
        draw_fitness_graph(screen, fitness_history)

        # Desenha todos os textos por cima
        draw_info(screen, font, generation, best_individual, best_fitness)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()