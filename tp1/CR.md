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

![Erreur](/src/Err_fct_h.png)

Pour une raison qui nous échappe, le fichier source compile bien mais les images
PNG en sortie affichent un blanc (pas de graphe). De même, le fichier 'euler_explicite_%2u.png' ne sort pas en plusieurs exemplaires (malgré l'instruction
format(i)).

### Séance 2
