# from django.http import Http404 # 에러 처리
# from django.shortcuts import render
import datetime

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.utils import timezone

from .models import Choice, Question

# # Create your views here.
# def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     output = ', '.join([q.question_text for q in latest_question_list])
# #     return HttpResponse(output)
# # # 출판일자를 통해 5개씩 qustion을 가져오겠다는 뜻
# # # 뷰에서 페이지의 디자인이 하드코딩 되어 있다고 합시다. 만약 페이지가 보여지는 방식을 바꾸고 싶다면, 이 Python 코드를 편집해야만 할 겁니다. 그럼, 뷰에서 사용할 수 있는 템플릿을 작성하여, Python 코드로부터 디자인을 분리하도록 Django의 템플릿 시스템을 사용해 봅시다.

#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = { 'latest_question_list' : latest_question_list, } # template에 latest_question_list라는 이름으로 latest_question을 전달하겠다는 뜻
#     # return HttpResponse(template.render(context, request))

# # render(shorcut) 활용

# # 모든 뷰에 적용한다면, 더 이상 loader와 HttpResponse를 임포트하지 않아도 됩니다. (만약 detail, results, vote에서 stub 메소드를 가지고 있다면, HttpResponse를 유지해야 할 것입니다.)
# # render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세전째 선택적(optional) 인수로 받습니다. 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = { 'latest_question_list' : latest_question_list, } # template에 latest_question_list라는 이름으로 latest_question을 전달하겠다는 뜻
#     return render(request, 'polls/index.html', context)

# # 에러 처리
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
    
#     # shorcut 사용: get_object_or_404() 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다. 만약 객체가 존재하지 않을 경우, Http404 예외가 발생합니다.
#     # get_object_or_404() 함수처럼 동작하는 get_list_or_404() 함수가 있습니다. get() 대신 filter() 를 쓴다는 것이 다릅니다. 리스트가 비어있을 경우, Http404 예외를 발생시킵니다.
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
# # def vote(request, question_id):
# #     return HttpResponse("You're voting on question %s." % question_id)

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

 # 제너릭 뷰
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]

# 개선시키기
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    if request.method == 'GET':
        do_something()
    elif request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

