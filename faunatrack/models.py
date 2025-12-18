


import uuid
from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Les modèles Abstraits sont très puissants pour éviter de dupliquer du code
# On oublie pas on_delete sur les ForeignKey
# Les méthodes __str__ améliorent l'UX/UI de votre application
# from django.utils.translation import gettext_lazy as _ est votre compagnong idéeal pour les translations
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
        
    project = models.ForeignKey("faunatrack.Project", on_delete=models.CASCADE, related_name="memberships")
    profil_scientifique = models.ForeignKey("faunatrack.ProfilScientifique", on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.VIEWER)
    
    def __str__(self):
        return f"{self.profil_scientifique.user.username} - {self.project.titre} - {self.role}"
    
class ProfilScientifique(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profil_scientifique")
    
    def __str__(self):
        return self.user.username
  
    
class Espece(BaseModel):
    nom = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        pass # Attention cette méthode n'est pas appelée par le bulk delete de l'admin
                    
    
class ObservationManager(models.Manager):
    
    # def get_queryset(self):
    #     return super().get_queryset().exclude(espece__nom="Lion")    
    
    def without_lion(self):
        return self.all().exclude(espece__nom="Lion")   

    
class Observation(BaseModel):
    
    objects = models.Manager()
    mon_manager = ObservationManager()

    espece = models.ManyToManyField(Espece, related_name="observations")
    project = models.ForeignKey("faunatrack.Project", on_delete=models.PROTECT, related_name="observations")
    location = models.ForeignKey("faunatrack.Location", on_delete=models.PROTECT, related_name="observations")
    date_observation = models.DateTimeField(verbose_name=_("Date d'observation"), default=timezone.now)
    quantite = models.IntegerField(verbose_name="Quantité", default=0,
                                   validators=[MinValueValidator(0)])
    notes = models.TextField(null=True, default=None)
    
    def __str__(self):
        return f"{self.project.titre} observations {self.id}"
    
    def save(self, *args, **kwargs):
        created = not self.pk
        if created:
            print("Je suis en train decréer un objet Observation")
        if not created:
            print("Je suis en train de maj un objet")
        if "pythagore" in self.notes:
            self.notes = ""    
        super().save(*args, **kwargs)
                    
    
class ObservationPhotos(BaseModel):
    photo = models.ImageField(upload_to="photos/", null=True)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE )

    
def validate_latitude(value):
    if value < -90 or value > 90:
        raise ValidationError("La latitude doit être comprise entre -90 et 90 deg")
        
class Location(BaseModel):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[validate_latitude])
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        # call api vers google maps pour obtenir le nom de la location
        return f"{self.latitude}, {self.longitude}"

class Project(BaseModel):
    titre = models.CharField(max_length=255)
    description = models.TextField()
 
    def __str__(self):
        return self.titre
    
