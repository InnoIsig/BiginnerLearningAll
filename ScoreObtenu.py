# # Input a Python list of student heights
# print("Bienvenu sur ma plate-forme\n")


# nom = input("Entrez le nom de l'éléve\n")
# postnom = input("Entrez le post-nom\n")
# age = int(input("Entrez l'age\n"))

# print(f"Nom : {nom}\nPostnom : {postnom}\nAge : {age} ans")

# student_score = input("Entrez les points obtenus par chaque  éléves\n").split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
    

# high_score = 0
# for score in student_score:
#     if score > high_score:
#         high_score = score
# print(f"Le premier point est : {high_score}")

import random
snake = '''
         
         ,,'6''-,.
        <====,.;;--.
        _`---===. """==__
      //""@@-\===\@@@@ ""\
     |( @@@  |===|  @@@  ||
      \ @@   |===|  @@  //
        \ @@ |===|@@@ //
         \  |===|  //
___________\|===| //_____,----""""""""""-----,_
  """"---,__`\===`/ _________,---------,____    `,
             |==||                           `\   \
            |==| |          pb                 )   |
           |==| |       _____         ______,--'   '
           |=|  `----"""     `""""""""         _,-'
            `=\     __,---"""-------------"""''
                """"
'''
stop = '''
        uuuuuuuuuuuuuuuuuuuu
          u" uuuuuuuuuuuuuuuuuu "u
        u" u$$$$$$$$$$$$$$$$$$$$u "u
      u" u$$$$$$$$$$$$$$$$$$$$$$$$u "u
    u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
  u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
$ $$$" ... "$...  ...$" ... "$$$  ... "$$$ $
$ $$$u `"$$$$$$$  $$$  $$$$$  $$  $$$  $$$ $
$ $$$$$$uu "$$$$  $$$  $$$$$  $$  """ u$$$ $
$ $$$""$$$  $$$$  $$$u "$$$" u$$  $$$$$$$$ $
$ $$$$....,$$$$$..$$$$$....,$$$$..$$$$$$$$ $
$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
"u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
  "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
    "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
      "u "$$$$$$$$$$$$$$$$$$$$$$$$" u"
        "u "$$$$$$$$$$$$$$$$$$$$" u"
          "u """""""""""""""""" u"
            """"""""""""""""""""

'''

home = '''
 )
       (  (              .^.
        \) )           .'.^.'.
         (/          .'.'---'.'.
        _\)_       .'.'-------'.'.
       (__)()    .'.'-,=======.-'.'.
       (_)__)  .'.'---|   |   |---'.'.
       (__)_),'.'-----|   |   |-----'.'.
       ()__.'.'-------|___|___|-------'.'.
       (_.'.'---------------------------'.'.
       .'.'-------------------------------'.'.
      """""|====..====.=======.====..====|"""""
       ()_)|    ||    |.-----.|    ||    |
       (_)_|    ||    ||     ||    ||    |
       (...|____||____||_____||____||____|
      (_)_(|----------| _____o|----------|
      (_)(_|----------||     ||----------|
      (__)(|----------||_____||----------|
      (_)(_|---------|"""""""""|---------|
      ()()(|--------|"""""""""""|--------|
Zot-wWUwwuw|wwWWwuu|"""""""""""""|uwuwuuW|wuwwuuwu

'''
image_game = [snake, stop, home]
choix_utilisateur = int(input("Entres ton choix entre 0 1 2"))
if choix_utilisateur >= 3 or choix_utilisateur < 0:
    print("Choix invalide")
else:
    image_game([choix_utilisateur])

choix_ordinateur = random.randint(0, 2)
print(image_game[choix_ordinateur])

if choix_utilisateur == 0 and choix_ordinateur == 2:
    print("Le serpent que t'as choisi")
elif choix_utilisateur > choix_ordinateur:
    print("T'as choisi entre de te stoper et la maison")
elif choix_ordinateur == choix_utilisateur:
    print("Pas de gangant")
elif choix_ordinateur > choix_utilisateur:
    print("C'est le serpent ou stop toi")

