from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LearningPathViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'paths', LearningPathViewSet)

urlpatterns = [
    path('', include(router.urls)),
]