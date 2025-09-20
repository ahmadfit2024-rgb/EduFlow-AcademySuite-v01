from rest_framework import viewsets
from apps.enrollment.models import Enrollment
from .serializers import EnrollmentSerializer
# from rest_framework.permissions import IsAuthenticated

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    # permission_classes = [IsAuthenticated]