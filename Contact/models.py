from django.db import models
from django.utils.translation import gettext as _

class Information(models.Model):
    address = models.CharField(max_length=200, verbose_name=_('address'), null=True, blank=True)
    phone_number = models.CharField(max_length=50, verbose_name=_('phone_number'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('email'), null=True, blank=True)

    class Meta:
        verbose_name = _('Information')
        verbose_name_plural = _('Informations')


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('email'), null=True, blank=True)
    subject = models.CharField(max_length=200, verbose_name=_('subject'), null=True, blank=True)
    message = models.TextField(verbose_name=_('message'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')