from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login 
from .forms import StudentRegistrationForm, AdultRegistrationForm
from django.shortcuts import  get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_type = form.cleaned_data.get('user_type')
            if user_type == 'admin':
                user.is_admin = True
            elif user_type == 'student':
                user.is_student = True
            elif user_type == 'employee':
                user.is_employee = True
            user.save()
            msg = 'user created successfully'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.user_type == 'admin':
                    login(request, user)
                    return redirect('adminpage')
                elif user.user_type == 'student':
                    login(request, user)
                    return redirect('student')
                elif user.user_type == 'employee':
                    login(request, user)
                    return redirect('employee')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'login.html', {'form': form, 'msg': msg})
    #         if user is not None and user.is_admin:
    #             login(request, user)
    #             return redirect('adminpage')
    #         elif user is not None and user.is_student:
    #             login(request, user)
    #             return redirect('student')
    #         elif user is not None and user.is_employee:
    #             login(request, user)
    #             return redirect('employee')
    #         else:
    #             msg= 'invalid credentials'
    #     else:
    #         msg = 'error validating form'
    # return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')

def hello_world_view(request):
    return render(request, 'hello_world.html')

def course_overview_view(request):
    return render(request,  'course_overview.html')


# def course_overview_view(request):
#     return render(request,  'course_overview.html')

def curriculum_view(request):
    return render(request,  'curriculum.html')

def messages_view(request):
    return render(request,  'messages.html')

def quiz_view(request):
    return render(request,  'quiz.html')


def student(request):
    return render(request,'student.html')

def student_profile(request):
    return render(request, 'student_profile.html')

def learning_materials(request):
    return render(request, 'learning_materials.html')


def employee(request):
    return render(request,'employee.html')

def logout_confirmation(request):
    return render(request, 'logout-confirmation.html')

# def logout_view(request):
#     # Logic to logout the user
#     logout(request)
#     return redirect('login')

# views.py

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    
    


# views.py
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Course


def landing_view(request):
    return render(request, 'landing.html')

def registration_type_view(request):
    if request.method == 'POST':
        registration_type = request.POST.get('type')
        if registration_type == 'student':
            return redirect('student_registration')
        elif registration_type == 'adult':
            return redirect('adult_registration')
    return redirect('landing')

def student_registration_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form_template.html', {'form': StudentRegistrationForm(), 'success': True})
    else:
        form = StudentRegistrationForm()
    return render(request, 'form_template.html', {'form': form})

def adult_registration_view(request):
    if request.method == 'POST':
        form = AdultRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form_template.html', {'form': AdultRegistrationForm(), 'success': True})
    else:
        form = AdultRegistrationForm()
    return render(request, 'form_template.html', {'form': form})


# Admin views
# @login_required
# def admin_course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'admin/course_list.html', {'courses': courses})

# @login_required
# def delete_course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     course.delete()
#     return redirect('admin_course_list')

# User views
# @login_required
# def user_course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'user/course_list.html', {'courses': courses})

# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     return render(request, 'user/course_detail.html', {'course': course})


