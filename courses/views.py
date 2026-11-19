from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from faculty.models import Faculty
from .models import Course


@login_required
def course_list(request):
    query = request.GET.get('q')
    courses = Course.objects.select_related('faculty').all()
    if query:
        courses = courses.filter(name__icontains=query) | courses.filter(code__icontains=query)
    return render(request, 'courses/list.html', {'courses': courses, 'query': query})


@login_required
def course_add(request):
    if request.method == 'POST':
        faculty_id = request.POST.get('faculty') or None
        Course.objects.create(code=request.POST['code'], name=request.POST['name'], department=request.POST['department'],
            credits=request.POST['credits'], faculty_id=faculty_id)
        messages.success(request, 'Course added successfully.')
        return redirect('course_list')
    return render(request, 'courses/form.html', {'faculty': Faculty.objects.all()})
