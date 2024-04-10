from constraint import *


def should_be(s, e, n, d, m, o, r, y):
    return (s * 1000 + e * 100 + n * 10 + d) + (
            1000 * m + 100 * o + 10 * r + e) == 10000 * m + o * 1000 + n * 100 + e * 10 + y


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    problem.addConstraint(AllDifferentConstraint(), variables)
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(should_be, variables)

    # ----------------------------------------------------

    print(problem.getSolution())
