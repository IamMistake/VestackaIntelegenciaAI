from constraint import *


def slot_constrain(slot1, slot2):
    day1, time1 = slot1.split("_")
    day2, time2 = slot2.split("_")
    if day1 != day2:
        return True

    return abs(int(time1) - int(time2)) >= 2


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    all_variables = []

    ai_lectures = []
    ml_lectures = []
    r_lectures = []
    bi_lectures = []

    ai_exercises = ["AI_vezbi"]
    bi_exercises = ["BI_vezbi"]
    ml_exercises = ["ML_vezbi"]

    for i in range(casovi_AI):
        ai_lectures.append(f"AI_cas_{i + 1}")

    for i in range(casovi_ML):
        ml_lectures.append(f"ML_cas_{i + 1}")

    for i in range(casovi_R):
        r_lectures.append(f"R_cas_{i + 1}")

    for i in range(casovi_BI):
        bi_lectures.append(f"BI_cas_{i + 1}")

    all_variables += ai_lectures
    all_variables += ml_lectures
    all_variables += r_lectures
    all_variables += bi_lectures
    all_variables += ai_exercises
    all_variables += bi_exercises
    all_variables += ml_exercises

    problem.addVariables(ai_lectures, AI_predavanja_domain)
    problem.addVariables(ml_lectures, ML_predavanja_domain)
    problem.addVariables(r_lectures, R_predavanja_domain)
    problem.addVariables(bi_lectures, BI_predavanja_domain)
    problem.addVariables(ai_exercises, AI_vezbi_domain)
    problem.addVariables(ml_exercises, ML_vezbi_domain)
    problem.addVariables(bi_exercises, BI_vezbi_domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    for activity1 in all_variables:
        for activity2 in all_variables:
            if activity1 == activity2:
                continue

            problem.addConstraint(slot_constrain, (activity1, activity2))

    for lecture in ml_lectures:
        for exercise in ml_exercises:
            problem.addConstraint(lambda slot1, slot2: slot1.split("_")[1] != slot2.split("_")[1], (lecture, exercise))

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
