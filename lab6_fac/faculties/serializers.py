from faculties.models import Faculties
from rest_framework import serializers

class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ["pk", "faculty_name", "passing_score", "is_growing", "date_modified"]