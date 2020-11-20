# python-best-practices

## Organiser un script

+ Utiliser la condition sur **__name__** pour ne pas exécuter la fonction main des modules importés.

+ Mettre dans .gitignore l'environnement utilisé.

+ Créer un fichier de dépendances.
```python
pip freeze > requirements.txt`
```
Le faire plutôt manuellement pour éviter d'avoir toutes les librairires fondamentales comme packaging par exemple.

+ Utiliser la variable **__file__**

+ Les imports personnalisés de modules (from os import path, name) ont deux avantages majeurs:
    + Optimisation de la mémoire vive
    + Amélioration de la sécurité: plus vous importez de code, plus vous augmentez le risque que ce dernier soit frauduleux ou mal concu.
    
+ Un paquet contient impérativement un fichier `__init__.py` par module. Un dossier sans ce fichier ne sera pas reconnu comme étant un module du paquet.
Une librairie minimale est organisée de la façon suivante:
 - nom de la librairie
    - setup.py 
    - nom_sous_module
        - sous_module.py
        - __init__.py
        
+ L'option help dans la fonction add_argument de argparse est très utile pour visualiser les arguments nécessaires en entrée
```
python parite.py --help
```


## Debugger

+ Pour debugger, utiliser le package **PDB**.
En particulier, la fonction **set_trace()** permet d'entrer dans le debugger pendant que le programme tourne (on définit le point d'arrêt à l'endroit du set_trace).
Pour quitter PDB, tapez
```
exit()
```
Souvent, pdb n'est pas importé en début de fichier comme les autres packages afin de penser à l'enlever lors de la mise en ligne.


## Gestion des erreurs

+ Il faut anticiper les erreurs et les distinguer les unes des autres:
![handle-errors-with-try-except](Handle-errors-with-try-except.png)
Liste des exceptions: [here](https://docs.python.org/3.6/library/exceptions.html#exceptions.TypeError)
Une excellente pratique qui vous aidera à choisir l'exception à lever est d'écrire des tests unitaires, voire de coder en Test-Driven Development ! Sinon, inspirez-vous de la documentation de Python qui est très bien faite. Regardez également la hiérarchie des exceptions [ici](https://docs.python.org/3.6/library/exceptions.html#exception-hierarchy).

+ Utiliser la fonction raise Warning 


## Traces, logs

+ Utiliser le package **logging** qui permet d'afficher des messages en fonction de leur niveau d'importance (DEBUG, INFO, WARNING, ERROR, CRITICAL)
En début de script, on spécifie le niveau minimal de log attendu :
```
lg.basicConfig(level=lg.DEBUG)
```
On peut aussi le mettre en argument (verbose par exemple).
*Le niveau par défaut de la librairie logging est WARNING.*