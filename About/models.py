from django.db import models
from django.utils.translation import gettext as _

class AboutModel(models.Model):
    image = models.ImageField(upload_to='About/Aboutmodel/%Y/%m/%d', verbose_name=_('image'))
    title = models.CharField(max_length=200, verbose_name=_('title'))
    sub_title = models.CharField(max_length=250, verbose_name=_('sub title'))
    function1 = models.CharField(max_length=150, verbose_name=_('function1'))
    function2 = models.CharField(max_length=150, verbose_name=_('function2'), null=True, blank=True)


class Team(models.Model):
    image =  models.ImageField(upload_to='About/Team/%Y/%m/%d', verbose_name=_('image'), null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=_('name'))
    position = models.CharField(max_length=50, verbose_name=_('position'), null=True, blank=True)
    sub_title = models.CharField(max_length=150, verbose_name=_('sub title'), null=True, blank=True)
    x_link = models.URLField(verbose_name=_('x link'), null=True, blank=True)
    facebook_link = models.URLField(verbose_name=_('facebook link'), null=True, blank=True)
    instagram_link = models.URLField(verbose_name=_('instagram link'), null=True, blank=True)
    Linkedin_link = models.URLField(verbose_name=_('Linkedin link'), null=True, blank=True)


