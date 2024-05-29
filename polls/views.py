from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse

from .models import Question


# this is a function based view(FBV), there is also a class based view(CBV)


def index(request):
    """
    The index page generally shows the most recent content. We will use the same logic here by using the Django's database API(model API))
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse(f"You are looking at the result of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
