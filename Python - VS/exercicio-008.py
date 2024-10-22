medida = float(input('Qual sua medida ? :'))
km = medida
metro = medida * 1000
cm = medida * 100.000
ml = cm * 10

print('Medida km : {}\nMedida de metro {:4.0f}\nMedida de cm {:6.3f}\nMedida de ml {:7.3f}'.format(km, metro, cm, ml))
