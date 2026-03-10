from math import *

stars = list(list(map(float, line.replace(',', '.').split())) for line in open('Пример 1 A.txt').readlines())

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def cluster_center(cluster):
    sum_dist = [sum([distance(star1, star2) for star1 in cluster]) for star2 in cluster]
    return cluster[sum_dist.index(min(sum_dist))]

def clusterize(points, eps):
    clusters = []

    for point in points:
        matched_indexes = []

        # Проверяем, к какому кластеру близка новая точка
        for i in range(len(clusters)):
            # Если расстояние хотя бы до ОДНОЙ точки кластера <= eps, то это наш кластер
            for p in clusters[i]:
                if distance(point, p) <= eps:
                    matched_indexes.append(i)
                    break

        if not matched_indexes:
            # Если точка далеко от всех, создаем новый кластер
            clusters.append([point])
        else:
            # Точка подошла. Добавляем ее в первый найденный кластер
            first_idx = matched_indexes[0]
            clusters[first_idx].append(point)

            # Если точка оказалась на границе и зацепила сразу несколько кластеров — сливаем их
            for i in reversed(matched_indexes[1:]):
                clusters[first_idx].extend(clusters[i])
                del clusters[i]

    return clusters

clusters = clusterize(stars, 1)
center0 = cluster_center(clusters[0])
center1 = cluster_center(clusters[1])
print(int(center0[0] * 10000), int(center0[1] * 10000))
print(int(center1[0] * 10000), int(center1[1] * 10000))



