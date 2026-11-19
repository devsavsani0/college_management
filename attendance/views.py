from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Attendance
from students.models import Student
from courses.models import Course


@login_required
def attendance_list(request):
    records = Attendance.objects.select_related('student', 'course').all()
    return render(request, 'attendance/list.html', {'records': records})


@login_required
def attendance_add(request):
    if request.method == 'POST':
        Attendance.objects.update_or_create(
            student_id=request.POST['student'], course_id=request.POST['course'], date=request.POST['date'],
            defaults={'status': request.POST['status']})
        messages.success(request, 'Attendance recorded successfully.')
        return redirect('attendance_list')
    return render(request, 'attendance/form.html', {'students': Student.objects.all(), 'courses': Course.objects.all()})
