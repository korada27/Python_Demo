from django.contrib import admin
from django.urls import path
# from django.conf.urls import url

from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getstudents/', views.getAllStudents, name='getstudents'),
    path('currency/', views.getCurrency, name='currency'),
    path('addstudent/', views.addStudent, name='add'),
    path('updatestudent/', views.updateStudent, name='update'),
    path('deletestudent/', views.deleteStudent, name='delete')
]
