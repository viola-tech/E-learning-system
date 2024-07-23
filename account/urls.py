from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('student/', views.student, name='student'),
    path('employee/', views.employee, name='employee'),
    path('hello-world/', views.hello_world_view, name='hello_world'),
    path('course_overview/', views.course_overview_view, name='course_overview'),
    path('curriculum/', views.curriculum_view, name='curriculum'),
    path('messages/', views.messages_view, name='messages'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('student-profile/', views.student_profile, name='student_profile'),
    path('learning-materials/', views.learning_materials, name='learning_materials'),
    
    path('logout-confirmation/', views.logout_confirmation, name='logout_confirmation'),
    # path('logout/', views.logout_view, name='logout'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    
    # Admin URLs
    # path('admin/courses/', views.admin_course_list, name='admin_course_list'),
    # path('admin/courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    # Other admin URLs

    # User URLs
    # path('courses/', views.user_course_list, name='user_course_list'),
    # path('courses/<int:course_id>/', views.course_detail, name='course_detail'),

    
]