from math import *


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def clusters_average(clusters):
    return [sum(clusters[:][0]) // len(clusters[:][0]), sum(clusters[:][-1]) // len(clusters[:][-1])]


def cluster_center(cluster):
    return min(cluster, key=lambda p: sum(distance(p, q) for q in cluster))

# Альтернатива atan2
def get_angel(center, p):
    dx = p[0] - center[0]
    dy = p[1] - center[1]
    if dx > 0:
        return atan(dy / dx) * 180 / pi
    elif dx < 0 <= dy:
        return (atan(dy / dx) + pi) * 180 / pi
    elif dx < 0 < dy:
        return (atan(dy / dx) - pi) * 180 / pi
    elif dx == 0 and dy > 0:
        return 90.0
    elif dx == 0 and dy < 0:
        return -90.0
    else:
        return 0.0

# -------------- II ------------------
def cross(center, p1, p2):
    a = (p1[0] - center[0]) * (p2[1] - center[1])
    b = (p1[1] - center[1]) * (p2[0] - center[0])
    return a - b

def get_angel_2(center, p1, p2):
    v1 = (p1[0] - center[0], p1[1] - center[1])
    v2 = (p2[0] - center[0], p2[1] - center[1])
    d = v1[0] * v2[0] + v1[1] * v2[1]
    m1 = sqrt(v1[0] ** 2 + v1[1] ** 2)
    m2 = sqrt(v2[0] ** 2 + v2[1] ** 2)
    return acos(max(-1, min(1, d / (m1 * m2)))) * 180 / pi

# --------------------------------------

def clusterize(dots, center, radius=50, max_angle=20):
    points = sorted(
        [s for s in dots if distance(center, s) <= radius],
        key=lambda p: get_angel(center, p)
    )
    clusters = []
    cluster_start = None
    for p in points:
        a = get_angel(center, p)
        if cluster_start is None or a - cluster_start > max_angle:
            clusters.append([p])
            cluster_start = a
        else:
            clusters[-1].append(p)
    return clusters


starsA = list(list(map(float, line.replace(',', '.').split())) for line in open('2701_А.txt').readlines())
starsB = list(list(map(float, line.replace(',', '.').split())) for line in open('2701_Б.txt').readlines())

clusterizeA = clusterize(starsA, [5, -9])
clusters_avgA = clusters_average([cluster_center(cluster) for cluster in clusterizeA])

print(len(clusterizeA), clusters_avgA)

clusterizeB = clusterize(starsB, [-10, -7])
clusters_avgB = clusters_average([cluster_center(cluster) for cluster in clusterizeB])
print(*sorted(clusterizeB, key=len), sep='\n')
print(len(clusterizeB), clusters_avgB)

# Ответ: значения через запятую
answer1 = ...
answer2 = ...

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(27, 2701, answer1 + answer2, 'd9e9ed2266d4d6af1c5ad2e26f510145'))
