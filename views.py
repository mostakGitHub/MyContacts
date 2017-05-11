from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Contact

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer
from rest_framework import generics


# For DRF
# To get the JSON data...URL : /rest/contacts/
class ContactList(generics.ListAPIView):
    model = Contact
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# URL : /contact
class IndexView(generic.ListView):
    template_name = 'contact/index.html'
    context_object_name = 'all_contacts'

    def get_queryset(self):
        return Contact.objects.all()

# URL : /contact/3
class ContactDetail(generic.DetailView):
    model = Contact
    template_name = 'contact/detail.html'


class ContactCreate(CreateView):
    model = Contact
    fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'address']


#def update(request, contact_id):
#    contact = Contact.objects.get(pk=contact_id)
#    contact.save()
#    return render(request, 'contact/index.html')


class ContactUpdate(UpdateView):
    model = Contact
    fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'address']
    #template_name = 'contact/update.html'


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact:index')