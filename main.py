import item
import random
import numpy as np

file = 'data'
cross_probability = 0.8
mutation_probability = 0.1
max_weight = 89
population_size = 20


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


# def check_solution(items, solution, max_weight):
#     total_weight = 0
#     for i in solution:
#         if i == 1:
#             total_weight = total_weight + items[solution.index(i)].weight
#         else:
#             pass
#     if total_weight > max_weight:
#         return check_solution(items, create_solution(items), max_weight)
#     else:
#         return True


def check_value(items, solution):
    value = 0
    for i in solution:
        if i == 1:
            value += items[i].value
    return value


def check_duplicates(solution1, solution2):
    if solution1 == solution2:
        return True
    else:
        return False


def initialize_population(population_size, items, max_weight):
    population = []
    while len(population) < population_size:
        print(population)
        new_solution = create_solution(items)
        print(new_solution)
        if len(population) > 1:
            for i in population:
                if check_duplicates(new_solution, i):
                    pass
                else:
                    population.append(new_solution)
                # else:
                #     if check_solution(items, new_solution, max_weight):
                #         population.append(new_solution)
                #     else:
                #         pass
        else:
            population.append(new_solution)
    return population


def tournament_selection(population):
    first_individual = population[random.randint(0, len(population) - 1)]
    second_individual = population[random.randint(0, len(population) - 1)]
    if check_value(items,first_individual) > check_value(items, second_individual):
        survive = first_individual
    else:
        survive = second_individual
    return survive


def single_point_crossover(parent1, parent2):
    new_parent1 = np.append(parent1[:3], parent2[3:])
    new_parent2 = np.append(parent2[:3], parent1[3:])
    new_parent1.tolist()
    new_parent2.tolist()
    return new_parent1, new_parent2


def inversion_mutation(chromosome):
    print(chromosome)
    start = random.randint(0, round(len(chromosome)/2))
    stop = random.randint(start, len(chromosome))
    mutation = chromosome[start:stop].reverse()
    print(mutation)
    return mutation


if __name__ == "__main__":
    items = read_file(file)
    population = initialize_population(population_size, items, max_weight)
    chromosome = random.choice(population)
    inversion_mutation(chromosome)