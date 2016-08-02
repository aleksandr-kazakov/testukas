from django.conf.urls import include, url
from django.contrib import admin

from app1 import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'testukas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^question/(?P<id>\d+)/', views.question_detail, name='question_detail'),
    url(r'^$', views.index, name='index'),

]
