from django.views.generic.detail import DetailView

from models import Page


class PageView(DetailView):
    model = Page


class HomepageView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
