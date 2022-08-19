# Université INUKA
### Facultés : Génie et NVlles Technologies Niveau : 4ème Année Devoir : Intra Python
#### Année Académique : 2021-2022 Matin/Médian/Soir Professeur : Jaures PIERRE


Voulant profiter de la rentabilité de la vente des Produits pétroliers dans le Pays ; Max London Petrovic, 
s’est convertit en entrepreneur et veut faire construire 4 nouvelles pompes à essences, qui seront
réparties dans les zones suivantes : Lalue, Tabarre, Clercine et Pétion-ville.

Pour avoir un contrôle total de ses pompes et d’automatiser certaines tâches récurrentes, il veut doter son
entreprise d’une application informatique qui prendra en compte les besoins suivants :

1. Stations :
Nom (Lalue, Tabarre, Clercine ou Petion-ville), capacité(gallon) en Gazoline, % d’utilisation Gazoline,
Capacité (gallon Diesel), % d’utilisation Diesel.
✓ Chaque station est stockée dans un dictionnaire.
✓ Vous pouvez ajouter des champs si c’est nécessaire.
✓ Le champ pourcentage (%) n’est pas à saisir par l’utilisateur mais important pour vérifier le niveau
d’utilisation des essences dans la station. Il est le rapport entre la quantité disponible et la capacité
de la citerne de la pompe pour un type d’essence donné.

- Opération à effectuer :
a. Enregistrer stations, modifier quantité gallon de gazoline et/ou de Diesel d’une station, afficher toutes les
stations.

2. Commandes (ID, quantité gallon Diesel et/ ou Quantité gallon Gazoline, date commande, état)
   
   - ✓ Toutes les commandes doivent être stockées dans une liste.
   
   - ✓ Avant de demander à l’administrateur du système de confirmer une nouvelle commande, le système
   doit afficher la quantité de gallon utilisée et disponible de chaque type d’essence pour chacune des
   stations.
   
   - ✓ Une commande peut contenir soit gazoline, soit Diesel ou les deux.
   
   - ✓ Exemple 1 : Si toutes les stations réunies consomment en moyenne 75% de leur stock de diesel, la
    nouvelle commande passe à 35% (25% disponible, puis un ajout de 10%) du total de gallon de Diesel
    des 4 stations.
   
   - ✓ Exemple 2 : Si toutes les stations réunies consomment en moyenne 50% de leur stock de Gazoline,
    la nouvelle commande passe à 70% (50% disponible, puis un ajout de 20%) du total de gallon de
    Gazoline des 4 stations.
    - ✓ Le système doit générer et enregistrer automatiquement (sans saisir les champs) la nouvelle
    commande en fonction du pourcentage d’essences disponible dans les stations. Après visualisation
    des pourcentages, l’administrateur doit confirmer s’il veut que le système génère et enregistre la
    nouvelle commande.
     - Etat N=Nouvelle, P=Passe. A chaque nouvelle commande toutes les anciennes commandes passent à P.
    Formule :
   - Quantité Gallon Diesel=((Pourcentage total diesel disponible + 10%)*total gallon des 4 stations )/100)
   - Quantité Gallon Gazoline=((Pourcentage total Gazoline disponible + 20%)*total gallon des 4 stations
     )/100).

   - Opération à effectuer : Enregistrer, afficher.

3. Lancer approvisionnement (ID, Station, quantité gallon Diesel, Quantité gallon Gazoline, date app.)
   - ✓ Tous les approvisionnements doivent être stockés dans un Set.
   - ✓ Le système doit demander à l’administrateur de confirmer l’enregistrement de l’approvisionnement
   et de lancer le processus de renflouement des stations.
   - ✓ Apartir de la dernière commande passée (Etat=N), par ordre décroissant du pourcentage d’utilisation
   des essences, le stock d’essence de chaque station est augmenté.

   - Opération à effectuer : Enregistrer, afficher.


4. Vente (ID, Station, quantité gallon Diesel et/ou Quantité gallon Gazoline, date vente)
   - ✓ Toutes les ventes doivent être stockées dans une liste.
   - ✓ A chaque vente, le nombre de gallon de diesel et/ou de gazoline disponible dans une station doit être
   diminué. Le prix du Diesel est de 353 Gourdes/Gallon et le prix du Gazoline est de 250
   Gourdes/Gallon.
   - ✓ Une personne peut acheter plusieurs gallons.
 
- Opération à effectuer : Enregistrer, afficher.