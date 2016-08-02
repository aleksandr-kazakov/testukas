from django.shortcuts import render
from django.http import Http404

from app1.models import Question

# Create your views here.
def index(request):
		questions = Question.objects.all()
		return render(request, 'app1/index.html', {
			'questions': questions,
			})

def question_detail(request, id):
	try:
		question = Question.objects.get(id=id)
	except Question.DoesNotExist:
		raise Http404('This question does not exist')
	return render(request, 'app1/question_detail.html', {
		'question': question,
		})