from django.db import models
from django.contrib.auth.models import User
from core.abstract import TimeStampedModel
from django.utils.translation import gettext as _

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('tag'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
    

class CategoryModel(TimeStampedModel):
    image = models.ImageField(upload_to='CategoryModel/%Y/%m/%d', verbose_name=_("image"))
    title = models.CharField(max_length=150, verbose_name=_('title'))
    author = models.CharField(max_length=100, verbose_name=_('author'))
    sub_title = models.CharField(max_length=400, verbose_name=_('sub title'))
    second_title = models.CharField(max_length=100, blank=True, verbose_name=_('second_title'))
    text = models.TextField(null=True, blank=True, verbose_name=_('text'))
    tag = models.ManyToManyField(Tag, related_name='blogs', blank=True, verbose_name=_('tag'))
    featured = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Comment(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="comments", verbose_name=_('category'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    text = models.TextField(verbose_name=_('text'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f"{self.user.username} - {self.category.title}"
    


    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

