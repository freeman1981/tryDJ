from django.conf.urls import url

from .views import QuestionListView, StartQuiz

urlpatterns = [
    url(r'^$', StartQuiz.as_view(), name='start_quiz'),
    url(r'^(\d+)$', QuestionListView.as_view(), name='question_list'),
]