from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Faculty


@login_required
def faculty_list(request):
    query = request.GET.get('q')
    faculty = Faculty.objects.all()
    if query:
        faculty = faculty.filter(name__icontains=query) | faculty.filter(employee_id__icontains=query)
    return render(request, 'faculty/list.html', {'faculty': faculty, 'query': query})


@login_required
def faculty_add(request):
    if request.method == 'POST':
        Faculty.objects.create(employee_id=request.POST['employee_id'], name=request.POST['name'], email=request.POST['email'],
            phone=request.POST['phone'], department=request.POST['department'], designation=request.POST['designation'],
            joining_date=request.POST['joining_date'])
        messages.success(request, 'Faculty member added successfully.')
        return redirect('faculty_list')
    return render(request, 'faculty/form.html')
