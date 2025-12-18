
from django.db.models import Q, Count, Sum
from django.shortcuts import  redirect, render
import logging

from django.urls import reverse_lazy
from faunatrack.forms import ObservationForm
from faunatrack.models import Espece, Observation, ProfilScientifique, Project
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

logger = logging.getLogger(__name__)



# Create your views here.
def hello_world(request):
    
    if not request.user.is_authenticated:
        return redirect("/")

    # Nombre total de chaque espèce observée exemple rossignol x3, merle x5
    especes = Espece.objects.all()
    list_especes = []
    for espece in especes:
        data = {
            "nom": espece.nom, 
            "quantite":Observation.objects.filter(espece=espece).aggregate(Sum("quantite"))["quantite__sum"] 
        }
        list_especes.append(data)

    # Nombre d’observations par espèce 
    espece_nb_observations = Observation.objects.all().values("espece__nom").annotate(nb_obs=Count("id"))
 
    
    # LEs utilisateurs du projet qui correspond aux observations de Lion/Merle/Rossignlo
    obs = Observation.objects.filter(espece__nom="Lion")
    users_lions = Project.objects.filter(observations__in=obs.values_list("id", flat=True)).values("titre", "memberships__profil_scientifique__user__username")
    
    
    # projets = Projet.objects.annotate(nombre_d_especes=Count('observation__espece', distinct=True)) 
    # Project_lions
    # observations_pks = Observation.objects.filter(espece__nom__icontains="L").values_list("id", flat=True)
    # projects_lion = Project.objects.filter(observations__in=observations_pks)

    return render(request, template_name="hello/hello.html", context={
        # "project_lions": projects_lion,
        "liste_especes": list_especes,
        "espece_nb_observations": espece_nb_observations,
        "users_projects_lions": users_lions
    })
    
    
    
class AuthenticationMixin(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        try:
            return self.request.user.profil_scientifique
        except ProfilScientifique.DoesNotExist as e:
            logger.error(e)
            return False

class ObservationList(AuthenticationMixin, ListView):
    # queryset = Observation.objects.all()
    template_name = "observation/list.html"
    permission_required = "faunatrack.view_observation"

    
    def get_queryset(self):
        return Observation.objects.all().values("espece__nom").annotate(nb_obs=Count("id"))
        
    
class ObservationCreate(AuthenticationMixin, CreateView):
    model = Observation
    form_class = ObservationForm
    template_name = "observation/create.html"
    success_url = reverse_lazy("observations_list")
    