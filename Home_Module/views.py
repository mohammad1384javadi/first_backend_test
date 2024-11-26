from django.shortcuts import render
from django.views.generic import TemplateView

from Account_Module.models import User
from Site_Module.models import SiteSetting


class HomeView(TemplateView):
    template_name = 'Home_Module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting']: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        return context


class AboutUsView(TemplateView):
    template_name = 'Home_Module/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(is_active=True, is_dev=True)
        context['users'] = user
        # dev_skills = DeveloperSkills.objects.all()
        # context['dev_skills'] = dev_skills
        return context


def site_header_component(request):
    site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'shared/header_component.html', context)


def site_footer_component(request):
    site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'shared/footer_component.html', context)
