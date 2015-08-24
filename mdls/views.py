from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Question, Answer


class QuestionListView(ListView):
    context_object_name = 'list_of_questions'
    template_name = 'mdls/question_list.html'

    def get_queryset(self):
        return get_list_or_404(Question, pk=self.args[0])


class StartQuiz(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'question_list'

    def get_redirect_url(self, *args, **kwargs):
        get_object_or_404(Question, pk=1)
        return super(StartQuiz, self).get_redirect_url(*args, **kwargs)
