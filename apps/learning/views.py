from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PathBuilderView(LoginRequiredMixin, TemplateView):
    """
    Placeholder for the interactive path builder interface.
    Requires Supervisor role.
    """
    template_name = 'learning/path_builder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add necessary data for the builder, like a list of available courses
        return context

class LessonDetailView(LoginRequiredMixin, TemplateView):
    """
    Placeholder for the student's lesson view interface.
    """
    template_name = 'learning/lesson_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add course and lesson data based on URL parameters
        return context