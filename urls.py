from django.conf.urls import url
from . import views

from .views import ContactList

app_name = 'contact'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ContactDetail.as_view(), name='detail'),
    url(r'^add/$', views.ContactCreate.as_view(), name='contact-add'),

    #url(r'^update/(?P<pk>[0-9]+)/$', views.update, name='update'),

    url(r'^update/(?P<pk>[0-9]+)/$', views.ContactUpdate.as_view(), name='contact-update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ContactDelete.as_view(), name='contact-delete'),

    #url(r'^$', ContactList.as_view(), name='index'),
]