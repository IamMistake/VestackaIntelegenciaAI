from constraint import *


def available_Marija(is_coming, time_slot):
    if not is_coming:
        return True

    if time_slot in (14, 15, 18):
        return True

    return False


def available_Simona(is_coming, time_slot):
    if not is_coming:
        return True

    if time_slot in (13, 14, 16, 19):
        return True

    return False


def available_Pater(is_coming, time_slot):
    if not is_coming:
        return True

    if time_slot in (12, 13, 16, 17, 18, 19):
        return True

    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", (0, 1))
    problem.addVariable("Simona_prisustvo", (0, 1))
    problem.addVariable("Petar_prisustvo", (0, 1))
    problem.addVariable("vreme_sostanok", (12, 13, 14, 15, 16, 17, 18, 19, 20))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(available_Marija, ("Marija_prisustvo", "vreme_sostanok"))
    problem.addConstraint(available_Simona, ("Simona_prisustvo", "vreme_sostanok"))
    problem.addConstraint(available_Pater, ("Petar_prisustvo", "vreme_sostanok"))

    problem.addConstraint(lambda person1, person2, person3: person1 == 1 and sum([person1, person2, person3]) >= 2,
                          ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"))

    # ----------------------------------------------------
    solutions = problem.getSolutions()

    formatted_printing = [solutions[2], solutions[0], solutions[1], solutions[3]]
    for solution in formatted_printing:
        print("{", end="")
        print(
            f"'Simona_prisustvo': {solution['Simona_prisustvo']}, 'Marija_prisustvo': {solution['Marija_prisustvo']}, 'Petar_prisustvo': {solution['Petar_prisustvo']}, 'vreme_sostanok': {solution['vreme_sostanok']}}}")
