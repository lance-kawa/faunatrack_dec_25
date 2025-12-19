from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from faunatrack.models import Espece, Observation, Project      
from faunatrack.serializers import EspeceSerializer, ObservationSerializer, ProjectSerializer

class HelloWorldView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request):
        return JsonResponse({
            "message": "Hello, world!",
            "user": str(request.user),
            "auth": str(request.auth),
        })
        
        
class ObservationViewset(ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
    
class EspeceViewset(ModelViewSet):
    queryset = Espece.objects.all()
    serializer_class = EspeceSerializer


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"