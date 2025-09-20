from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse

from .services.pdf_generator import PDFReportGenerator
from .services.excel_generator import ExcelReportGenerator

class ReportDashboardView(LoginRequiredMixin, TemplateView):
    """
    A view that displays the reporting dashboard and allows users
    to select and generate different reports.
    """
    template_name = "reports/report_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reporting Dashboard"
        # In a real scenario, you'd pass lists of courses, students, etc.
        # for the user to select from in the template filters.
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        report_type = request.POST.get("report_type")

        if report_type == "student_pdf":
            # --- Placeholder Data ---
            student_data = {
                "id": 101,
                "name": "Omar (Student)",
                "course": "Advanced Digital Marketing",
                "progress": 85,
                "average_score": 92,
            }
            # --- End Placeholder Data ---
            generator = PDFReportGenerator()
            return generator.generate_student_performance_pdf(student_data)
        
        elif report_type == "course_excel":
            # --- Placeholder Data ---
            enrollments_data = [
                {'student_name': 'Student A', 'student_email': 'a@test.com', 'enrollment_date': '2025-01-10', 'progress': 100, 'status': 'completed'},
                {'student_name': 'Student B', 'student_email': 'b@test.com', 'enrollment_date': '2025-01-12', 'progress': 75, 'status': 'in_progress'},
            ]
            course_title = "Introduction to Python"
            # --- End Placeholder Data ---
            generator = ExcelReportGenerator()
            return generator.generate_course_enrollment_excel(course_title, enrollments_data)

        return self.get(request, *args, **kwargs) # Redirect back if report type is unknown