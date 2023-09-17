#!/usr/bin/python3
"""The main program"""

from patient import Patient
from questions import Questions
from examens import Examens

mon_patient = Patient()
mon_patient_dict = {}

while True:
    # Question 1
    while True:
        sex = input(Questions.q1)
        if sex != "homme" and sex != "femme":
            error = input("Valeur invalide. Recommencez (type ok) ou passez à la question suivante (type next)\n")
            if error == "ok":
                continue
            elif error == "next":
                break
        else:
            mon_patient.sex = sex
            mon_patient_dict["Sexe"] = mon_patient.sex
            break

    print("Mon patient:")
    for k, v in mon_patient_dict.items():
        print("\t{}: {}".format(k, v))
        print()
    break
