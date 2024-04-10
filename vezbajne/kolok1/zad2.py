from constraint import *

def totalSum(s, e, n, d, m, o, r, y):
    return (s * 1000 + e * 100 + n * 10 + d) + (m * 1000 + o * 100 + r * 10 + e) \
            == m * 10000 + o * 1000 + n * 100 + e * 10 + y


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)

    """
    S	E	N	D
	M	O	R	E
M	O	N	E	Y
    """

    problem.addConstraint(totalSum, variables)

    # ----------------------------------------------------

    print(problem.getSolution())