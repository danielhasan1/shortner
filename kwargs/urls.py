from django.conf.urls import url
from django.contrib import admin
from shorten.views import HomeView,kwrgCBview,about_view,about_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$',about_view),
    url(r'^$',HomeView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$',kwrgCBview.as_view(), name='scode'),
    
]