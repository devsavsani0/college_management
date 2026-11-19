from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student


@login_required
def student_list(request):
    students = Student.objects.all()
    query = request.GET.get('q')
    if query:
        students = students.filter(name__icontains=query) | students.filter(student_id__icontains=query)
    return render(request, 'students/list.html', {'students': students, 'query': query})


@login_required
def student_add(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST['student_id'], name=request.POST['name'], email=request.POST['email'],
            phone=request.POST['phone'], gender=request.POST['gender'], department=request.POST['department'],
            year=request.POST['year'], status=request.POST['status'])
        messages.success(request, 'Student added successfully.')
        return redirect('student_list')
    return render(request, 'students/form.html')
