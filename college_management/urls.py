from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('faculty/', include('faculty.urls')),
    path('courses/', include('courses.urls')),
    path('attendance/', include('attendance.urls')),
]
