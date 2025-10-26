from django.urls import path
from .views import CategoryListView, CategoryDetailView, TagBlogListView

urlpatterns = [
    path('category/query/', CategoryListView.as_view(), name='category_list'),
    path("category/", CategoryListView.as_view(), name="category"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("tags/<int:pk>/", TagBlogListView.as_view(), name="tag_blogs"),
]