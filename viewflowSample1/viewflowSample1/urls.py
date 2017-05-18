
from django.conf.urls import url,include
from django.contrib import admin
from pqrs import  views
from django.contrib.auth.views import login,logout
from django.views import generic

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', generic.TemplateView.as_view(template_name='index.html')),
    url(r'^pqrs/', include('pqrs.urls',namespace='pqrs')),
    url(r'^login/', login, name='login'),
    url(r'^logout/$', logout,name='logout'),
]

