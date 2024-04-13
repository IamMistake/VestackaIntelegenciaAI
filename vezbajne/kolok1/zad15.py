from constraint import *

def fourDiff(*args):
    br = 4
    for i in range(br):
        t = f'T{i + 1}'
        if args.count(t) > 4:
            return False
    return True

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = []
    ai_vars = []
    ml_vars = []
    nlp_vars = []
    for key, value in papers.items():
        ime = key + ' (' + value + ")"
        if value == "AI":
            ai_vars.append(ime)
        elif value == "ML":
            ml_vars.append(ime)
        else:
            nlp_vars.append(ime)
        variables.append(ime)

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    if len(ai_vars) <= 4 and len(ai_vars) != 0:
        problem.addConstraint(AllEqualConstraint(), ai_vars)
    if len(ml_vars) <= 4 and len(ml_vars) != 0:
        problem.addConstraint(AllEqualConstraint(), ml_vars)
    if len(nlp_vars) <= 4 and len(nlp_vars) != 0:
        problem.addConstraint(AllEqualConstraint(), nlp_vars)
    problem.addConstraint(fourDiff, variables)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    keys = sorted(result.keys())
    tmp = keys.pop(1)
    keys.append(tmp)
    for item in keys:
        print(item + ': ' + result[item])
