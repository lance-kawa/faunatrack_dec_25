from sys import exception
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import logging
from faunatrack.models import Espece, Observation, Project

logger = logging.getLogger(__name__)



# Create your views here.
def hello_world(request):

    # Nombre total de chaque espèce observée exemple rossignol x3, merle x5
    especes = Espece.objects.all()
    list_especes = []
    for espece in especes:
        data = {
            "nom": espece.nom, 
            "quantite":Observation.objects.filter(espece=espece).aggregate(Sum("quantite"))["quantite__sum"] 
        }
        list_especes.append(data)
        
    
    # list_especes = [
    #     {"espece": espece.nom, "quantite":Observation.objects.filter(espece=espece).aggregate(Sum("quantite")) }
    #     for espece in especes
    # ]

    
    # Nombre d’observations par espèce 
    
    # LEs utilisateurs du projet qui correspond aux observations de Lion/Merle/Rossignlo
    
    # Project_lions
    observations_pks = Observation.objects.filter(espece__nom__icontains="L").values_list("id", flat=True)
    projects_lion = Project.objects.filter(observations__in=observations_pks)

    return render(request, template_name="hello/hello.html", context={
        "project_lions": projects_lion,
        "liste_especes": list_especes,
        "espece_nb_observations": projects_lion,
        "users_projects_lions": projects_lion
    })
    