base_set = []
base_set_binary = []


def flip_to_2(set):
    for number in set:
        number = bin(number).replace("0b", "")

for x in range(0, 128):
    y = 2 * (x * x + 1)
    base_set.append(y)
    # base_set_binary.append(bin(y).replace("0b", ""))

print(str(x) + ": " + str(y))

print("base_set: ")
print(base_set)
print("base_set_binary: ")
print(base_set_binary)

# n = 8
# print(n)
# n = bin(n).replace("0b", "")
# print(n)

print(int(3, 2))

def cross(a: int, b: int) -> [int, int]:

