from math import *


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def clusters_average(clusters):
    return [sum(clusters[:][0]) // len(clusters[:][0]), sum(clusters[:][-1]) // len(clusters[:][-1])]


def cluster_center(cluster):
    sum_distance = [sum([distance(star1, star2) for star1 in cluster]) for star2 in cluster]
    return cluster[sum_distance.index(min(sum_distance))]


def clusterize(dots, eps):
    clusters = []
    for dot in dots:
        matched_index = []
        for i in range(len(clusters)):
            for d in clusters[i]:
                if distance(dot, d) <= eps and (distance(dot, d) // 0.342) <= 100 + eps:
                    matched_index.append(i)
                    break
        if not matched_index:
            clusters.append([dot])
        else:
            first_idx = matched_index[0]
            clusters[first_idx].append(dot)
            for i in reversed(matched_index[1:]):
                clusters[first_idx].extend(clusters[i])
                del clusters[i]
    return clusters


starsA = list(list(map(float, line.replace(',', '.').split())) for line in open('2701_А.txt').readlines())
starsB = list(list(map(float, line.replace(',', '.').split())) for line in open('2701_Б.txt').readlines())

clusterizeA = clusterize(starsA, 3)
clusters_avgA = clusters_average([cluster_center(cluster) for cluster in clusterizeA])

print(len(clusterizeA), clusters_avgA)

clusterizeB = clusterize(starsB, 1.5)
clusters_avgB = clusters_average([cluster_center(cluster) for cluster in clusterizeB])
print(*sorted(clusterizeB, key = len), sep = '\n')
print(len(clusterizeB), clusters_avgB)

# Ответ: значения через запятую
answer1 = ...
answer2 = ...

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(27, 2701, answer1 + answer2, 'd9e9ed2266d4d6af1c5ad2e26f510145'))