from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
   path('index.',views.index,name="index"),
   path('',views.home,name="home"),
   path('employdata/',views.employdata,name="employdata"),
   path("company/",views.company,name='company'),
   path("searching_comp/",views.searching_comp,name='searching_comp'),
   path("searching_emp/",views.searching_emp,name='searching_emp'),
   path('empdata/',views.empdata,name="empdata"),
   path('compdata/',views.compdata,name="compdata"),
   path('viewEmpData/',views.viewEmpData,name="viewEmpData"),
   path('viewcompdata/',views.viewcompdata,name="viewcompdata"),
]
