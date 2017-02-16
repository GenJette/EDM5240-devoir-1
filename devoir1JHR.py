#coding: utf-8

donald = [format(donald) for donald in range(30000, 100000)]

mike = ["{:05d}".format(mike) for mike in range(0, 18000)]

print(donald, mike)

# Ha ha! Tes noms de variables! :)
# Ton script fonctionne bien, mais il imprime deux listes successivement.
# Il était possible de les jumeler en une seule.
# Et s'il s'agissait d'afficher chaque numéro de permis possible sur une ligne distincte, il aurait été préférable de faire une boucle avec ta nouvelle liste comme ceci:

barrette = donald + mike
for gaetan in barrette:
	print(gaetan)