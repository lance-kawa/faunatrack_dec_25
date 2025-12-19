from rest_framework import serializers
from faunatrack.models import Espece, Observation, Project


class EspeceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Espece
        exclude = ["created_at", "updated_at"]
        

class ObservationSerializer(serializers.ModelSerializer):
    espece_name = serializers.SlugRelatedField(slug_field="nom", queryset=Espece.objects.all(), write_only=True)
    espece = EspeceSerializer(read_only=True)
    location = serializers.SerializerMethodField()
    date_observation = serializers.SerializerMethodField()
    
    class Meta:
        model = Observation
        fields = '__all__'
        read_only_fields = ["id"]
        
    def get_location(self, obj):
        return {
            "latitude": obj.location.latitude,
            "longitude": obj.location.longitude,
        }
    
    def get_date_observation(self, obj):
        return obj.date_observation.strftime("%Y-%m-%d")
    
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ["id"]