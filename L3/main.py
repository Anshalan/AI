import matplotlib.pyplot as plt
import random

def generate_two_sets(size_of_base_set):  # will be split 4:1 | pass dividible by 5
    # size_of_base_set = 2000
    base_set = []
    test_set = []
    rand_weights = [round(random.uniform(-10, 10), 2), round(random.uniform(-10, 10), 2)]
    for i in range(0, size_of_base_set):
        temp = []
        temp.append(round(random.uniform(-10, 10), 2))
        temp.append(round(random.uniform(-10, 10), 2))
        if temp[0] * rand_weights[0] + temp[1] * rand_weights[1] > 0:
            temp.append(1)
        else:
            temp.append(-1)
        base_set.append(temp)
    for j in range(0, int(size_of_base_set / 5 * 4)): #*4
    # for j in range(0, 1000): #*4
        test_set.append(base_set.pop(random.randint(0, len(base_set) - 1)))
    return base_set, test_set


def generate_plot(weights, bias, current_generation, points_dict):
    plt.clf()
    if (current_generation == -1):
        plt.title("verifivation")
    else:
        plt.title("generation {0}".format(current_generation))
    plt.grid(False)
    plt.xlim(-11, 11)
    plt.ylim(-11, 11)
    xA = 11
    xB = -11

    if weights[1] != 0:
        yA = (- weights[0] * xA - bias) / weights[1]
        yB = (- weights[0] * xB - bias) / weights[1]
    else:
        xA = - bias / weights[0]
        xB = - bias / weights[0]
        yA = 11
        yB = -11

    plt.plot([xA, xB], [yA, yB], color='g', linestyle='-', linewidth=2)
    x_coords, y_coords = get_points(points_dict, '-1')
    plt.plot(x_coords, y_coords, 'bo')
    x_coords, y_coords = get_points(points_dict, '1')
    plt.plot(x_coords, y_coords, 'ro')
    plt.show()
    plt.pause(0.5)

def activation(output, threshold):
    if output > threshold:
        return  1
    else:
        return -1

def get_points(data, label):
    x_coords = [float(point.split(",")[0]) for point in data.keys() if data[point] == label]
    y_coords = [float(point.split(",")[1]) for point in data.keys() if data[point] == label]
    return x_coords, y_coords


training_array, test_array = generate_two_sets(100)

data_dictionary = {}
for line in training_array:
    data_dictionary['{0},{1}'.format(line[0], line[1])] = '{0}'.format(line[2])
test_dictionary = {}
for line in test_array:
    test_dictionary['{0},{1}'.format(line[0], line[1])] = '{0}'.format(line[2])


weights = [round(random.uniform(-10, 10), 2), round(random.uniform(-10, 10), 2)]
bias = 1
threshold = 0
learning_rate = 0.05
max_iterations = 1000
plt.ion()
###
generations = 0

for k in range(1, max_iterations):
    hits = 0
    print("________________generation{0}_________________".format(k))
    for i in range(0, len(training_array)):
        sum = 0
        for j in range(0, len(training_array[i]) - 1):
            sum += training_array[i][j] * weights[j]
        output = bias + sum
        y = activation(output,threshold)
        ### weights correction ###
        if y == training_array[i][2]:
            hits += 1
        else:
            for j in range(0, len(weights)):
                weights[j] = weights[j] + (learning_rate * training_array[i][2] * training_array[i][j])
            bias = bias + learning_rate * training_array[i][2]
    generate_plot(weights, bias, k, data_dictionary)
    if hits == len(training_array):
        print("-------------------------------------------------------------")
        print("Algorithm learned within {0} iterations".format(k))
        generations = k
        break
print(weights)
print("DONE")

generate_plot(weights, bias, -1, test_dictionary)
all_points = len(test_array)
correctly_classified = 0
for each in test_array:
    output = each[0] * weights[0] + each[1] * weights[1]
    if activation(output, threshold) == each[2]:
        correctly_classified +=1
print("{0}% of points were classified correctly".format(round(correctly_classified/all_points*100,2)))
