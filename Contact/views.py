from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from Contact.forms import ContactForm
from Contact.models import Information


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact') 

    def form_valid(self, form):
        form.save() 
        self.request.session['success'] = True
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['information'] = Information.objects.all()
        # Agar sessiyada success bo‘lsa, uni contextga qo‘shamiz
        if 'success' in self.request.session:
            context['success'] = True
            del self.request.session['success']  # bir martalik chiqsin
        return context
    
