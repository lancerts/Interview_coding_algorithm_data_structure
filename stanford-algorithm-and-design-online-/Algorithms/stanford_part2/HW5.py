from math import sqrt
from math import factorial
from time import time
from itertools import combinations



def euc_dist(city1, city2):
    """Computes the Euclidean distance between 'city1' and 'city2', which are
    2-tuple of coordinates."""

    return sqrt(pow(city1[0] - city2[0], 2) + pow(city1[1] - city2[1], 2))
















def main():
    city_num = 1
    cities = {}
    dist_dict = {}
    #with open('test.txt') as file_in:
    with open('tsp.txt') as file_in:
        next(file_in)
        for line in file_in:
            cities[city_num] = map(float, line.strip().split(' '))
            city_num += 1
    for x, y in combinations(range(1, city_num), 2):
        dist_dict[(x, y)] = euc_dist(cities[x], cities[y])
        dist_dict[(y, x)] = dist_dict[(x, y)]
    #pprint(dist_dict)
    return tsp(city_num - 1, dist_dict)


if __name__ == '__main__':
    main()
