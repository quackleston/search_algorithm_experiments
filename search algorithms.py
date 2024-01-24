from time import perf_counter
import random
import statistics


def linear_search(array, e):
    """
    :param array: a list with items
    :param e: what we are looking for
    :return: if we found it or not
    """
    index = 0
    found = False
    while index < len(array) and found == False:
        if array[index] == e:
            found = True
        else:
            index += 1

    return found


def binary_search(array, e):
    index1 = 0
    indexN = len(array) - 1
    found = False

    while index1 <= indexN and found == False:
        indexM = (index1 + indexN) // 2
        if array[indexM] == e:
            found = True
        else:
            if e < array[indexM]:
                indexN = indexM - 1
            else:
                index1 = indexM + 1
    return found


print(linear_search([1, 2, 3, 4], 4))
print(binary_search([1, 2, 3, 4, 5, 6], 4))


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXPERIMENT LAB
#
# N: 1000       binary search:       linear search:
# N: 5000       binary search:       linear search:
# N: 10000      binary search:       linear search:

n = 80000
dummyArray = []
for i in range(n):
    dummyArray.append(random.randrange(2, 100, 2))

print(dummyArray)

# generate a possibility of 100 numbers to look for
t = 100
target = random.sample(dummyArray, t // 2)  # k is initialized with K//2 number of elements derived from array
for i in range(t // 2):
    odd_rand_num = random.randrange(1, 100, 2)
    target.append(odd_rand_num)  # it is then filled with K//2 number of odd numbers
random.shuffle(target)


binaryRes = []
linearRes = []

sortedDummy = sorted(dummyArray)

for i in range(3):
    counterStart = perf_counter()
    for i in target:
        linear_search(sortedDummy, i)
    counterStop = perf_counter()
    linearRes.append(((counterStop-counterStart) * 1000))

for i in range(3):
    counterStart = perf_counter()
    for i in target:
        binary_search(sortedDummy, i)
    counterStop = perf_counter()
    binaryRes.append(((counterStop - counterStart) * 100))

print(f"\nRESULTS:\nlinear results: {statistics.mean(linearRes)}\nbinary results: {statistics.mean(binaryRes)}")

if statistics.mean(binaryRes) < statistics.mean(linearRes):
    print(f"binary search is faster \nfor target: {t}\nin n: {n}")
else:
    print(f"linear search is faster \nfor target: {t}\nin n: {n}")