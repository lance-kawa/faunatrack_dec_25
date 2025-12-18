# Project Faunatrack 

## STEPS

- Initialiser le projet avec django-admin startproject
- Créer une application avec python manage.py mon_app
- Ecrire mes premiers modèles
    - [Formateur Advice] "Perdez" du temps sur cette partie, ce sont les fondations de votre application. Une mauvaise modèlisation de vos données, entrainera de la dette technique, du code "pas propre" et des features plus compliqué à développer. A terme, vous aurez perdu beaucoup de temps 
    - [Formateur Advice] Pour les équipes "agiles". La modélisation des données (écrire les modèles) prend généralement plus de temps que ce que l'on estime. Il est conseillé de prévoir des ateliers ou des meetings pour que les devs (entre eux et avec les PO) puissent échanger. Une bonne modélisation = code propre = dev content = features facile a implémenter = PO content = Client content. Ne négligez pas cette partie ! 

- Visualiser ma modélisation dans le module admin en enregistrant nos modèles dans admin.py
    - [Formateur Advice] Le module Admin peut vous servir d'étape intermédiaire pour valider une fonctionnalité. Un PO qui peut utiliser et comprendre l'interface d'administration aura des insights sur la fonctionnalité développée.
    - [Formateur Advice] De nombreuses librairies sont disponibles pour améliorer l'UX/UI de l'admin. N'hésitez pas à les utiliser au lieu de "réinventez la roue" : Vous n'avez pas besoin de coder des modules d'export et import de données. django-import-export est bien plus pertinent à utiliser. Il en existe beaucoup renseignez vous avant de vous lancer dans le code.

- Créer des "vues" HTML ou API


### Translations 
`python manage.py makemessages -l fr` => Pour générer le fichier de traduction
`python manage.py compilemessages` => Pour compiler mes traductions une fois complétées

### ORM dans les routes

    # lion = get_object_or_404(Espece, nom="sdfsdf") +> Pour éviter les erreurs 500
    
    # try: 
    #     lion = Espece.objects.get(nom="sdfsdf")
    # except Espece.DoesNotExist:
    #     pass