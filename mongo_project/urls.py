from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django.views.generic import RedirectView
from student import views
import products.urls
# from employee import empviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getstudents/', views.getAllStudents, name='getstudents'),
    path('currency/', views.getCurrency, name='currency'),
    path('addstudent/', views.addStudent, name='add'),
    path('updatestudent/', views.updateStudent, name='update'),
    path('deletestudent/', views.deleteStudent, name='delete'),
    # path(r'\^employee/', include('employee.urls', namespace='employee'))
    # path('employeelogin/', empviews.employeeLogin)
    # path(r'', RedirectView.as_view(
    #     pattern_name='myrestaurants:restaurant_list'), name='home'),
    # url(r'\^admin/', admin.site.urls),
    path('myrestaurants/', include('myrestaurants.urls', namespace='myrestaurants')),
    path('products/', include('products.urls'))
]
