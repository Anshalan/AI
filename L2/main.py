import random

def generate_full_population():
    ret = []
    for x in range(0, 128):
        ret.append(x)
    return ret


def generate_random_population():
    ret = []
    for x in range(0, 128):
        ret.append(random.randint(0, 127))
    return ret


def cast_to_bin(population):
    ret = []
    for element in population:
        ret.append(bin(element).replace("0b", "").zfill(8))
    return ret

def cast_to_dec(population):
    ret = []
    for each in population:
        ret.append(int(each, 2))
    return ret

def cross(population):
    for i in range(0, int(len(population) / 2)):
        if random.random() < cross_probability:
            global crossings
            crossings += 2
            parent1 = population[2 * i]
            parent2 = population[2 * i + 1]
            child1 = parent1[:int(len(parent1)/2)] + parent2[int(len(parent2)/2):]
            child2 = parent2[:int(len(parent2)/2)] + parent1[int(len(parent1)/2):]
            population[2 * i] = child1
            population[2 * i + 1] = child2


def get_new_generation(population):
    roulette_set = []
    new_population = []
    for each in population:
        for i in range(0, int(each, 2)):
            roulette_set.append(each)
    r_size = len(roulette_set)
    for j in range(0, len(population)):
        new_population.append(roulette_set[random.randint(0, r_size - 1)])
    return new_population


def swap_value(thing, sign):
    if thing[sign] == 0:
        thing = thing[:sign] + "1" + thing[sign + 1:]
    else:
        thing = thing[:sign] + "0" + thing[sign + 1:]
    return thing


def mutate(population):
    for each in population:
        if (random.random() < mutation_probability):
            global mutations
            mutations += 1
            each = swap_value(each, random.randint(1, len(each) - 1))



cross_probability = 0.95
mutation_probability = 0.01
crossings = 0
mutations = 0
number_of_generations = 1000

base_set = generate_full_population()
# base_set = generate_random_population()
base_set_binary = cast_to_bin(base_set)

for i in range(0,number_of_generations):
    if i > 0:
        base_set_binary = get_new_generation(base_set_binary)
    random.shuffle(base_set_binary)
    mutate(base_set_binary)
    cross(base_set_binary)
    # print("generation " + str(i+1) + str(base_set_binary))
base_set_binary.sort(reverse=True)
print("Populacja wejściowa\n" + str(base_set))
print("Populacja po {0} generacjach\n".format(number_of_generations) + str(cast_to_dec(base_set_binary)))
print("mutations: " + str(mutations))
print("crossings: " + str(crossings))

