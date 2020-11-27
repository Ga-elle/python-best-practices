# Quelques note sur PEP 8

## Quelques règles bien connues

### Mise en page 

 + une ligne doit contenir 80 caractères maximum
 + l'indentation est de 4 espaces
 + ajouter 2 lignes entre deux éléments de haut niveu (ex: des class)
 + séparer chaque fonction par une ligne vide
 + les noms ne doivent pas contenir d'accent

### Docstrings

Commentaire sur plusieurs lignes avec la triple quote """

Chaque partie du code qui se doit de contenir une docstring :
 + tous les modules
 + toutes les fonctions
 + toutes les classes
 + toutes les méthodes de ces classes
 
### Imports

 + import en début de script
 + une ligne par librairie
 + ordre suivant : bibliothèques standard, bibliothèques tierces et imports locaux. Sauter une ligne entre chaque bloc
 
### Espaces dans les instructions

 + pas d'espace avant `:` mais un après. Exemple : `{oeufs: 2}`
 + opérateurs : un espace avant et après. Exemple : `i = 1 + 1`
 + aucun espace avant et après le `=` quand assignement d'une valeur par défaut. Exemple : `def elephant(trompe=True, pattes=4)`
 
### Conventions de nommage

 + **modules** : nom court, tout en minuscules, tiret du bas si nécessaire. Exemple : `great_module`
 + **paquets** : nom court, tout en minuscules, tiret du bas très déconseillés. Exemple : `paquet`
 + **classes** : lettres majuscules en début de mot. Exemple : `MyGreatClass`
 + **exceptions** : similaire aux classes mais avec un Error à la fin. Exemple : `MyGreatError`
 + **fonctions**, **méthodes**, **arguments**,  **variables** : miniscules et tiret du bas ; self en premier paramètre. Exemple : `my_method(self, param=False)`
 + **constantes** : toute en majuscules avec des tirets si nécessaire. Exemple : `I_WILL_NEVER_CHANGE`
 + **privé** : précédé de deux tirets du bas. Exemple : `__i_am_private`
 + **protégé** : précédé d'un tiret du bas. Exemple : `_i_am_protected`
 
### Comparaisons

Par convention, il est conseillé d'utiliser `is`ou `is not` lors d'une comparaison avec `None`.


## Utiliser Pylint

