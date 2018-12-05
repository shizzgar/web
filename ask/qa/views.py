from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET
from .models import Question, Answer, QuestionManager
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import AskForm, AnswerForm



def q_details(request, id):
	question = get_object_or_404(Question, id = id)
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save(id)
			answer.save()
			return redirect('q_details', id=question.id)
	else:
		form = AnswerForm()

	return render(request, 'question.html',{
		'question':		question,
		'form':			form,
		#  остальное пожно прописать сразу в шаблоне
	})


@require_GET
def q_new(request):
	q_list = Question.objects.new()
	limit = request.GET.get('limit', 10)
	paginator = Paginator(q_list, limit)
	page = request.GET.get('page', 1)
	questions = paginator.page(page)
	return render(request, 'new.html', {
		"questions":	questions,
		# "questions":	q_list,
		# "paginator":	paginator,
		# "page":			page,
	})


@require_GET
def q_popular(request):
	q_list = Question.objects.popular()
	limit = request.GET.get('limit', 10)
	paginator = Paginator(q_list, limit)
	page = request.GET.get('page', 1)
	questions = paginator.page(page)
	return render(request, 'popular.html', {
		"questions":	questions,
		# paginator:	paginator,
		# page:		page,
	})


def test(request, *args, **kwargs):
	return HttpResponse('OK')


def q_add(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			question.save()
			return redirect('q_details', id=question.id)
	else:
		form = AskForm()

	return render(request, 'ask.html',{
		'form':		form
	})