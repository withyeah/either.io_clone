from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'ei/index.html', context)
    
def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comments = question.answer_set.all()
    first = len(Answer.objects.filter(pick='True').filter(question_id=question_pk))
    second = len(Answer.objects.filter(pick='False').filter(question_id=question_pk))
    answernum = len(Answer.objects.filter(question_id=question_pk))
    if answernum:    
        first = int((first/answernum)*100)
        second = int((second/answernum)*100)
    context = {
        'question': question,
        'comments': comments,
        'first': first,
        'second': second,
    }
    return render(request, 'ei/detail.html', context)

def answer_create(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    pick = request.POST.get('pick')
    comment = request.POST.get('comment')
    answer = Answer(question=question, pick=pick, comment=comment)
    answer.save()
    return redirect('ei:detail', question.pk)

def answer_delete(request, question_pk, answer_pk):
    answer = Answer.objects.get(pk=answer_pk)
    if request.method == 'POST':
        answer.delete()
        return redirect('ei:detail', question_pk)
    else:
        return redirect('ei:detail', question_pk)