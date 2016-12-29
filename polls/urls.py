from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: polls/432
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: polls/432/result
    url(r'^(?P<pk>[0-9]+)/result/$', views.ResultsView.as_view(), name='results'),
    # ex: polls/463/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]