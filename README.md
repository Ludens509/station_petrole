# station_petrole
Voulant profiter de la rentabilité de la vente des Produits pétroliers dans le Pays ; Max London
Petrovic, s’est convertit en entrepreneur et veut faire construire 4 nouvelles pompes à essences, qui seront 
réparties dans les zones suivantes : Lalue, Tabarre, Clercine et Pétion-ville.
Pour avoir un contrôle total de ses pompes et d’automatiser certaines tâches récurrentes, il veut doter son 
entreprise d’une application informatique qui prendra en compte les besoins suivants : 
1. Stations :
Nom (Lalue, Tabarre, Clercine ou Petion-ville), capacité(gallon) en Gazoline, % d’utilisation Gazoline, 
Capacité (gallon Diesel), % d’utilisation Diesel. 
  ✓ Chaque station est stockée dans un dictionnaire. 
  ✓ NB : Vous pouvez ajouter des champs si c’est nécessaire.
  ✓ On considère le pourcentage d’utilisation(consommation) de Gazoline et de Diesel est à 100 % lors 
de l’enregistrement de chaque station et à 0% lors de chaque approvisionnement.
  ✓ Le % d’utilisation de Gazoline et de Diesel diminuent à chaque vente.
  ✓ Le champ pourcentage (%) n’est pas à saisir par l’utilisateur mais important pour vérifier le niveau 
d’utilisation des essences dans la station. Il est le rapport entre la quantité consommée et la quantité 
disponible pour un type d’essence donné.
Opération à effectuer : 
a. Enregistrer stations, modifier quantité gallon de gazoline et/ou de Diesel d’une station, afficher toutesles 
stations.
2. Commandes (ID, quantité gallon Diesel et/ ou Quantité gallon Gazoline, date commande, état)
  ✓ Toutes les commandes doivent être stockées dans une liste.
  ✓ Avant de demander à l’administrateur du système de confirmer une nouvelle commande, le système 
doit afficher la quantité de gallon consommée et disponible de chaque type d’essence pour chacune 
des stations.
  ✓ Une commande peut contenir soit gazoline, soit Diesel ou les deux.
  ✓ Le système doit générer et enregistrer automatiquement (sans saisir les champs) la nouvelle 
commande en fonction de la quantité de gallon d’essences (Diesel et Gazoline) consommée dans les 
stations. Après visualisation des consommations, l’administrateur doit confirmer s’il veut que le 
système génère et enregistre la nouvelle commande.
 Etat N=Nouvelle, P=Passe. A chaque nouvelle commande toutes les anciennes commandes passent à P.
Formule : 
Quantité Gallon Diesel=(1.10 * Total des gallons Diesel manquants des 4 stations ).
Quantité Gallon Gazoline =(1.25 * Total des gallons Gazoline manquants des 4 stations )
 
 Opération à effectuer : Enregistrer, afficher.
Université INUKA
Facultés : Génie et NVlles Technologies Niveau : 4ème Année Devoir : Intra Python
Année Académique : 2021-2022 Matin/Médian/Soir Professeur : Jaures PIERRE
3. Lancer approvisionnement (ID, Station, quantité gallon Diesel, Quantité gallon Gazoline, date app.)
  ✓ Tous les approvisionnements doivent être stockés dans un Set. 
  ✓ Le système doit demander à l’administrateur de confirmer l’enregistrement de l’approvisionnement 
et de lancer le processus de renflouement des stations.
  ✓ Apartir de la dernière commande passée (Etat=N), par ordre décroissant du pourcentage d’utilisation 
des essences, le stock d’essence de chaque station est augmenté.
 Opération à effectuer : Enregistrer, afficher.
4. Vente (ID, Station, quantité gallon Diesel et/ou Quantité gallon Gazoline, date vente)
  ✓ Toutes les ventes doivent être stockées dans une liste.
  ✓ A chaque vente, le nombre de gallon de diesel et/ou de gazoline disponible dans une station doit être 
diminué. Le prix du Diesel est de 353 Gourdes/Gallon et le prix du Gazoline est de 250 
Gourdes/Gallon. 
✓ Une personne peut acheter plusieurs gallons.
 Opération à effectuer : Enregistrer, afficher.
 Travail Conceptuel :
 Il s’agit d’une application Console à développer en Python.