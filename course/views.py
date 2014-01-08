from django.http import HttpResponse
from django.template import RequestContext, loader
from course.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.shortcuts import redirect

@login_required
def lessons(request):
	allLessons = Lesson.objects.all()
	template = loader.get_template('course/lessons.html')
	authenticater = request.user.is_authenticated()
	context = RequestContext(request, {'lessons': allLessons,'authenticated':authenticater,})
	return HttpResponse(template.render(context))

@login_required
def lesson_page(request):
    lesson = Lesson.objects.get(title = request.GET.get("title", "NULL"))
    template = loader.get_template('course/lessonpage.html')
    authenticater = request.user.is_authenticated()
    context = RequestContext(request, {'resources':lesson, 'authenticated':authenticater,})
    return HttpResponse(template.render(context))

@login_required
def logout_user(request):
    logout(request)
    return redirect("lessons")
