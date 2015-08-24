from django.views.generic import ListView
from django.shortcuts import get_list_or_404

from .models import Question, Answer


class QuestionListView(ListView):
    context_object_name = 'list_of_questions'
    template_name = 'mdls/question_list.html'

    def get_queryset(self):
        return get_list_or_404(Question, pk=self.args[0])