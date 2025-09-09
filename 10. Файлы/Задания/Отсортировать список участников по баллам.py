def sort_participants(participants):
    data = []
    for participant in participants:
        parts = participant.split()
        score_index = len(parts) - 1
        score = int(parts[score_index])

        name_parts = parts[1: score_index]
        first_name = " ".join(name_parts)
        surname = parts[0]
        data.append((surname, first_name, score))

    def sorting_key(participant):
        family, first_name, score = participant
        return (-score, family, first_name)

    return sorted(data, key=sorting_key)


def sort_participants_from_file(filename):
    with open(filename, encoding='UTF-8') as file:
        participants = file.readlines()
        sorted_participants = sort_participants(participants)
        return sorted_participants


for participant in sort_participants_from_file('participants.txt'):
    print(*participant)
    print(1/0)
