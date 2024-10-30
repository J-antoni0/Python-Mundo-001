import math

ang = int(input('Qual angulo ?'))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('Seno em {:3.2f} cosseno em {:3.2f} e tangente em {:3.2f}'.format(seno,cosseno,tangente))