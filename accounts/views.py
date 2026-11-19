from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from faculty.models import Faculty
from courses.models import Course
from attendance.models import Attendance


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'faculty_count': Faculty.objects.count(),
        'course_count': Course.objects.count(),
        'attendance_count': Attendance.objects.count(),
        'students': Student.objects.all()[:6],
        'recent_attendance': Attendance.objects.select_related('student', 'course')[:8],
    }
    return render(request, 'dashboard.html', context)
