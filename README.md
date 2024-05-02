# exam-ansible

## Contexte et objectif :

Vous avez été recruté en tant qu'ingenieur DevOps dans une nouvelle statup e-commerce qui souhaite créer et déployer un nouveau site Web.

Après consultation avec l'équipe de développeurs, il a été déterminé que la solution utilisée sera Wordpress pour le serveur Web et MySQL pour stocker les données. En tant qu'ingénieur DevOps, vous avez pour objectif d'automatiser ce déploiement en créant deux rôles :

- Un rôle devra déployer Wordpress.

- Un autre autre rôle devra déployer une base de données MySql.

Il est primordial que le serveur Web puisse communiquer avec la base de données.

Afin de vérifier que vos rôles exécutent leurs tâches comme prévu, vous êtes chargé d'écrire des tests unitaires afin de valider leur fonctionnement avant le déploiement en production pour le site e-commerce de la société. Ces tests serviront à vérifier la connexion entre le serveur Web Wordpress et la base de données MySql, ainsi qu'à vérifier si les utilisateurs ont bien accès à la page d'accueil du site.

## Livrables:

Pour valider l'évaluation, vous devrez envoyer en format Zip :

- Deux arborescences de rôles avec les scripts répondant aux besoins de l'énoncé.

- Le playbook qui vous permettra d'orchestrer le lancement de vos rôles.

- Les logs des résultats associés aux tests dans un fichier .txt.

- Les scripts doivent être fonctionnels, peu importe l'environnement utilisé.

## Quelques conseils pour vous lancer :

- Créez un utilisateur "root" pour votre base de données afin que le serveur web puisse se connecter à celle-ci.

- Le protocole par défault utilisé par tous les serveurs Web est http, celui-ci est ouvert sur le port 80.

- Le protocole de connection MySql est ouvert sur le port 3306 par défaut.

- Pour une architecture complexe, il vaut mieux diviser votre configuration entre plusieurs rôles que d'écrire un seul playbook volumineux.

- Un rôle par machine, commencez par construire votre inventaire.

- Vous pouvez tout à fait créer vos propres tests personnalisés avec Python et la librairie pytest ou request.

- Pour cela, vous pouvez utiliser Molecule et réaliser vos tests avec le "vérificateur" testinfra que vous pouvez spécifier lors de la création du rôle.
