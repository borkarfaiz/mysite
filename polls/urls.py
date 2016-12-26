from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: polls/
    url(r'^$', views.index, name='index'),

    # ex: polls/432
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: polls/432/result
    url(r'^(?P<question_id>[0-9]+)/result/$', views.results, name='result'),

    # ex: polls/463/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]