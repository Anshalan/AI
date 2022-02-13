import random

cross_probability = 0.7
mutation_probability = 0.1

crossings = 0
mutations = 0

base_set = []
base_set_binary = []

for x in range(0, 128):
    # for x in range(0, 10):
    base_set.append(x)

for element in base_set:
    temp = bin(element).replace("0b", "").zfill(8)
    # temp =  bin(element).replace("0b", "").zfill(4)
    base_set_binary.append(temp)

random.shuffle(base_set_binary)


# def increase_crossings()

def cross(population):
    for i in range(0, int(len(population) / 2)):
        if random.random() < cross_probability:
            global crossings
            crossings += 2
            parent1 = population[2 * i]
            parent2 = population[2 * i + 1]
            child1 = parent1[:int(len(parent1) / 2)] + parent2[int(len(parent1) / 2):]
            child2 = parent1[:int(len(parent2) / 2)] + parent1[int(len(parent1) / 2):]
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
            each = swap_value(each, random.randint(0, len(each)-1))

print(base_set_binary)
for i in range(0, 51):
    random.shuffle(base_set_binary)
    mutate(base_set_binary)
    cross(base_set_binary)
    base_set_binary.sort()
    print("generation " + str(i) + str(base_set_binary))
    base_set_binary = get_new_generation(base_set_binary)

print("mutations: " + str(mutations))
print("crossings: " + str(crossings))


# aaaa= '10101010'
# b = swap_value(aaaa, 4)
# print(aaaa)
# print(b)
# get_new_generation(base_set_binary)
