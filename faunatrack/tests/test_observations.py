from django.test import TestCase

from faunatrack.models import Observation
from faunatrack.models import Espece
from faunatrack.models import Project
from faunatrack.models import Location
from django.utils import timezone


class ObservationTestCase(TestCase):
    
    def setUp(self):
        self.observation = Observation.objects.create(  
            espece=Espece.objects.create(nom="Test Espece"),
            project=Project.objects.create(titre="Test Project"),
            location=Location.objects.create(latitude=0, longitude=0),
            date_observation=timezone.now(),
            quantite=1,
            notes="Test Notes"
        )
    
    def test_observation(self):
        location = Location.objects.create(latitude=200, longitude=0)
        self.assertLessEqual(location.latitude, 90)
        
        
    
