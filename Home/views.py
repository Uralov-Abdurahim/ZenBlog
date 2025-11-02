from django.shortcuts import render
from django.views.generic import ListView
from Category.models import CategoryModel

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

class HomeListView(ListView):
    model = CategoryModel
    template_name = "index.html"
    context_object_name = "posts"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_post'] = CategoryModel.objects.filter(featured=True)
        context['recent_posts'] = CategoryModel.objects.filter(featured=False).order_by('-created_at')[:6]
        context['trending_posts'] = CategoryModel.objects.order_by('-views')[:5]  # 🔥 Eng ko‘p ko‘rilgan 5 ta post
        context['special'] = CategoryModel.objects.filter(special=True)
        return context

def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_of_use(request):
    return render(request, 'terms_of_use.html')


class TagBlogListView(ListView):
    model = CategoryModel
    template_name = "index.html"
    context_object_name = "tags"

    def get_queryset(self):
        return CategoryModel.objects.filter(tag__id=self.kwargs['pk']).order_by('-created_at')