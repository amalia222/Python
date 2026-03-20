from math import *


def distance(p1, p2):
    return sqrt((p1[0] ** 2 - p2[0] ** 2) + (p1[1] ** 2 - p2[1] ** 2))


def cluster_average(cluster):
    return [sum(cluster[0]) // len(cluster[0]), sum(cluster[-1]) // len(cluster[-1])]


def cluster_center(cluster):
    sum_distance = [sum([distance(star1, star2) for star1 in cluster]) for star2 in cluster]
    return cluster[sum_distance.index(min(sum_distance))]


def clusterize(dots, eps):
    clusters = []
    for dot in dots:
        matched_index = []
        for i in range(len(clusters)):
            for d in clusters[i]:
                if distance(dot, d) <= eps:
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


stars = list(list(map(float, line.replace(',', '.').split()) for line in open('2701_А.txt').readlines()))
