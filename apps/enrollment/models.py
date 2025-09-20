from djongo import models
from django.conf import settings
from apps.learning.models import Course, LearningPath

class Enrollment(models.Model):
    """
    Connects a student to a course or a learning path they are enrolled in.
    """
    _id = models.ObjectIdField()
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Generic relation to either a Course or a LearningPath
    # In MongoDB, we'll store the ObjectId and the collection name.
    enrollable_id = models.CharField(max_length=24) # To store ObjectId as string
    enrollable_type = models.CharField(max_length=50, choices=[('Course', 'Course'), ('LearningPath', 'LearningPath')])
    
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('in_progress', 'In Progress'), ('completed', 'Completed')],
        default='in_progress'
    )
    progress = models.FloatField(default=0.0) # e.g., 0.75 for 75%
    completed_lessons = models.JSONField(default=list) # Store list of completed lesson IDs
    last_accessed_lesson_id = models.CharField(max_length=24, blank=True, null=True)

    objects = models.DjongoManager()
    
    class Meta:
        # Ensures a student cannot be enrolled in the same item twice.
        unique_together = ('student', 'enrollable_id')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.enrollable_type} ({self.enrollable_id})"