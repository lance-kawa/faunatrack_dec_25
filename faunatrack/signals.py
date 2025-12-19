from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from faunatrack.models import Observation, ObservationPhotos, ProfilScientifique

User = get_user_model()

@receiver(post_save, sender=User)
def create_profil_scientifique(sender, instance, created, **kwargs):
    
    # with transaction.atomic():
    if created:
        ProfilScientifique.objects.create(user=instance)
    
    
    
    # Observation
    # GET /observation/ => Liste de mes Observation
    # POST /observation/ => Création d'une observation
    # GET /observation/<id>/ => Détail d'une observation
    # PUT/PATCH /observation/<id>/ => Mise à jour d'une observation
    # DELETE /observation/<id>/ => Suppression d'une observation
    # GET /obseratons/export => Exportation des observations
    
    # RPC 
    # /observation/id-moteur/start => Démarrer le moteur
    # /moteur/id-moteur/stop => Arrêter le moteur
    # /moteur/id-moteur/restart => Redémarrer le moteur
    # /moteur/id-moteur/status => Voir le status du moteur
    # /moteur/id-moteur/logs => Voir les logs du moteur
    