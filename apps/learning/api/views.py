from rest_framework import viewsets
from apps.learning.models import Course, LearningPath
from .serializers import CourseSerializer, LearningPathSerializer
# Import custom permissions later
# from apps.users.api.permissions import IsAdminRole, IsSupervisorRole

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAdminRole] # Add appropriate permissions

class LearningPathViewSet(viewsets.ModelViewSet):
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer
    # permission_classes = [IsSupervisorRole] # Add appropriate permissions