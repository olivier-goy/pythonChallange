from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
