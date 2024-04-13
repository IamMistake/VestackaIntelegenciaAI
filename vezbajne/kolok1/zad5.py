from constraint import *

#["AI_vezbi", "ML_vezbi", "BI_vezbi", ai_casovi, ml_casovi, r_casovi, bi_casovi]
# cAI, cML, cR, cBI
def terminConstraint(*args):
    for termin in args:
        tmp = list(termin)
        last = int(tmp[len(tmp) - 1])
        last += 1
        tmp[len(tmp) - 1] = str(last)
        tmp = ''.join(tmp)
        if tmp in args:
            return False
    return True

def masinskoConstraint(*args):
    casovi = list(args)
    vezba = casovi.pop(len(casovi) - 1)
    tmp = list(vezba)
    last = int(tmp[len(tmp) - 1])
    prelast = int(tmp[len(tmp) - 2]) * 10
    br = prelast + last

    days = ['Mon_', 'Tue_', 'Wed_', 'Thu_', 'Fri_']
    for day in days:
        newTermin = day + str(br)
        if newTermin in casovi:
            return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)

    tmp = ["AI_vezbi", "ML_vezbi", "BI_vezbi"]
    masinsko = ["ML_vezbi"]

    ai_casovi = []
    for i in range(1, int(casovi_AI) + 1):
        name = "AI_cas_" + str(i)
        ai_casovi.append(name)
        tmp.append(name)
    problem.addVariables(ai_casovi, AI_predavanja_domain)

    ml_casovi = []
    for i in range(1, int(casovi_ML) + 1):
        name = "ML_cas_" + str(i)
        ml_casovi.append(name)
        tmp.append(name)
        masinsko.append(name)
    problem.addVariables(ml_casovi, ML_predavanja_domain)

    r_casovi = []
    for i in range(1, int(casovi_R) + 1):
        name = "R_cas_" + str(i)
        r_casovi.append(name)
        tmp.append(name)
    problem.addVariables(r_casovi, R_predavanja_domain)

    bi_casovi = []
    for i in range(1, int(casovi_BI) + 1):
        name = "BI_cas_" + str(i)
        bi_casovi.append(name)
        tmp.append(name)
    problem.addVariables(bi_casovi, BI_predavanja_domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(), tmp)
    problem.addConstraint(terminConstraint, tmp)
    problem.addConstraint(masinskoConstraint, masinsko)
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)