from django.conf.urls import url

from .views import QuestionListView

urlpatterns = [
    url(r'^(\d+)$', QuestionListView.as_view(), name='question_list'),
]