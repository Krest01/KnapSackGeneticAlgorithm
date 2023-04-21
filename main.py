import item
import random
import numpy as np

file = 'data'
cross_probability = 0.8
mutation_probability = 0.1
max_weight = 89
population_size = 20
generations = 50


def read_file(file):
    with open(file)as file:
        items = []
        for line in file:
            new_line = line.strip()
            new_line = new_line.split(" ")
            id = new_line[0]
            weight = new_line[1]
            value = new_line[2]
            new_item = item.ITEM(id, weight, value)
            items.append(new_item)
    return items


def create_solution(items):
    solution = []
    i = 0
    while i < len(items):
        solution.append(random.randint(0, 1))
        i = i + 1
    return solution


def check_solution(items, solution, max_weight):
    total_weight = 0
    for i in solution:
        if i == 1:
            total_weight = total_weight + items[solution.index(i)].weight
        else:
            pass
    if total_weight > max_weight:
        return False
    else:
        return True


def check_value(items, solution):
    value = 0
    for i in solution:
        if i == 1:
            value += items[i].value
    return value


# def check_duplicates(solution_1, solution_2):
#     if solution_1 == solution_2:
#         return True
#     else:
#         return False


def initialize_population(population_size, items):
    population = []
    while len(population) < population_size:
        new_solution = create_solution(items)
        population.append(new_solution)
    return population


def tournament_selection(population):
    first_individual = population[random.randint(0, len(population) - 1)]
    second_individual = population[random.randint(0, len(population) - 1)]
    if check_value(items, first_individual) > check_value(items, second_individual):
        survive = first_individual
    else:
        survive = second_individual
    return survive


def single_point_crossover(parent_1, parent_2):
    point = np.random.randint(0, len(parent_1) - 1)
    child_1 = parent_1[:point] + parent_2[point:]
    child_2 = parent_2[:point] + parent_1[point:]
    return child_1, child_2


def inversion_mutation(chromosome):
    for i in range(len(chromosome)):
        if chromosome[i] == 0:
            chromosome[i] = 1
        else:
            chromosome[i] = 0
    return chromosome


# def genetic_algorithm(max_weight, cross_probability, mutation_probability, file, population__size, generations):
#     population = initialize_population()
#     for generation in range(generations - 1):


if __name__ == "__main__":
    items = read_file(file)
    population = initialize_population(population_size, items, max_weight)
    chromosome = random.choice(population)
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    single_point_crossover(parent1, parent2)
    inversion_mutation(chromosome)