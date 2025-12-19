from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from faunatrack.models import Espece, Observation, Project      
from faunatrack.serializers import EspeceSerializer, ObservationSerializer, ProjectSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2NjIyMzg2OCwiaWF0IjoxNzY2MTM3NDY4LCJqdGkiOiJhNDU2YzcwNmI2YmQ0ZDA2OTRiYmI1MTYxYjVlMjM0OCIsInVzZXJfaWQiOiIxIn0.djvnrwUSH9M7Le5DzgaExDNsEcn-aU7wBstlKR-KZJI",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY2MTM3NDk4LCJpYXQiOjE3NjYxMzc0NjgsImp0aSI6ImM0MTgzZWY0ODk5NDQ3YWM5OTdiNDg5ZTQ0OGQ5NWFmIiwidXNlcl9pZCI6IjEifQ.PAvdoxN93c40ODvIeJGgxNCwjl2VYUimX-dxrHJYQ0s"
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