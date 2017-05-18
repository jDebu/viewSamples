from django.conf.urls import url, include
from viewflow.flow.viewset import FlowViewSet
from django.contrib.auth.decorators import login_required
from . import views
from .flows import ManageClaimFlow


claims_urls = FlowViewSet(ManageClaimFlow).urls

urlpatterns = [
     url(r'', include(claims_urls) )
]