from django.db.models import Count
from wagtail.admin.edit_handlers import ObjectList
from wagtail.contrib.modeladmin.options import ModelAdmin
from wagtail.contrib.modeladmin.views import CreateView, InspectView
from wkhtmltopdf.views import PDFTemplateView

from crm.models import CV, CVGenerationSettings
from home.models import HomePage, TechnologyInfo, ProjectPage


class CreateCVView(CreateView):
    def get_edit_handler(self):
        if hasattr(self.model, 'edit_handler'):
            edit_handler = self.model.edit_handler
        else:
            edit_handler = ObjectList(CV.create_panels)
        return edit_handler.bind_to_model(self.model)

    def get_initial(self):
        site = self.request.site
        user = self.request.user
        settings = CVGenerationSettings.for_site(site)
        home = HomePage.objects.live().first()
        return {
            "title": settings.default_title,
            "experience_overview": settings.default_experience_overview,
            "education_overview": settings.default_education_overview,
            "contact_details": settings.default_contact_details,
            "languages_overview": settings.default_languages_overview,
            "rate_overview": settings.default_rate_overview,
            "working_permit": settings.default_working_permit,
            "full_name": f"{user.first_name} {user.last_name}",
            "earliest_available": home.earliest_available,
            "picture": home.picture
        }


class CVInspectView(PDFTemplateView,
                    InspectView):
    show_content_in_browser = True
    template_name = "cv/body.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['skills'] = TechnologyInfo.objects.annotate(
            projects_count=Count('tag__home_projecttechnology_items')
        ).filter(projects_count__gt=0).order_by('-projects_count')
        context['project_pages'] = ProjectPage.objects.live().order_by('-start_date')
        context['relevant_project_pages'] = self.instance.relevant_project_pages.order_by('-start_date')
        return context

    def get_filename(self):
        return f"{self.instance.full_name} CV and project portfolio for {self.instance.project}.pdf"


class CVAdmin(ModelAdmin):
    model = CV
    menu_icon = 'fa-id-card'
    menu_label = 'CVs'
    create_view_class = CreateCVView
    list_display = ['project', 'created']
    list_filter = ['project', 'created']
    ordering = ['-created']
    inspect_view_enabled = True
    inspect_view_class = CVInspectView
    inspect_template_name = CVInspectView.template_name
