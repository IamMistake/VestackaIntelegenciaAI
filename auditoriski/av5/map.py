from constraint import *

def notEqualColors(color1, color2):
    return color1 != color2

if __name__ == '__main__':
    problem = Problem()

    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    problem.addVariables(variables, ["R", "B", "G"])

    # problem.addConstraint(notEqualColors, ("NT", "WT"))
    pairs = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("SA", "NSW"), ("SA", "Q"), ("SA", "V"), ("NT", "Q"),
             ("Q", "NSW"), ("NSW", "V")]
    for pair in pairs:
        problem.addConstraint(notEqualColors, pair)

    print(problem.getSolution())
    print(problem.getSolutions())

    res_iter = problem.getSolutionIter()
    for i in range(5):
        print(next(res_iter))