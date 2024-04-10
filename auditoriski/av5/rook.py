from constraint import *


if __name__ == '__main__':
    problem = Problem()

    variables = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8"]
    problem.addVariables(variables, ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"])

    problem.addConstraint(AllDifferentConstraint(), variables)

    res = problem.getSolution()
    print(res)
