from sys import exception
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from faunatrack.models import Espece, Observation, Project




# Create your views here.
def hello_world(request):
    user = request.user
    especes = Espece.objects.all() # Lazy evaluated
    
    # lion = get_object_or_404(Espece, nom="sdfsdf")
    
    # try: 
    #     lion = Espece.objects.get(nom="sdfsdf")
    # except Espece.DoesNotExist:
    #     pass
    # Nombre total de chaque espèce observée exemple rossignol x3, merle x5
    # Nombre d’observations par espèce 
    # LEs utilisateurs du projet qui correspond aux observations de Lion/Merle/Rossignlo
    observations_pks = Observation.objects.filter(espece__nom__icontains="L").values_list("id", flat=True)
    projects_lion = Project.objects.filter(observations__in=observations_pks)

    return render(request, template_name="hello/hello.html", context={
        "especes_quantity_observe": ...,
        "espece_nb_observations": ...
        "users_projects_lions": ...
    })
    