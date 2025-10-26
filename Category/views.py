from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CategoryModel, Tag, Comment
from .forms import CommentForm



class CategoryListView(ListView):
    model = CategoryModel
    template_name = "category.html"
    context_object_name = "categories"
    paginate_by = 6

    def get_queryset(self):
        queryset = CategoryModel.objects.all().order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

class CategoryDetailView(DetailView):
    model = CategoryModel
    template_name = "single-post.html"
    context_object_name = "post"



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by('-created_at')
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.category = self.object
            comment.user = request.user
            comment.save()
        return redirect("category_detail", pk=self.object.pk)
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views += 1       # 🔥 Ko‘rishlar sonini oshirish
        post.save(update_fields=['views'])
        return post


class TagBlogListView(ListView):
    model = CategoryModel
    template_name = "category.html"
    context_object_name = "categories"

    def get_queryset(self):
        return CategoryModel.objects.filter(tag__id=self.kwargs['pk']).order_by('-created_at')