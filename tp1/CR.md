**Florian Robert & Mamadou Sidibé & Youssef Fellous**
# Rapport TP1.1
## Séance 1
### Partie 1
 1. Nous avons choisi d'utiliser l'éditeur de fichiers Atom qui est très simple
 d'utilisation
 2. Nous ferons le clone plus tard (séance 2)
 3. Le rôle des fichiers est le suivant :
 * Les fichiers du dossier src (sources) contiennent les données sources pour
 un programme compilable (langage : Python, extension : .py), par exemple des
 types de données (data_types), des méthodes ou le code source du programme
 (recherche de solution avec la méthode d'Euler `euler_explicite`)
 * Le fichier CR.md est prévu pour le compte-rendu du TP1 (langage : Markdown,
   extension : .md)
 * Le fichier README.md contient l'énoncé du TP (langage : Markdown, extension :
   .md)

## Partie 2
1. Le programme fonctionne : nous avons utilisé une boucle `for` afin d'actualiser
le pas à chaque étape. Les valeurs de h sont stockées dans un tableau employé
dans la boucle

| h (pas) | Err (erreur) |
|:-------:|:------------:|
|0.2      | 0.06506033134105892|
|0.1      | 0.031075643227486384|
|0.05     | 0.015202834302256153|
|0.025    | 0.007520886771982899|

On remarque que lorsque le pas est divisé par 2, l'erreur commise est aussi
divisée par 2.

**Graphe de Erreur = f(h)**

![Err = f(h) 1](https://github.com/upici/csm1-Frb37/blob/master/tp1/src/Err_fct_h_log.png)

Pour une raison qui nous échappe, le fichier source compile bien mais les images
PNG en sortie affichent un blanc (pas de graphe). De même, le fichier 'euler_explicite_%2u.png' ne sort pas en plusieurs exemplaires (malgré l'instruction
format(i)).



**Florian Robert (travail individuel - séance 2)**

## Séance 2 - Python, Numpy et Matplotlib

2. On considère y' = 1 - y^2 avec t dans [0, 1] :

La solution générale de cette EDO est : y(t) = th(t) avec th la fonction
tangente hyperbolique définie par :

th(t) = (c*e^2t - 1) / (c*e^2t + 1)

Compte tenu des conditions initiales (CI), on trouve : c = (1+y(0))/(1-y(0))

* Pour y(0) = 0 => c = 1
* Pour y(0) = 2 => c = - 3

On effectue quelques ajustements au programme en rajoutant :
* une fonction `sol.th` dans le module *equations* calculant th(t) en fonction
des CI
* une fonction `f_para` dans le même module qui encode la dérivée sous la forme
y'(t) = F(t) = 1-y^2(t)

CONSTATS :

* Pour y = 0, l'affichage du graphe logarithmique semble ne pas fonctionner
(logique !)
* Pour y = 2, il n'y a aucun problème

![Err = f(h) 2](https://github.com/upici/csm1-Frb37/blob/master/tp1/src/Err_fct_h_log_th.png)

* On constate la convergence rapide de la méthode dans les deux cas
* Dans les deux cas, l'erreur Err est une fonction linéaire de h (bien que cela
  soit plus discutable pour la deuxième équation)

3. La méthode RK2 est présentée dans le fichier source /src/.programme.py

Pour une raison que je n'arrive pas à comprendre, mon programme refuse de compiler
et m'affiche le message d'erreur suivant :

y[k+1] = y[k] + h*f(t[k]+0.5*h,y[k]+0.5*h*f(y[k])) # Formule de la méthode RK2

TypeError: f_para() missing 1 required positional argument: 'y'
