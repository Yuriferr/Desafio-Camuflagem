import random
import math

class GeneticAlgorithm:
    """
    Encapsula toda a lógica para evoluir uma população de cores
    para encontrar uma cor alvo.
    """
    def __init__(self, target_color, population_size, mutation_rate):
        """
        Inicializa o algoritmo genético.
        :param target_color: Uma tupla (R, G, B) que é o nosso objetivo.
        :param population_size: O número de indivíduos em cada geração.
        :param mutation_rate: A probabilidade de um gene sofrer mutação.
        """
        self.target_color = target_color
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = [self._create_individual() for _ in range(population_size)]

    def _create_individual(self):
        """Cria um indivíduo (cor) com genes [R, G, B] aleatórios."""
        return [random.randint(0, 255) for _ in range(3)]

    def _calculate_fitness(self, individual):
        """Calcula o fitness de um indivíduo (inverso da distância para o alvo)."""
        r_dist = (individual[0] - self.target_color[0]) ** 2
        g_dist = (individual[1] - self.target_color[1]) ** 2
        b_dist = (individual[2] - self.target_color[2]) ** 2
        distance = math.sqrt(r_dist + g_dist + b_dist)
        return 1 / (distance + 1)

    def _selection(self, population_with_fitness):
        """Seleciona um pai (método de roleta)."""
        total_fitness = sum(fitness for _, fitness in population_with_fitness)
        pick = random.uniform(0, total_fitness)
        current = 0
        for individual, fitness in population_with_fitness:
            current += fitness
            if current > pick:
                return individual
        return population_with_fitness[-1][0] # Fallback

    def _crossover(self, parent1, parent2):
        """Realiza o cruzamento (crossover) para criar um filho."""
        child = [
            random.choice([parent1[0], parent2[0]]),
            random.choice([parent1[1], parent2[1]]),
            random.choice([parent1[2], parent2[2]])
        ]
        return child

    def _mutate(self, individual):
        """Aplica uma mutação em um indivíduo."""
        for i in range(3):
            if random.random() < self.mutation_rate:
                mutation_value = random.randint(-20, 20)
                gene = individual[i] + mutation_value
                individual[i] = max(0, min(255, gene))
        return individual

    def run_generation(self):
        """
        Executa uma geração completa: avaliação, seleção, crossover e mutação.
        Retorna o melhor indivíduo da geração e seu fitness.
        """
        # 1. Avaliação
        population_with_fitness = []
        for individual in self.population:
            fitness = self._calculate_fitness(individual)
            population_with_fitness.append((individual, fitness))
        
        population_with_fitness.sort(key=lambda item: item[1], reverse=True)

        # 2. Criação da nova geração
        new_population = []
        
        # Elitismo: Mantém o melhor indivíduo
        best_individual = population_with_fitness[0][0]
        best_fitness = population_with_fitness[0][1]
        new_population.append(best_individual)

        # Preenche o resto com filhos
        while len(new_population) < self.population_size:
            parent1 = self._selection(population_with_fitness)
            parent2 = self._selection(population_with_fitness)
            child = self._crossover(parent1, parent2)
            child = self._mutate(child)
            new_population.append(child)

        self.population = new_population
        return best_individual, best_fitness