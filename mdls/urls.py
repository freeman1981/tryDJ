from django.conf.urls import url

from .views import QuestionListView, StartQuiz, get_name, Foo

urlpatterns = [
    url(r'^$', StartQuiz.as_view(), name='start_quiz'),
    url(r'^(\d+)$', QuestionListView.as_view(), name='question_list'),


    url(r'^your-name/$', get_name),
    url(r'^thanks/$', get_name),
    url(r'^foo/$', Foo.as_view()),
]