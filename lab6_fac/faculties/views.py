from rest_framework import viewsets
from faculties.serializers import FacultiesSerializer
from faculties.models import Faculties

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculties.objects.all().order_by("date_modified")
    serializer_class = FacultiesSerializer
