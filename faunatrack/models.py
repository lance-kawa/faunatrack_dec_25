


import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class ProjectMembership(BaseModel):
    
    class Role(models.TextChoices):
        # CODE = "BDD", "Interface"
        VIEWER = ("viewer", "Observateur")
        CONTRIBUTOR = ("contrib", "Contributeur")
        ADMIN = ("admin", "Administrateur")
        
    project = models.ForeignKey("faunatrack.Project", on_delete=models.CASCADE)
    profil_scientifique = models.ForeignKey("faunatrack.ProfilScientifique", on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.VIEWER)
    
    def __str__(self):
        return f"{self.profil_scientifique.user.username} - {self.project.titre} - {self.role}"
    
class ProfilScientifique(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class Espece(BaseModel):
    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom
    
    
class Observation(BaseModel):
    espece = models.ManyToManyField(Espece)
    project = models.ForeignKey("faunatrack.Project", on_delete=models.PROTECT, related_name="observations")
    location = models.ForeignKey("faunatrack.Location", on_delete=models.PROTECT, related_name="observations")
    date_observation = models.DateTimeField(verbose_name=_("Date d'observation"), default=timezone.now)
    quantite = models.IntegerField(verbose_name="Quantité", default=0)
    notes = models.TextField(null=True, default=None)
    
    def __str__(self):
        return f"{self.project.titre} observations {self.id}"
    
class ObservationPhotos(BaseModel):
    photo = models.ImageField(upload_to="photos/", null=True)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE )

    
class Location(BaseModel):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        # call api vers google maps pour obtenir le nom de la location
        return f"{self.latitude}, {self.longitude}"

class Project(BaseModel):
    titre = models.CharField(max_length=255)
    description = models.TextField()
 
    def __str__(self):
        return self.titre
    
