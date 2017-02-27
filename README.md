# Altegrad
Project for Advanced Learning for Text and Graph Data

Link for the report : https://www.overleaf.com/8336378nmwndfjxjxgt#/29534773/

Je le mettrai à jour lundi matin.

En gros, il y a 3 jupyter Notebook : 
- un pour découvrir les données et les structures
- un pour analyser les données de la base training
- un pour faire la cross-validation + prédiction sur 80% du training + calcul de l'erreur + prédiction sur test + écriture du fichier

Les deux premiers sont plutôt propres mais pas le troisième.

Pour le moment, j'ai 5 modèles : 
- pour un mail, recommander 10 individus (parmi tous les users de la base !) randomly 
- pour un mail, recommander 10 individus (parmi l'historique de l'expéditeur) randomly
- pour un mail, recommander 10 individus en considérant les 10 personnes à qui l'expéditeur a envoyé le plus de mails
- pour un mail, voir le premier mot du mail, déterminer un destinataire à partir de ce mot et combler les au moins 9 places restantes par la méthode précédente
- faire un TF-IDF mais j'ai oublié de faire la phase de STEM comme un gros boulet

Les problèmes que j'ai rencontré : 
- comment faire la cross-validation ? j'ai utilisé 3 méthodes différentes mais il semble que split aléatoirement (sans prendre en compte la date) donne les résultats les plus satisfaisants
- j'ai un biais sur l'erreur MAP@10 : python me dit 0.29 alors que Kaggle me dit 0.34.
- certaines dates sont à l'an 0001
- il faut faire gaffe aux données : il faut penser à spliter leurs listes (voir training_set.mids)

Au niveau de la littérature, certaines méthodes nous promettent du 0.5 (pour le moment, les meilleurs sur Kaggle sont à 0.4) et nous à 0.34.
