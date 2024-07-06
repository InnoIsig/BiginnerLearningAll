def nombre_premier(nombre):
    est_premier = True
    for i in range(2, nombre):
        if nombre % 2 == 0:
            est_premier = False
    if est_premier:
        print("C'est le nombre nombre")
    else:
        print("Ce n'est pas le nombre premier")

nombre = int(input("Entrez un nombre entre premier et non premier "))
nombre_premier(nombre = nombre)

