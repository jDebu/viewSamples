
from django.conf.urls import url
from django.contrib import admin
from pqrs import  views
from django.contrib.auth.views import login,logout
from django.views import generic
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', generic.TemplateView.as_view(template_name='index.html')),
    url(r'^pqrs/', login_required(views.testView.as_view())),
    url(r'^login/', login, name='login'),
    url(r'^logout/$', logout,name='logout'),
]
