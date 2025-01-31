from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home_func,name="home"),
    path('pathparam/<id>', views.path_param_func,name="pathparam_name"),
    path('queryparam/', views.query_param_func,name="queryparam_name"),
    path('insert/', views.insert_data,name="insert_data"),
    path('formdata/', views.insert_form_data,name="formdata_name"),
    path('rawhtml/', views.raw_html,name="raw_html"),
    path('html/', views.html,name="html_name"),

]
