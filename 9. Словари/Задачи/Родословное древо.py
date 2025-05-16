def build_tree(data):
    tree = {}
    for line in data:
        child, parent = line.split()
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    return tree


def find_ancestors(tree, person):
    ancestors = set()
    q = [person]
    visited = set()

    while q:
        curr = q.pop(0)
        if curr in visited:
            continue


def find_lca(tree, person1, person2):
    ancestors1 = find_ancestors(tree, person1)
    ancestors2 = find_ancestors(tree, person2)
    common_ancestors = ancestors1.intersection(ancestors2)

    lca = None
    max_depth = 0

    for ancestor in common_ancestors:
        depth = 0


input_data = ["Alexei Peter_I", "Anna Peter_I", "Elizabeth Peter_I", "Peter_II Alexei", "Peter_III Anna",
              "Paul_I Peter_III", "Alexander_I Paul_I", "Nicholaus_I Paul_I", "Alexander_I Nicholaus_I",
              "Peter_II Paul_I", "Alexander_I Anna"]

queries = [("Alexei", "Anna"), ("Alexei", "Peter_II"), ("Anna", "Peter_III"), ]