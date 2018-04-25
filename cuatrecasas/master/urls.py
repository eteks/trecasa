from django.conf.urls import url,include
from master import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [    
    url(r'^$', views.Index_pageview.as_view(), name='index'),
    url(r'^actividades/$', views.Actividades_pageview.as_view(), name='actividades'),
   ]