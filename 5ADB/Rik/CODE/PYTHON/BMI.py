cm = int(input("Wat is je lengte (cm)"))
gewicht = int(input("Wat is je gewicht? (kg)"))
lengte = cm/100

f_bmi = gewicht/(lengte*lengte)
bmi = round(f_bmi, 2)
if bmi < 18.5:
    print(f"Je BMI is {bmi}, en dit is ondergewicht")
elif 18.5 < bmi < 24.9:
    print(f"Je BMI is {bmi}, en dit is normaal")
elif 20.0 < bmi < 29.9:
    print(f"Je BMI is {bmi}, en dit is overgewicht")
elif 30 < bmi:
    print(f"Je BMI is {bmi}, en dit is obees")
else:
    print(f"Onverwachte fout, je BMI is {bmi}")