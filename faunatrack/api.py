from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from faunatrack.models import Espece, Observation, Project      
from faunatrack.serializers import EspeceSerializer, ObservationSerializer, ProjectSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2NjIyMzAyNCwiaWF0IjoxNzY2MTM2NjI0LCJqdGkiOiI0NDE4OTE4NmQ5MDA0MTczYTI5NGVhNWRjYjZiMWRkZCIsInVzZXJfaWQiOiIxIn0.Vim0GF-nlxslRjjLlhscu2H5Z0UfpugZaX_h4r73Gis",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY2MTM2NjU0LCJpYXQiOjE3NjYxMzY2MjQsImp0aSI6ImM0Y2E5M2ZhZjgzNTQ3NzBhNDkzYzhlYjM5YmJjOWI2IiwidXNlcl9pZCI6IjEifQ.XIm8Io9nDQuG_F_MCqur7mFIF5SCFJ5LWPh9GPuJWxY"
# }

# {
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY2MTM2NzQ3LCJpYXQiOjE3NjYxMzY3MTcsImp0aSI6ImM0ZDU4YjU5NzE3NTQzOWE5NmZiZWU3MzYyOTdkMzRjIiwidXNlcl9pZCI6IjEifQ.ZDLlqoPz6ak4h5SoHyugutrQLaSLjMckmrL4UxoQ6IM"
# }
class HelloWorldView(APIView):
    permission_classes = []  # Allow any
    
    def get(self, request):
        return JsonResponse({
            "message": "Hello, world!",
            "user": str(request.user),
            "auth": str(request.auth),
        })
        
        
class ObservationViewset(ModelViewSet):
    permission_classes = [] # API PUBLIQUE
    authentication_classes = [JWTAuthentication]
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
    
class EspeceViewset(ModelViewSet):
    queryset = Espece.objects.all()
    serializer_class = EspeceSerializer


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"