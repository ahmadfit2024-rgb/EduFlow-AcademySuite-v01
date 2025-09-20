from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, View):
    """
    A smart view that renders the correct dashboard template
    based on the logged-in user's role.
    """
    login_url = '/login/' # Redirect if not logged in

    def get(self, request, *args, **kwargs):
        user = request.user
        
        # Mapping roles to their respective dashboard templates
        dashboard_templates = {
            'admin': 'dashboards/admin.html',
            'supervisor': 'dashboards/supervisor.html',
            'instructor': 'dashboards/instructor.html',
            'student': 'dashboards/student.html',
            'third_party': 'dashboards/third_party.html',
        }

        # Get the template for the user's role, or redirect to login if role is invalid
        template_name = dashboard_templates.get(user.role)
        
        if template_name:
            # Here you can pass role-specific context to the template
            context = {'user': user}
            return render(request, template_name, context)
        else:
            # Handle cases where user has no role or an invalid one
            # Potentially log this issue and redirect to login
            return redirect('login')