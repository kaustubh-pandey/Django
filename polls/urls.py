from django.conf.urls import url

from . import views

app_name="polls"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #detail
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    #results
    url(r'^(?P<choice_id>[0-9]+)/results/$',views.results,name='results'),
    #vote
    url(r'^(?P<choice_id>[0-9]+)/vote/$',views.vote,name='vote'),
]
