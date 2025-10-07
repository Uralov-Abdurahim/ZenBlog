from django.shortcuts import render
from django.views.generic import ListView
from Category.models import CategoryModel

class HomeListView(ListView):
    model = CategoryModel
    template_name = "index.html"
    context_object_name = "posts"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_post'] = CategoryModel.objects.filter(featured=True)
        context['recent_posts'] = CategoryModel.objects.filter(featured=False).order_by('-created_at')[:6]
        context['trending_posts'] = CategoryModel.objects.order_by('-views')[:5]  # 🔥 Eng ko‘p ko‘rilgan 5 ta post
        return context
