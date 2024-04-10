from constraint import *


def my_fun(*args):
    by_slots = {}
    for slot in args:
        if slot not in by_slots:
            by_slots[slot] = 0

        by_slots[slot] += 1

    for key in by_slots:
        if by_slots[key] > 4:
            return False

    return True


def same(*args):
    distinct = dict()

    for period in args:
        if period not in distinct:
            distinct[period] = 0
        distinct[period] += 1

    return len(distinct.keys()) == 1


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = [f"{key} ({value})" for key, value in papers.items()]

    papers_by_topic = {}
    for key, value in papers.items():
        if value not in papers_by_topic:
            papers_by_topic[value] = []

        papers_by_topic[value].append(f"{key} ({value})")

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    for key, value in papers_by_topic.items():
        if len(value) <= 4:
            problem.addConstraint(same, value)

    problem.addConstraint(my_fun, variables)

    result = problem.getSolution()
    sorted_keys = sorted(result, key=lambda string: int(string.split(" ")[0][5:]))
    for key in sorted_keys:
        print(f"{key}: {result[key]}")

    # Tuka dodadete go kodot za pechatenje
    ...
