#!/usr/bin/python3

class Patient:
    """A class representing a patient undergoing
    screening for DT2 complications"""

    "Patient parameters"
    sex = None  # Homme ou Femme
    age = 0  # 15 - 105 ans arbitrairement
    height = 0  # 100 - 220 cm arbitrairement
    weight = 0  # 30 - 200 kg arbitrairement
    tabacco = False  # Tabagisme actif ou sevré depuis < 20 ans
    diabetes_duration = 1  # DT2 duration in years, 2 options < 10 years or < 1 year
    family_health_history = {
        "AAA": False,  # abdominal aortic aneurysm
        "FH": False,  # Familial hypocholesteolemia
        "CMI": False  # Myocardial ischemia chez l'homme < 50 ans ou femme < 60 ans
    }
    cmi = False  # myocardial ischemia
    aomi = False  # aomi or peripheral artery disease, known or symptoms
    retinopathy = False
    peripheral_neuropathy = False
    avc_ait = False
    arterial_stenosis = False  # documented arterial stenosis
    carotid_atherom = False  # Carotid atherosclerotic disease
    cardiac_insufficiency = False
    fa = False  # atrial fibrillation
    q_wave = False  # a q wave found on EKG
    left_ventricle = False  # left ventricular insufficiency or hypertrophy on echography
    ldl = 0.0  # LDL cholesterol level (float)
    ct = 0.0  # Total cholesterol level (float)
    dfg = 90  # Glomerular filtration rate from 0 to 150 arbitrarely, ml/min/1,73 m2 
    hta = False  # high blood pressure
    proteinuria = 0.0  # the level of proteins in urine
    hba1c = 0.0  # the level oh HbA1c
    autonomic_neuropathy = False  # Signs: hypotension orthostatique, dysfonction érectile, incontinence urinaire, gastroparésie, constipation
    two_floors = False  # Can the patient climb 2 floors without difficulty ?
    weight_loss = False  # Have the patient recently lose weight ?
    chronic_pancreatitis = False
    difficult_diabetes = False  # diabete décompensé ou difficile à équilibrer
    saos = False
    nash = False  # stéato-hépatite non alcoolique
    dyspnea = False  # dyspnée non expliquée
    low_income = False  # niveau socio-économique bas
    platelets = 0  # last measured platelets level en G/L
    alat_asat = 0  # last measured ASAT/ALAT level
    dry_skin = False  # dry skin symptoms
    metformin = False
    sport_45 = False  # reprise de l'activité physique soutenue après 45 ans

    """Scores calculations"""
    def bmi(self, weight, height):
        """The calculation of BMI"""
        pass

    def hemorrage_risk(self):
        """Calculation of hemorragic score"""
        pass

    def cardiovascular_risk(self):
        """Calculation of cardiovascular risk"""
        pass

    def coronary_risk(self):
        """Calculation of coronary risk"""
        pass

    def tca_screening(self):
        """Alimentory desorder screening"""
        pass

    def fib4_score(self):
        """FIB4 score calculation"""
        pass

    def irc_grade(self):
        """Renal insufficiency grade calculation"""
        if self.dfg >= 90:
            return "Stade I: pas d'atteinte de l'épuration rénale"
        elif self.dfg >= 60 and self.dfg < 90:
            return "Stade I: insuffisance rénale légère"
        elif self.dfg >= 45 and self.dfg < 60:
            return "Stade IIIA: insuffisance rénale modérée"
        elif self.dfg >= 30 and self.dfg < 45:
            return "Stade IIIB: insuffisance rénale modérée"
        elif self.dfg >= 15 and self.dfg < 30:
            return "Stade IV: insuffisance rénale sévère"
        elif self.dfg < 15:
            return "Stade V: insuffisance rénale terminale"


def main():
    patient_1 = Patient()
    patient_1.dfg = int(input("Quel est le DFG du patient ?"))
    print(patient_1.irc_grade())


if __name__ == "__main__":
    main()
