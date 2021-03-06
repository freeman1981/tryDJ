from django.views.generic import ListView
from django.views.generic.base import RedirectView, TemplateView
from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Question
from .forms import NameForm


class QuestionListView(ListView):
    context_object_name = 'list_of_questions'
    template_name = 'mdls/question_list.html'

    def get_queryset(self):
        return get_list_or_404(Question, pk=self.args[0])


class StartQuiz(RedirectView):
    pattern_name = 'question_list'

    def get_redirect_url(self, *args, **kwargs):
        args = (1,)
        return super(StartQuiz, self).get_redirect_url(*args, **kwargs)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/quiz/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'mdls/name.html', {'form': form})


class Foo(TemplateView):

    template_name = 'mdls/temp_same_origin_policy.html'
