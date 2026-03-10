# Calculadora funcional

nmb1 = 1
nmb2 = 1
action = ""

if action == "+":
  result = round(float(nmb1),2) + round(float(nmb2),2)

if action == "-":
  result = round(float(nmb1),2) - round(float(nmb2),2)

if action == "x":
  result = round(float(nmb1),2) * round(float(nmb2),2)

if action == "/":
  if round(float(nmb2),2) == round(float(0),2):
    print("you can divide by 0")
    break
  result = round(float(nmb1),2) / round(float(nmb2),2)
