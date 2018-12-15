from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Question, Answer, QuestionManager
from .forms import AskForm, AnswerForm, LoginForm, SignupForm



def q_details(request, id):
	question = get_object_or_404(Question, id = id)
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			answer.author = request.user
			answer.question_id = id
			answer.save()
			return render(request, 'question.html',{
					'question':		question,
					'form':			form,
					#  остальное пожно прописать сразу в шаблоне
			})
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
			question.author = request.user
			question.save()
			return redirect('q_details', id=question.id)
	else:
		form = AskForm()

	return render(request, 'ask.html', {
		'form':		form
	})


def signup(request):
	error = ''
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user_data = form.save()
			user = User.objects.create_user(user_data['username'], user_data['email'], user_data['password'])
			login(request, user)
			return redirect('q_new')
		else:
			error = 'Something wrong with your data'
	else:
		form = SignupForm()
	
	return render(request, 'signup.html', {
		'error':	error,
		'form':		form,
	})
	

def logining(request):
	error = ''
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user_data = form.save()
			user = authenticate(request, username=user_data['username'], password=user_data['password'])
			if user:
				login(request, user)
				return redirect('q_new')
			else:
				error = 'Something wrong'
	else:
		form = LoginForm()

	return render(request, 'login.html', {
		'error':	error,
		'form':		form,
	})

